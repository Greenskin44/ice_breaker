"""
Ice Breaker - AI-Powered Conversation Starter Generator

This module orchestrates the main functionality of the Ice Breaker application.
It coordinates multiple AI agents to gather information from LinkedIn and Twitter/X,
then uses LangChain and OpenAI to generate personalized conversation starters.

Author: Based on original work by Eden Marco (@emarco177)
Course: LangChain Udemy Course by Eden Marco
"""

from typing import Tuple
from dotenv import load_dotenv

from langchain_core.prompts import PromptTemplate
from langchain_openai import ChatOpenAI

from output_parsers import summary_parser, Summary
from third_parties.linkedin import scrape_linkedin_profile
from agents.linkedin_lookup_agent import lookup as linkedin_lookup_agent
from agents.twitter_lookup_agent import lookup as twitter_lookup_agent
from third_parties.twitter import scrape_user_tweets


def ice_break_with(name: str) -> Tuple[Summary, str]:
    """
    Generate personalized ice breakers for a given person using AI and RAG.
    
    This function orchestrates the entire ice breaker generation process:
    1. Uses LinkedIn agent to find the person's LinkedIn profile
    2. Scrapes LinkedIn profile information
    3. Uses Twitter agent to find the person's Twitter/X profile  
    4. Scrapes recent tweets
    5. Combines all information using LangChain and OpenAI to generate insights
    
    Args:
        name (str): Full name of the person to generate ice breakers for
        
    Returns:
        Tuple[Summary, str]: A tuple containing:
            - Summary object with generated summary and interesting facts
            - Profile picture URL from LinkedIn
            
    Example:
        >>> summary, pic_url = ice_break_with("John Doe")
        >>> print(summary.summary)
        >>> print(summary.facts)
    """
    # Use LinkedIn agent to find profile URL
    linkedin_username = linkedin_lookup_agent(name=name)
    linkedin_data = scrape_linkedin_profile(linkedin_profile_url=linkedin_username)

    # Use Twitter agent to find username and scrape tweets
    twitter_username = twitter_lookup_agent(name=name)
    tweets = scrape_user_tweets(username=twitter_username)

    # Create prompt template for LLM
    summary_template = """
    Given the information about a person from LinkedIn {information}, 
    and their latest Twitter posts {twitter_posts},
    I want you to create:
    1. A short summary about the person
    2. Two interesting facts about them that could serve as conversation starters

    Use both information from Twitter and LinkedIn to provide comprehensive insights.
    Focus on professional achievements, interests, and recent activities that would 
    be appropriate for networking conversations.

    {format_instructions}
    """
    
    summary_prompt_template = PromptTemplate(
        input_variables=['information', 'twitter_posts'],
        template=summary_template,
        partial_variables={
            "format_instructions": summary_parser.get_format_instructions()
        },
    )

    # Initialize LLM with appropriate parameters
    llm = ChatOpenAI(temperature=0, model_name='gpt-4o-mini')

    # Create LangChain processing chain
    chain = summary_prompt_template | llm | summary_parser

    # Process the information and generate insights
    res: Summary = chain.invoke({
        "information": linkedin_data,
        "twitter_posts": tweets
    })

    return res, linkedin_data.get("PhotoUrl")


if __name__ == "__main__":
    load_dotenv()
    
    print("Ice Breaker Application - Testing Mode")
    print("=" * 50)
    
    # Test the application with Eden Marco's profile
    try:
        summary, profile_pic = ice_break_with(name="Eden Marco")
        print(f"Summary: {summary.summary}")
        print(f"Facts: {summary.facts}")
        print(f"Profile Picture URL: {profile_pic}")
    except Exception as e:
        print(f"Error during testing: {str(e)}")
        print("Please ensure all API keys are properly configured in your .env file")





