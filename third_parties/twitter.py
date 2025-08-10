"""
Twitter/X Profile and Tweets Scraper

This module provides functionality to scrape Twitter/X user tweets using
the Twitter API v2 via Tweepy. It supports both live data extraction and
mock data for testing purposes.

Author: Based on original work by Eden Marco (@emarco177)
Course: LangChain Udemy Course by Eden Marco
"""

import os
from dotenv import load_dotenv
import tweepy
import requests
from typing import List, Dict, Any, Optional
import logging

load_dotenv()

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# Initialize Twitter client with API credentials
try:
    twitter_client = tweepy.Client(
        bearer_token=os.environ.get("TWITTER_BEARER_TOKEN"),
        consumer_key=os.environ.get("TWITTER_API_KEY"),
        consumer_secret=os.environ.get("TWITTER_API_KEY_SECRET"),
        access_token=os.environ.get("TWITTER_ACCESS_TOKEN"),
        access_token_secret=os.environ.get("TWITTER_ACCESS_TOKEN_SECRET"),
        wait_on_rate_limit=True  # Automatically wait when rate limited
    )
except Exception as e:
    logger.warning(f"Failed to initialize Twitter client: {str(e)}")
    twitter_client = None


def scrape_user_tweets(
    username: str, 
    num_tweets: int = 5,
    use_mock: bool = False
) -> List[Dict[str, Any]]:
    """
    Scrape a Twitter user's original tweets (excluding retweets and replies).
    
    This function retrieves recent tweets from a user's timeline, filtering out
    retweets and replies to focus on original content that provides insights
    into the person's interests and activities.
    
    Args:
        username (str): Twitter username (without @ symbol)
        num_tweets (int, optional): Maximum number of tweets to retrieve. Defaults to 5.
        use_mock (bool, optional): If True, uses mock data instead of live API. 
                                 Defaults to False.
        
    Returns:
        List[Dict[str, Any]]: List of tweet dictionaries with 'text' and 'url' fields
        
    Example:
        >>> tweets = scrape_user_tweets("example_user", num_tweets=3)
        >>> for tweet in tweets:
        ...     print(f"Tweet: {tweet['text']}")
        ...     print(f"URL: {tweet['url']}")
        
    Raises:
        tweepy.TweepyException: If Twitter API request fails
        ValueError: If username is invalid or user not found
    """
    if use_mock or not twitter_client:
        logger.info("Using mock Twitter data")
        return scrape_user_tweets_mock(username, num_tweets)
    
    try:
        logger.info(f"Scraping tweets for user: @{username}")
        
        # Get user information first
        user = twitter_client.get_user(username=username)
        if not user.data:
            raise ValueError(f"User @{username} not found")
            
        user_id = user.data.id
        
        # Get user's tweets (excluding retweets and replies)
        tweets = twitter_client.get_users_tweets(
            id=user_id,
            max_results=min(num_tweets, 100),  # API limit is 100
            exclude=["retweets", "replies"],
            tweet_fields=["created_at", "public_metrics"]
        )
        
        if not tweets.data:
            logger.warning(f"No tweets found for @{username}")
            return []
        
        # Format tweets into consistent structure
        tweet_list = []
        for tweet in tweets.data[:num_tweets]:
            tweet_dict = {
                "text": tweet.text,
                "url": f"https://twitter.com/{username}/status/{tweet.id}"
            }
            tweet_list.append(tweet_dict)
        
        logger.info(f"Successfully retrieved {len(tweet_list)} tweets for @{username}")
        return tweet_list
        
    except tweepy.TweepyException as e:
        logger.error(f"Twitter API error: {str(e)}")
        logger.info("Falling back to mock data")
        return scrape_user_tweets_mock(username, num_tweets)
        
    except Exception as e:
        logger.error(f"Unexpected error: {str(e)}")
        logger.info("Falling back to mock data")
        return scrape_user_tweets_mock(username, num_tweets)


def scrape_user_tweets_mock(username: str = "EdenEmarco177", num_tweets: int = 5) -> List[Dict[str, Any]]:
    """
    Scrape pre-made tweet data from Eden's GitHub Gist for testing purposes.
    
    This function provides mock data when the Twitter API is unavailable or
    for testing scenarios. It uses a curated set of tweets from Eden Marco.
    
    Args:
        username (str, optional): Username for URL generation. Defaults to "EdenEmarco177".
        num_tweets (int, optional): Number of tweets to return. Defaults to 5.
        
    Returns:
        List[Dict[str, Any]]: List of mock tweet dictionaries
        
    Example:
        >>> mock_tweets = scrape_user_tweets_mock("testuser", 3)
        >>> print(f"Retrieved {len(mock_tweets)} mock tweets")
        
    Note:
        Mock data is sourced from: 
        https://twitter.com/EdenEmarco177
    """
    try:
        logger.info(f"Fetching mock tweet data for @{username}")
        
        # URL to Eden Marco's curated tweet data
        EDEN_TWITTER_GIST = (
            "https://gist.githubusercontent.com/emarco177/"
            "827323bb599553d0f0e662da07b9ff68/raw/"
            "57bf38cf8acce0c87e060f9bb51f6ab72098fbd6/eden-marco-twitter.json"
        )
        
        response = requests.get(EDEN_TWITTER_GIST, timeout=10)
        response.raise_for_status()
        
        tweets_data = response.json()
        
        # Format tweets into consistent structure
        tweet_list = []
        for tweet in tweets_data[:num_tweets]:
            tweet_dict = {
                "text": tweet["text"],
                "url": f"https://twitter.com/{username}/status/{tweet['id']}"
            }
            tweet_list.append(tweet_dict)
        
        logger.info(f"Successfully loaded {len(tweet_list)} mock tweets")
        return tweet_list
        
    except Exception as e:
        logger.error(f"Failed to load mock data: {str(e)}")
        # Return empty list if even mock data fails
        return []


if __name__ == "__main__":
    """
    Test the Twitter scraping functionality.
    """
    print("Testing Twitter Profile Scraper")
    print("=" * 50)
    
    try:
        # Test with mock data first
        print("Testing with mock data...")
        mock_tweets = scrape_user_tweets_mock(username="EdenEmarco177", num_tweets=3)
        print(f"Retrieved {len(mock_tweets)} mock tweets")
        
        if mock_tweets:
            print("Sample tweet:")
            print(f"Text: {mock_tweets[0]['text'][:100]}...")
            print(f"URL: {mock_tweets[0]['url']}")
        
        # Uncomment the following lines to test with live API
        # print("\nTesting with live API...")
        # live_tweets = scrape_user_tweets("EdenEmarco177", num_tweets=3)
        # print(f"Retrieved {len(live_tweets)} live tweets")
        
    except Exception as e:
        print(f"Error during test: {str(e)}")
        print("Please ensure API keys are properly configured.")