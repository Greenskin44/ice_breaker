"""
AI Agents Package

This package contains specialized AI agents for data collection and processing.
Each agent focuses on a specific data source and uses LangChain's ReAct framework
for intelligent search and reasoning.

Author: Based on original work by Eden Marco (@emarco177)
Course: LangChain Udemy Course by Eden Marco
"""

from .linkedin_lookup_agent import lookup as linkedin_lookup
from .twitter_lookup_agent import lookup as twitter_lookup

__all__ = ["linkedin_lookup", "twitter_lookup"]