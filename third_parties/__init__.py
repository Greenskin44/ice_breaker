"""
Third Party Integrations Package

This package contains integrations with external APIs and services
for collecting profile and social media data.

Author: Based on original work by Eden Marco (@emarco177)
Course: LangChain Udemy Course by Eden Marco
"""

from .linkedin import scrape_linkedin_profile
from .twitter import scrape_user_tweets, scrape_user_tweets_mock

__all__ = ["scrape_linkedin_profile", "scrape_user_tweets", "scrape_user_tweets_mock"]