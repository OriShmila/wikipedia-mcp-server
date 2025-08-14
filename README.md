# Wikipedia MCP Server

A comprehensive Model Context Protocol (MCP) server that provides access to Wikipedia content through 10 powerful tools. Built with Python, featuring complete schema validation, comprehensive testing, and robust error handling.

## 🎯 Overview

This MCP server enables seamless interaction with Wikipedia through a standardized protocol. It provides tools for searching, retrieving, summarizing, and analyzing Wikipedia content with built-in validation and error handling.

### Key Features

- **10 Wikipedia Tools** - Comprehensive coverage of Wikipedia functionality
- **100% Test Coverage** - 31 test cases with full validation
- **Schema Validation** - Complete input/output validation using JSON Schema
- **Multi-language Support** - Access Wikipedia in different languages
- **Geographic Data** - Retrieve coordinates and location information
- **Content Analysis** - Extract facts, summaries, and related topics
- **Robust Error Handling** - Graceful handling of edge cases and API errors
- **Performance Optimized** - Optional caching and efficient API usage

## 🛠️ Available Tools

| Tool | Description | Use Cases |
|------|-------------|-----------|
| `search_wikipedia` | Search for articles matching a query | Find relevant articles, explore topics |
| `get_article` | Get complete article content | Full text access, detailed research |
| `get_summary` | Get article summary | Quick overviews, brief information |
| `summarize_article_for_query` | Get query-focused summary | Targeted information extraction |
| `summarize_article_section` | Summarize specific sections | Focus on particular aspects |
| `extract_key_facts` | Extract key facts from articles | Bullet points, important details |
| `get_related_topics` | Find related articles and categories | Discover connected content |
| `get_sections` | Get article structure and sections | Navigation, content organization |
| `get_links` | Get all links within an article | Reference discovery, link analysis |
| `get_coordinates` | Get geographic coordinates | Location data, mapping |

## 🚀 Quick Start

### Installation

#### Option 1: Direct Installation with uvx
```bash
uvx --from git+https://github.com/yourusername/wikipedia-mcp-server wikipedia-mcp-server
```

#### Option 2: Local Development
```bash
git clone https://github.com/yourusername/wikipedia-mcp-server.git
cd wikipedia-mcp-server
uv sync
```

### Testing the Server
```bash
# Run comprehensive test suite
uv run python test_server.py

# Expected output: 31 test cases, 100% pass rate
```

### Using with MCP Clients

#### Claude Desktop Configuration
Add to your Claude Desktop configuration:

```json
{
  "mcpServers": {
    "wikipedia": {
      "command": "uvx",
      "args": [
        "--from",
        "git+https://github.com/yourusername/wikipedia-mcp-server",
        "wikipedia-mcp-server"
      ]
    }
  }
}
```

#### Other MCP Clients
The server works with any MCP-compatible client using JSON-RPC 2.0 over stdio.

## 📖 Tool Documentation

### 1. Search Wikipedia
Search for articles matching a query.

**Input:**
- `query` (string, required): Search terms
- `limit` (integer, 1-50, default: 10): Maximum results

**Example:**
```json
{
  "tool": "search_wikipedia",
  "arguments": {
    "query": "artificial intelligence",
    "limit": 5
  }
}
```

**Output:**
```json
{
  "query": "artificial intelligence",
  "results": [
    {
      "title": "Artificial intelligence",
      "snippet": "Artificial intelligence (AI) is intelligence demonstrated by machines...",
      "pageid": 1645,
      "wordcount": 15420,
      "timestamp": "2024-01-15T10:30:00Z"
    }
  ]
}
```

### 2. Get Article
Retrieve complete article content.

**Input:**
- `title` (string, required): Article title

**Example:**
```json
{
  "tool": "get_article",
  "arguments": {
    "title": "Python (programming language)"
  }
}
```

**Output:**
```json
{
  "title": "Python (programming language)",
  "pageid": 23862,
  "summary": "Python is a high-level programming language...",
  "text": "Full article text...",
  "url": "https://en.wikipedia.org/wiki/Python_(programming_language)",
  "sections": [...],
  "categories": [...],
  "links": [...],
  "exists": true
}
```

### 3. Get Summary
Get a brief summary of an article.

**Input:**
- `title` (string, required): Article title

**Example:**
```json
{
  "tool": "get_summary",
  "arguments": {
    "title": "Albert Einstein"
  }
}
```

### 4. Query-Focused Summary
Get a summary focused on a specific query.

**Input:**
- `title` (string, required): Article title
- `query` (string, required): Focus query
- `max_length` (integer, 50-1000, default: 250): Maximum length

**Example:**
```json
{
  "tool": "summarize_article_for_query",
  "arguments": {
    "title": "Albert Einstein",
    "query": "relativity theory",
    "max_length": 200
  }
}
```

### 5. Section Summary
Summarize a specific article section.

**Input:**
- `title` (string, required): Article title
- `section_title` (string, required): Section name
- `max_length` (integer, 50-500, default: 150): Maximum length

### 6. Extract Key Facts
Extract key facts from an article.

**Input:**
- `title` (string, required): Article title
- `topic_within_article` (string, optional): Focus topic
- `count` (integer, 1-20, default: 5): Number of facts

**Example:**
```json
{
  "tool": "extract_key_facts",
  "arguments": {
    "title": "Marie Curie",
    "topic_within_article": "Nobel Prize",
    "count": 3
  }
}
```

### 7. Get Related Topics
Find topics related to an article.

**Input:**
- `title` (string, required): Article title
- `limit` (integer, 1-50, default: 10): Maximum results

### 8. Get Sections
Retrieve article section structure.

**Input:**
- `title` (string, required): Article title

