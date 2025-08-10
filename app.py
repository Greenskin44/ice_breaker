"""
Ice Breaker Flask Web Application

A Flask-based web application that provides a user-friendly interface
for generating AI-powered conversation starters using LinkedIn and Twitter data.

This application serves as the entry point for the Ice Breaker system,
handling HTTP requests and orchestrating the ice breaker generation process.

Author: Based on original work by Eden Marco (@emarco177)
Course: LangChain Udemy Course by Eden Marco
"""

from dotenv import load_dotenv
from flask import Flask, render_template, request, jsonify
import logging

# Load environment variables before importing other modules
load_dotenv()

from ice_breaker import ice_break_with

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

app = Flask(__name__)


@app.route("/")
def index():
    """
    Serve the main application page.
    
    Returns:
        Rendered HTML template for the ice breaker interface
    """
    return render_template("index.html")


@app.route("/process", methods=["POST"])
def process():
    """
    Process ice breaker generation request.
    
    Handles POST requests containing a person's name and returns
    generated conversation starters and profile information.
    
    Returns:
        JSON response containing:
        - summary_and_facts: Generated summary and interesting facts
        - photoUrl: Profile picture URL from LinkedIn
        
    Raises:
        400: If name parameter is missing
        500: If processing fails
    """
    try:
        # Extract name from form data
        name = request.form.get("name")
        if not name:
            return jsonify({"error": "Name parameter is required"}), 400
            
        logger.info(f"Processing ice breaker request for: {name}")
        
        # Generate ice breaker content
        summary_and_facts, profile_pic_url = ice_break_with(name=name)
        
        # Return structured response
        response = {
            "summary_and_facts": summary_and_facts.to_dict(),
            "photoUrl": profile_pic_url or "",
        }
        
        logger.info(f"Successfully processed request for: {name}")
        return jsonify(response)
        
    except Exception as e:
        error_name = request.form.get("name", "unknown")
        logger.error(f"Error processing request for {error_name}: {str(e)}")
        return jsonify({
            "error": "Failed to generate ice breaker content. Please try again.",
            "details": str(e) if app.debug else None
        }), 500


@app.errorhandler(404)
def not_found_error(error):
    """Handle 404 errors."""
    return jsonify({"error": "Page not found"}), 404


@app.errorhandler(500)
def internal_error(error):
    """Handle 500 errors."""
    return jsonify({"error": "Internal server error"}), 500


if __name__ == '__main__':
    logger.info("Starting Ice Breaker Flask application...")
    app.run(host="0.0.0.0", port=5000, debug=True)