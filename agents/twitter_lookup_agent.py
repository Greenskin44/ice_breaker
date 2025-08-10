"""
Twitter/X Lookup Agent

This module implements an AI agent that searches for Twitter/X profile URLs
and extracts usernames. The agent uses LangChain's ReAct framework to find
and process Twitter profile information for social media analysis.

Author: Based on original work by Eden Marco (@emarco177)
Course: LangChain Udemy Course by Eden Marco
"""

from langchain_core.prompts import PromptTemplate
from langchain_core.tools import Tool
from langchain_openai import ChatOpenAI
from langchain import hub
from langchain.agents import create_react_agent, AgentExecutor

from dotenv import load_dotenv
from tools.tools import get_profile_url_tavily

load_dotenv()


def lookup(name: str) -> str:
    """
    Find the Twitter/X username for a given person using AI agent search.
    
    This function creates an AI agent that uses web search tools to find
    the most relevant Twitter/X profile for the specified person and extracts
    their username. The agent uses the ReAct framework for reasoning.
    
    Args:
        name (str): Full name of the person to search for
        
    Returns:
        str: Twitter/X username (without @ symbol)
        
    Example:
        >>> username = lookup("John Doe")
        >>> print(username)  # johndoe
        
    Raises:
        Exception: If the search fails or no profile is found
    """
    # Initialize the language model
    llm = ChatOpenAI(temperature=0, model_name="gpt-4o-mini")
    
    # Define the search template for the agent
    template = """
    Given the name {name_of_person}, I want you to find a link to their Twitter/X profile page,
    and extract from it their username.
    
    In your final answer, provide only the person's username (without the @ symbol)
    which should be extracted from a URL like: https://x.com/USERNAME
    
    For example, if you find https://x.com/johndoe, return only: johndoe
    """
    
    # Define tools available to the agent
    tools_for_agent_twitter = [
        Tool(
            name="Crawl Google 4 Twitter profile page",
            func=get_profile_url_tavily,
            description="Useful for when you need to get the Twitter/X profile page URL. "
                       "Input should be a person's full name."
        ),
    ]

    prompt_template = PromptTemplate(
        input_variables=["name_of_person"], 
        template=template
    )

    # Load the ReAct prompt template from LangChain hub
    react_prompt = hub.pull("hwchase17/react")
    
    # Create the ReAct agent
    agent = create_react_agent(
        llm=llm, 
        tools=tools_for_agent_twitter, 
        prompt=react_prompt
    )
    
    # Create agent executor with error handling
    agent_executor = AgentExecutor(
        agent=agent, 
        tools=tools_for_agent_twitter, 
        verbose=True,
        max_iterations=5,
        handle_parsing_errors=True
    )

    # Execute the agent to find Twitter username
    result = agent_executor.invoke(
        input={"input": prompt_template.format_prompt(name_of_person=name)}
    )

    twitter_username = result["output"]
    return twitter_username


if __name__ == '__main__':
    """
    Test the Twitter lookup agent with a sample search.
    """
    print("Testing Twitter Lookup Agent")
    print("=" * 40)
    
    try:
        # Test with a sample name
        test_name = "Harrison Chase"
        print(f"Searching for Twitter profile of: {test_name}")
        
        twitter_username = lookup(name=test_name)
        print(f"Found Twitter username: {twitter_username}")
        
    except Exception as e:
        print(f"Error during test: {str(e)}")
        print("Please ensure all API keys are properly configured.")