**Output:**
```json
{
  "title": "Article Title",
  "sections": [
    {
      "title": "Introduction",
      "level": 0,
      "text": "Section content...",
      "sections": [...]
    }
  ]
}
```

### 9. Get Links
Get all links within an article.

**Input:**
- `title` (string, required): Article title

### 10. Get Coordinates
Retrieve geographic coordinates.

**Input:**
- `title` (string, required): Article title

**Example Output:**
```json
{
  "title": "Paris",
  "pageid": 22989,
  "coordinates": [
    {
      "latitude": 48.8566667,
      "longitude": 2.3522222,
      "primary": true,
      "globe": "earth"
    }
  ],
  "exists": true
}
```

## 🔧 Advanced Usage

### Multi-language Support
The server supports different Wikipedia language editions:

```python
# Initialize with different language
client = WikipediaClient(language="fr")  # French Wikipedia
client = WikipediaClient(language="de")  # German Wikipedia
```

### Country-based Language Selection
Automatically select language based on country:

```python
client = WikipediaClient(country="CN")  # Chinese Wikipedia
client = WikipediaClient(country="JP")  # Japanese Wikipedia
```

### Performance Optimization
Enable caching for improved performance:

```python
client = WikipediaClient(enable_cache=True)
```

## 🧪 Testing

### Running Tests
```bash
# Run complete test suite
uv run python test_server.py

# Sample output:
# Total Tests: 31
# ✅ Passed: 31
# ❌ Failed: 0
# 📊 Success Rate: 100.0%
```

### Test Categories
- **Input Validation** - Parameter requirement and constraint testing
- **Output Validation** - Schema compliance verification
- **Error Handling** - Invalid input and edge case testing
- **Integration** - Real Wikipedia API interaction testing
- **Performance** - Response time monitoring

### Adding Custom Tests
Add test cases to `test_cases.json`:

```json
{
  "test_cases": [
    {
      "name": "test_custom_case",
      "tool": "search_wikipedia",
      "arguments": {
        "query": "test query"
      },
      "description": "Custom test description",
      "expected_fields": ["query", "results"],
      "should_succeed": true
    }
  ]
}
```

## 🛡️ Error Handling

The server provides comprehensive error handling:

### Input Validation Errors
```json
{
  "error": "ValueError: title is required"
}
```

### API Errors
```json
{
  "error": "Article error: Page does not exist"
}
```

### Parameter Constraint Errors
```json
{
  "error": "ValueError: limit must be between 1 and 50"
}
```

## 📊 Schema Validation

All tools use JSON Schema for validation:

### Input Schema Example
```json
{
  "type": "object",
  "properties": {
    "title": {
      "type": "string",
      "description": "Wikipedia article title"
    },
    "limit": {
      "type": "integer",
      "minimum": 1,
      "maximum": 50,
      "default": 10
    }
  },
  "required": ["title"]
}
```

### Output Schema Example
```json
{
  "type": "object",
  "properties": {
    "title": { "type": "string" },
    "exists": { "type": "boolean" },
    "data": { "type": ["object", "null"] }
  }
}
```

## 🔨 Development

### Project Structure
```
wikipedia-mcp-server/
├── wikipedia_mcp_server/       # Main package
│   ├── __init__.py            # Package initialization
│   ├── __main__.py            # Entry point
│   ├── server.py              # MCP server implementation
│   ├── handlers.py            # Tool implementations
│   ├── tools.json             # Tool schemas
│   └── wikipedia_client.py    # Wikipedia API client
├── main.py                    # Testing wrapper
├── test_server.py             # Test framework
├── test_cases.json           # Test definitions
├── pyproject.toml            # Project configuration
└── README.md                 # This file
```

### Dependencies
- `mcp>=1.6.0` - MCP protocol support
- `wikipedia-api>=0.6.0` - Wikipedia API client
- `requests>=2.31.0` - HTTP client
- `jsonschema>=4.0.0` - Schema validation

### Local Development
```bash
# Install dependencies
uv sync

# Run in development mode
uv run python main.py

# Run tests
uv run python test_server.py

# Build package
uv build
```

## 📚 Use Cases

### Research and Education
- **Academic Research** - Gather comprehensive information on topics
- **Student Projects** - Quick access to reliable information
- **Fact Checking** - Verify information against Wikipedia sources

### Content Creation
- **Article Writing** - Research topics and gather facts
- **Content Summarization** - Create concise summaries
- **Topic Exploration** - Discover related topics and connections

### Data Analysis
- **Knowledge Graphs** - Build connections between topics
- **Geographic Analysis** - Extract location data
- **Link Analysis** - Study article relationships

### AI and Automation
- **Knowledge Retrieval** - Integrate with AI assistants
- **Automated Research** - Programmatic information gathering
- **Content Enrichment** - Enhance applications with Wikipedia data

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch
3. Add comprehensive tests
4. Ensure 100% test pass rate
5. Update documentation
6. Submit a pull request

## 📄 License

This project is licensed under the MIT License - see the LICENSE file for details.

## 🔗 Resources

- [MCP Specification](https://github.com/modelcontextprotocol)
- [Wikipedia API Documentation](https://www.mediawiki.org/wiki/API:Main_page)
- [JSON Schema](https://json-schema.org/)
- [UV Package Manager](https://github.com/astral-sh/uv)

## 🎯 Roadmap

- [ ] Additional language support
- [ ] Enhanced caching mechanisms  
- [ ] Rate limiting configuration
- [ ] Wikipedia edit history access
- [ ] Image and media retrieval
- [ ] Custom search filters
- [ ] Batch operations
- [ ] Performance metrics

---

**Ready to use:** This Wikipedia MCP server is production-ready with comprehensive testing, validation, and error handling. Perfect for integration with MCP clients like Claude Desktop.