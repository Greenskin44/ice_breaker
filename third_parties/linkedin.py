"""
LinkedIn Profile Scraper

This module provides functionality to scrape LinkedIn profile information
using the Scrapin.io API. It supports both live data extraction and mock
data for testing purposes.

Author: Based on original work by Eden Marco (@emarco177)
Course: LangChain Udemy Course by Eden Marco
"""

import os
import requests
from dotenv import load_dotenv
from typing import Dict, Any, Optional
import logging

load_dotenv()

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


def scrape_linkedin_profile(
    linkedin_profile_url: str, 
    mock: bool = False,
    timeout: int = 10
) -> Dict[str, Any]:
    """
    Scrape information from LinkedIn profiles using Scrapin.io API.
    
    This function extracts professional information from LinkedIn profiles
    including work experience, education, skills, and other relevant data
    that can be used for generating conversation starters.
    
    Args:
        linkedin_profile_url (str): The LinkedIn profile URL to scrape
        mock (bool, optional): If True, uses mock data instead of live API. 
                              Defaults to False.
        timeout (int, optional): Request timeout in seconds. Defaults to 10.
        
    Returns:
        Dict[str, Any]: Dictionary containing profile information with cleaned data
        
    Example:
        >>> profile_data = scrape_linkedin_profile(
        ...     "https://www.linkedin.com/in/eden-marco/"
        ... )
        >>> print(profile_data.get("fullName"))
        
    Raises:
        requests.RequestException: If the API request fails
        KeyError: If the response format is unexpected
    """
    try:
        if mock:
            # Use pre-made mock data for testing
            logger.info("Using mock LinkedIn data for testing")
            mock_data_url = (
                "https://gist.githubusercontent.com/emarco177/"
                "859ec7d786b45d8e3e3f688c6c9139d8/raw/"
                "32f3c85b9513994c572613f2c8b376b633bfc43f/eden-marco-scrapin.json"
            )
            response = requests.get(mock_data_url, timeout=timeout)
            
        else:
            # Use live Scrapin.io API
            api_endpoint = "https://api.scrapin.io/enrichment/profile"
            api_key = os.environ.get("SCRAPIN_API_KEY")
            
            if not api_key:
                logger.warning("SCRAPIN_API_KEY not found, falling back to mock data")
                return scrape_linkedin_profile(linkedin_profile_url, mock=True, timeout=timeout)
            
            params = {
                "apikey": api_key,
                "linkedInUrl": linkedin_profile_url,
            }
            
            logger.info(f"Scraping LinkedIn profile: {linkedin_profile_url}")
            response = requests.get(api_endpoint, params=params, timeout=timeout)
        
        # Check if request was successful
        response.raise_for_status()
        
        # Parse JSON response
        json_data = response.json()
        person_data = json_data.get("person", {})
        
        # Clean and filter the data
        cleaned_data = clean_profile_data(person_data)
        
        logger.info("Successfully scraped LinkedIn profile data")
        return cleaned_data
        
    except requests.exceptions.RequestException as e:
        logger.error(f"Request failed: {str(e)}")
        if not mock:
            logger.info("Falling back to mock data due to API error")
            return scrape_linkedin_profile(linkedin_profile_url, mock=True, timeout=timeout)
        raise
        
    except Exception as e:
        logger.error(f"Unexpected error: {str(e)}")
        raise


def clean_profile_data(data: Dict[str, Any]) -> Dict[str, Any]:
    """
    Clean and filter profile data by removing empty values and unwanted fields.
    
    Args:
        data (Dict[str, Any]): Raw profile data from API
        
    Returns:
        Dict[str, Any]: Cleaned profile data with empty values removed
    """
    # Fields to exclude from the cleaned data
    excluded_fields = ["certifications"]
    
    # Values considered as empty
    empty_values = [[], "", None]
    
    cleaned_data = {
        key: value
        for key, value in data.items()
        if value not in empty_values and key not in excluded_fields
    }
    
    return cleaned_data


if __name__ == "__main__":
    """
    Test the LinkedIn scraping functionality.
    """
    print("Testing LinkedIn Profile Scraper")
    print("=" * 50)
    
    try:
        # Test with Eden Marco's profile using mock data
        test_url = "https://www.linkedin.com/in/eden-marco/"
        
        print("Testing with mock data...")
        mock_profile = scrape_linkedin_profile(test_url, mock=True)
        print(f"Mock profile data keys: {list(mock_profile.keys())}")
        
        # Uncomment the following lines to test with live API
        # print("\nTesting with live API...")
        # live_profile = scrape_linkedin_profile(test_url, mock=False)
        # print(f"Live profile data keys: {list(live_profile.keys())}")
        
    except Exception as e:
        print(f"Error during test: {str(e)}")
        print("Please ensure API keys are properly configured.")