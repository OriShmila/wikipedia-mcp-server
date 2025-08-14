"""
Wikipedia MCP server tool handlers.

All tool functions that implement the Wikipedia MCP server functionality.
"""

import logging
from typing import Dict, Any

from .wikipedia_client import WikipediaClient

logger = logging.getLogger(__name__)

# Initialize Wikipedia client with default settings
wikipedia_client = WikipediaClient(language="en", enable_cache=True)


async def search_wikipedia(query: str, limit: int = 10) -> Dict[str, Any]:
    """Search Wikipedia for articles matching a query."""
    if not query:
        raise ValueError("query is required")

    if limit < 1 or limit > 50:
        raise ValueError("limit must be between 1 and 50")

    try:
        logger.info(f"Searching Wikipedia for: {query}")
        results = wikipedia_client.search(query, limit=limit)
        return {"query": query, "results": results}
    except Exception as e:
        logger.error(f"Error searching Wikipedia: {e}")
        raise ValueError(f"Search error: {str(e)}")


async def get_article(title: str) -> Dict[str, Any]:
    """Get the full content of a Wikipedia article."""
    if not title:
        raise ValueError("title is required")

    try:
        logger.info(f"Getting article: {title}")
        article = wikipedia_client.get_article(title)
        return article
    except Exception as e:
        logger.error(f"Error getting Wikipedia article: {e}")
        raise ValueError(f"Article error: {str(e)}")


async def get_summary(title: str) -> Dict[str, Any]:
    """Get a summary of a Wikipedia article."""
    if not title:
        raise ValueError("title is required")

    try:
        logger.info(f"Getting summary for: {title}")
        summary = wikipedia_client.get_summary(title)
        return {"title": title, "summary": summary}
    except Exception as e:
        logger.error(f"Error getting Wikipedia summary: {e}")
        raise ValueError(f"Summary error: {str(e)}")


async def summarize_article_for_query(
    title: str, query: str, max_length: int = 250
) -> Dict[str, Any]:
    """Get a summary of a Wikipedia article tailored to a specific query."""
    if not title:
        raise ValueError("title is required")

    if not query:
        raise ValueError("query is required")

    if max_length < 50 or max_length > 1000:
        raise ValueError("max_length must be between 50 and 1000")

    try:
        logger.info(
            f"Getting query-focused summary for article: {title}, query: {query}"
        )
        summary = wikipedia_client.summarize_for_query(
            title, query, max_length=max_length
        )
        return {"title": title, "query": query, "summary": summary}
    except Exception as e:
        logger.error(f"Error getting query-focused summary: {e}")
        raise ValueError(f"Query summary error: {str(e)}")


async def summarize_article_section(
    title: str, section_title: str, max_length: int = 150
) -> Dict[str, Any]:
    """Get a summary of a specific section of a Wikipedia article."""
    if not title:
        raise ValueError("title is required")

    if not section_title:
        raise ValueError("section_title is required")

    if max_length < 50 or max_length > 500:
        raise ValueError("max_length must be between 50 and 500")

    try:
        logger.info(f"Getting summary for section: {section_title} in article: {title}")
        summary = wikipedia_client.summarize_section(
            title, section_title, max_length=max_length
        )
        return {"title": title, "section_title": section_title, "summary": summary}
    except Exception as e:
        logger.error(f"Error getting section summary: {e}")
        raise ValueError(f"Section summary error: {str(e)}")


async def extract_key_facts(
    title: str, topic_within_article: str = "", count: int = 5
) -> Dict[str, Any]:
    """Extract key facts from a Wikipedia article, optionally focused on a topic."""
    if not title:
        raise ValueError("title is required")

    if count < 1 or count > 20:
        raise ValueError("count must be between 1 and 20")

    try:
        logger.info(
            f"Extracting key facts for article: {title}, topic: {topic_within_article}"
        )
        # Convert empty string to None for backward compatibility
        topic = topic_within_article if topic_within_article.strip() else None
        facts = wikipedia_client.extract_facts(title, topic, count=count)
        return {
            "title": title,
            "topic_within_article": topic_within_article,
            "facts": facts,
        }
    except Exception as e:
        logger.error(f"Error extracting key facts: {e}")
        raise ValueError(f"Fact extraction error: {str(e)}")


async def get_related_topics(title: str, limit: int = 10) -> Dict[str, Any]:
    """Get topics related to a Wikipedia article based on links and categories."""
    if not title:
        raise ValueError("title is required")

    if limit < 1 or limit > 50:
        raise ValueError("limit must be between 1 and 50")

    try:
        logger.info(f"Getting related topics for: {title}")
        related = wikipedia_client.get_related_topics(title, limit=limit)
        return {"title": title, "related_topics": related}
    except Exception as e:
        logger.error(f"Error getting related topics: {e}")
        raise ValueError(f"Related topics error: {str(e)}")


async def get_sections(title: str) -> Dict[str, Any]:
    """Get the sections of a Wikipedia article."""
    if not title:
        raise ValueError("title is required")

    try:
        logger.info(f"Getting sections for: {title}")
        sections = wikipedia_client.get_sections(title)
        return {"title": title, "sections": sections}
    except Exception as e:
        logger.error(f"Error getting sections: {e}")
        raise ValueError(f"Sections error: {str(e)}")


async def get_links(title: str) -> Dict[str, Any]:
    """Get the links contained within a Wikipedia article."""
    if not title:
        raise ValueError("title is required")

    try:
        logger.info(f"Getting links for: {title}")
        links = wikipedia_client.get_links(title)
        return {"title": title, "links": links}
    except Exception as e:
        logger.error(f"Error getting links: {e}")
        raise ValueError(f"Links error: {str(e)}")


async def get_coordinates(title: str) -> Dict[str, Any]:
    """Get the coordinates of a Wikipedia article."""
    if not title:
        raise ValueError("title is required")

    try:
        logger.info(f"Getting coordinates for: {title}")
        coordinates = wikipedia_client.get_coordinates(title)
        return coordinates
    except Exception as e:
        logger.error(f"Error getting coordinates: {e}")
        raise ValueError(f"Coordinates error: {str(e)}")


# Tool functions mapping
TOOL_FUNCTIONS = {
    "search_wikipedia": search_wikipedia,
    "get_article": get_article,
    "get_summary": get_summary,
    "summarize_article_for_query": summarize_article_for_query,
    "summarize_article_section": summarize_article_section,
    "extract_key_facts": extract_key_facts,
    "get_related_topics": get_related_topics,
    "get_sections": get_sections,
    "get_links": get_links,
    "get_coordinates": get_coordinates,
}
