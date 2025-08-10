"""
LinkedIn Lookup Agent

This module implements an AI agent that searches for LinkedIn profile URLs
using web search capabilities. The agent uses LangChain's ReAct framework
to iteratively search and reason about LinkedIn profile information.

Author: Based on original work by Eden Marco (@emarco177)
Course: LangChain Udemy Course by Eden Marco
"""

import os
from dotenv import load_dotenv
from langchain_openai import ChatOpenAI
from langchain_core.prompts import PromptTemplate
from langchain_core.tools import Tool
from langchain.agents import create_react_agent, AgentExecutor
from langchain import hub
from tools.tools import get_profile_url_tavily

load_dotenv()


def lookup(name: str) -> str:
    """
    Find the LinkedIn profile URL for a given person using AI agent search.
    
    This function creates an AI agent that uses web search tools to find
    the most relevant LinkedIn profile for the specified person. The agent
    uses the ReAct (Reasoning and Acting) framework to iteratively search
    and reason about the results.
    
    Args:
        name (str): Full name of the person to search for
        
    Returns:
        str: LinkedIn profile URL for the person
        
    Example:
        >>> url = lookup("John Doe")
        >>> print(url)  # https://www.linkedin.com/in/johndoe/
        
    Raises:
        Exception: If the search fails or no profile is found
    """
    # Initialize the language model
    llm = ChatOpenAI(
        temperature=0,
        model_name="gpt-4o-mini",
        openai_api_key=os.environ.get("OPENAI_API_KEY"),
    )

    # Define the search template for the agent
    template = """
    Given the full name {name_of_person}, I want you to get me a link to their
    LinkedIn profile page. Please search thoroughly and return the most relevant
    and current LinkedIn profile URL.
    
    Your answer should contain only a URL in the format:
    https://www.linkedin.com/in/profile-name/
    """

    prompt_template = PromptTemplate(
        template=template,
        input_variables=["name_of_person"]
    )

    # Define tools available to the agent
    tools_for_agent = [
        Tool(
            name="Crawl Google 4 linkedin profile page",
            func=get_profile_url_tavily,
            description="Useful for when you need to get the LinkedIn profile page URL. "
                       "Input should be a person's full name."
        )
    ]

    # Load the ReAct prompt template from LangChain hub
    react_prompt = hub.pull("hwchase17/react")
    
    # Create the ReAct agent
    agent = create_react_agent(llm=llm, tools=tools_for_agent, prompt=react_prompt)
    
    # Create agent executor with error handling
    agent_executor = AgentExecutor(
        agent=agent, 
        tools=tools_for_agent, 
        verbose=True,
        max_iterations=5,
        handle_parsing_errors=True
    )

    # Execute the agent to find LinkedIn profile
    result = agent_executor.invoke(
        input={"input": prompt_template.format_prompt(name_of_person=name)}
    )

    linkedin_profile_url = result["output"]
    return linkedin_profile_url


if __name__ == '__main__':
    """
    Test the LinkedIn lookup agent with a sample search.
    """
    print("Testing LinkedIn Lookup Agent")
    print("=" * 40)
    
    try:
        # Test with a known LinkedIn profile
        test_name = "Harrison Chase"
        print(f"Searching for LinkedIn profile of: {test_name}")
        
        linkedin_url = lookup(name=test_name)
        print(f"Found LinkedIn URL: {linkedin_url}")
        
    except Exception as e:
        print(f"Error during test: {str(e)}")
        print("Please ensure all API keys are properly configured.")