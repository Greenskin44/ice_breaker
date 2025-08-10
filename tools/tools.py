"""
Tools for Ice Breaker Application

This module provides utility tools for web searches and profile lookups.
It integrates with Tavily Search API to perform targeted searches for
LinkedIn and Twitter/X profiles.

Author: Based on original work by Eden Marco (@emarco177)
Course: LangChain Udemy Course by Eden Marco
"""

from langchain_community.tools.tavily_search import TavilySearchResults


def get_profile_url_tavily(name: str) -> str:
    """
    Search for LinkedIn or Twitter profile pages using Tavily search API.
    
    This function performs a web search to find social media profiles
    for a given person's name. It's designed to work with AI agents
    that need to discover profile URLs for further processing.
    
    Args:
        name (str): Full name of the person to search for
        
    Returns:
        str: Search results containing relevant profile information
        
    Example:
        >>> results = get_profile_url_tavily("John Doe")
        >>> print(results)  # Returns search results with potential profile links
        
    Note:
        This function requires a valid Tavily API key to be set in
        the environment variables as TAVILY_API_KEY.
    """
    try:
        # Initialize Tavily search with default parameters
        search = TavilySearchResults(
            max_results=5,  # Limit results to most relevant matches
            search_depth="basic",  # Use basic search depth for faster results
            include_answer=True,  # Include AI-generated answer
            include_raw_content=False,  # Exclude raw HTML content
            include_images=False  # Don't include images in search results
        )
        
        # Perform search with enhanced query for better profile discovery
        enhanced_query = f"{name} LinkedIn Twitter X social media profile"
        results = search.run(enhanced_query)
        
        return results
        
    except Exception as e:
        # Return error information for debugging
        return f"Error during search: {str(e)}. Please check your Tavily API key configuration."


if __name__ == "__main__":
    """
    Test the profile search functionality.
    """
    print("Testing Profile URL Search Tool")
    print("=" * 40)
    
    try:
        # Test with a sample name
        test_name = "Eden Marco"
        print(f"Searching for profiles of: {test_name}")
        
        results = get_profile_url_tavily(test_name)
        print(f"Search results:\n{results}")
        
    except Exception as e:
        print(f"Error during test: {str(e)}")
        print("Please ensure Tavily API key is properly configured.")