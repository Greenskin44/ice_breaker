"""
Output Parsers for Ice Breaker Application

This module defines Pydantic models and parsers for structured output
from LangChain LLM responses. It ensures that the AI-generated content
follows a consistent format for the web application.

Author: Based on original work by Eden Marco (@emarco177)
Course: LangChain Udemy Course by Eden Marco
"""

from typing import List, Dict, Any
from langchain_core.output_parsers import PydanticOutputParser
from pydantic import BaseModel, Field


class Summary(BaseModel):
    """
    Pydantic model for structured summary output.
    
    This model defines the expected structure for AI-generated
    conversation starters and ensures consistent formatting.
    
    Attributes:
        summary (str): A concise summary about the person
        facts (List[str]): A list of interesting facts that can serve as conversation starters
    """
    summary: str = Field(
        description="A concise summary about the person based on their LinkedIn profile and social media activity"
    )
    facts: List[str] = Field(
        description="A list of interesting facts about the person that could serve as conversation starters"
    )

    def to_dict(self) -> Dict[str, Any]:
        """
        Convert the Summary object to a dictionary.
        
        Returns:
            Dict[str, Any]: Dictionary representation with 'summary' and 'facts' keys
        """
        return {"summary": self.summary, "facts": self.facts}

    def __str__(self) -> str:
        """
        String representation of the Summary object.
        
        Returns:
            str: Formatted string showing summary and facts
        """
        facts_str = "\n".join([f"• {fact}" for fact in self.facts])
        return f"Summary: {self.summary}\n\nInteresting Facts:\n{facts_str}"


# Initialize the parser for use with LangChain
summary_parser = PydanticOutputParser(pydantic_object=Summary)