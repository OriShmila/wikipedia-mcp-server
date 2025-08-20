# Wikipedia MCP Server

A Model Context Protocol (MCP) server providing access to Wikipedia through 10 tools: search, retrieve articles, summarize content, extract facts, get coordinates, and more.

## Features
- **100% Test Coverage** - 31 test cases, full schema validation
- **Multi-language Support** - Access different Wikipedia editions  
- **Robust Error Handling** - Graceful API error handling

## Available Tools

| Tool | Description |
|------|-------------|
| `search_wikipedia` | Search for articles matching a query |
| `get_article` | Get complete article content |
| `get_summary` | Get article summary |
| `summarize_article_for_query` | Get query-focused summary |
| `summarize_article_section` | Summarize specific sections |
| `extract_key_facts` | Extract key facts from articles |
| `get_related_topics` | Find related articles and categories |
| `get_sections` | Get article structure and sections |
| `get_links` | Get all links within an article |
| `get_coordinates` | Get geographic coordinates |

## Installation

```bash
# Install with uvx
uvx --from git+https://github.com/yourusername/wikipedia-mcp-server wikipedia-mcp-server

# Or local development
git clone https://github.com/yourusername/wikipedia-mcp-server.git
cd wikipedia-mcp-server && uv sync
```

## Usage

### Claude Desktop Configuration
```json
{
  "mcpServers": {
    "wikipedia": {
      "command": "uvx", 
      "args": ["--from", "git+https://github.com/yourusername/wikipedia-mcp-server", "wikipedia-mcp-server"]
    }
  }
}
```

### Testing
```bash
uv run python test_server.py  # 31 tests, 100% pass rate
```

## Example Usage

**Search:**
```json
{"tool": "search_wikipedia", "arguments": {"query": "AI"}}
```

**Get Article:**
```json  
{"tool": "get_article", "arguments": {"title": "Python (programming language)"}}
```

**Extract Facts:**
```json
{"tool": "extract_key_facts", "arguments": {"title": "Marie Curie", "topic_within_article": "Nobel Prize"}}
```

## 🎯 Parameter and Type Handling Rules

This server follows specific design patterns for handling parameters and data types to ensure consistency and predictability.

### Input Parameter Design

**Schema Pattern**: All input parameters are marked as `required` in JSON schemas
```json
{
  "required": ["title", "query", "max_length"]
}
```

**Handler Pattern**: Functions can have optional parameters with defaults
```python
async def summarize_article_for_query(
    title: str, 
    query: str, 
    max_length: int = 250  # Default provided in handler
) -> Dict[str, Any]:
```

**Benefits**:
- **Clear Client Expectations**: MCP clients must provide all documented parameters
- **Implementation Flexibility**: Handlers can use sensible defaults when appropriate
- **Future Extensibility**: Schema can be expanded without breaking existing implementations

### Output Type Design

**Nullable Fields**: Use `["type", "null"]` only when data genuinely might not exist
```json
{
  "coordinates": { "type": ["array", "null"] },  // May not exist for non-geographic articles
  "pageid": { "type": ["number", "null"] },      // May be null if article doesn't exist
  "error": { "type": ["string", "null"] }        // Null on success, string on error
}
```

**Non-Nullable Collections**: Always return empty arrays instead of null
```json
{
  "links": { "type": "array" },     // Returns [] if no links found
  "facts": { "type": "array" },     // Returns [] if no facts extracted
  "sections": { "type": "array" }   // Returns [] if no sections found
}
```

**Non-Nullable Strings**: Always return empty strings instead of null  
```json
{
  "summary": { "type": "string" },  // Returns "" if no summary available
  "text": { "type": "string" },      // Returns "" if no content available
  "title": { "type": "string" }     // Always present, never null
}
```

### Design Principles

1. **Semantic Nullability**: Only use null when it represents "this data doesn't exist" rather than "this data is empty"
2. **Predictable Types**: Arrays are always arrays, strings are always strings (unless explicitly nullable)
3. **Client Safety**: Clients can safely iterate arrays and concatenate strings without null checks
4. **Clear Intent**: Nullable fields have explicit semantic meaning (coordinates for non-places, errors on success, etc.)

### Examples

**Geographic Data** (nullable when appropriate):
```json
{
  "title": "Programming",           // Always string
  "coordinates": null,              // Null - programming isn't a place
  "pageid": 12345,                 // Number when article exists
  "error": null                    // Null on success
}
```

**Content Collections** (empty when no data):
```json
{
  "title": "Stub Article",         // Always string  
  "links": [],                     // Empty array - no links found
  "facts": [],                     // Empty array - no facts extracted
  "summary": ""                    // Empty string - no summary available
}
```

This design ensures type safety, predictable behavior, and clear semantic meaning across all tools.

## Development

**Dependencies**: `mcp>=1.6.0`, `wikipedia-api>=0.6.0`, `requests>=2.31.0`, `jsonschema>=4.0.0`

```bash
# Local development
git clone repo && cd wikipedia-mcp-server
uv sync && uv run python test_server.py
```

---
**Production-ready** Wikipedia MCP server with 100% test coverage.