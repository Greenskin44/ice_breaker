# Ice Breaker - AI-Powered Conversation Starter

An intelligent web application that generates personalized conversation starters using AI agents and Retrieval-Augmented Generation (RAG) with LangChain. The system analyzes LinkedIn profiles and Twitter/X posts to create engaging ice breakers for networking and professional interactions.

## 🚀 Features

- **AI-Powered Analysis**: Utilizes OpenAI's GPT models to analyze professional profiles and social media content
- **Multi-Source Data Integration**: Combines LinkedIn profile information with Twitter/X posts for comprehensive insights
- **Agent-Based Architecture**: Employs specialized agents for different data sources (LinkedIn and Twitter/X)
- **RAG Implementation**: Uses Retrieval-Augmented Generation for contextual and accurate information processing
- **Web Interface**: Clean, responsive web interface built with Flask
- **Real-time Processing**: Dynamic content generation based on user input

## 📋 Prerequisites

- Python 3.12 or higher
- OpenAI API key
- Scrapin.io API key (for LinkedIn data)
- Twitter/X API credentials (Bearer token, API keys, and access tokens)
- Tavily API key (for web searches)

## 🛠️ Installation

1. **Clone the repository:**
   ```bash
   git clone https://github.com/[your-username]/ice_breaker.git
   cd ice_breaker
   ```

2. **Install dependencies using Pipenv:**
   ```bash
   pipenv install
   pipenv shell
   ```

   **Or using pip with requirements.txt:**
   ```bash
   pip install -r requirements.txt
   ```

3. **Set up environment variables:**
   Create a `.env` file in the root directory with the following variables:
   ```env
   OPENAI_API_KEY=your_openai_api_key
   SCRAPIN_API_KEY=your_scrapin_api_key
   TWITTER_BEARER_TOKEN=your_twitter_bearer_token
   TWITTER_API_KEY=your_twitter_api_key
   TWITTER_API_KEY_SECRET=your_twitter_api_key_secret
   TWITTER_ACCESS_TOKEN=your_twitter_access_token
   TWITTER_ACCESS_TOKEN_SECRET=your_twitter_access_token_secret
   TAVILY_API_KEY=your_tavily_api_key
   ```

## 🚀 Usage

1. **Start the application:**
   ```bash
   python app.py
   ```

2. **Access the web interface:**
   Open your browser and navigate to `http://localhost:5000`

3. **Generate ice breakers:**
   - Enter a person's full name in the input field
   - Click "Do Your Magic" to generate personalized conversation starters
   - The system will analyze their LinkedIn profile and Twitter/X posts to create relevant ice breakers

## 🏗️ Project Structure

```
ice_breaker/
├── app.py                      # Flask web application entry point
├── ice_breaker.py             # Main application logic and orchestration
├── output_parsers.py          # Pydantic models for structured output parsing
├── requirements.txt           # Python dependencies
├── Pipfile                    # Pipenv configuration
├── agents/                    # AI agents for different data sources
│   ├── linkedin_lookup_agent.py
│   └── twitter_lookup_agent.py
├── third_parties/            # External API integrations
│   ├── linkedin.py
│   └── twitter.py
├── tools/                    # Utility tools and functions
│   └── tools.py
└── templates/                # HTML templates for web interface
    └── index.html
```

## 🔧 Core Components

### AI Agents
- **LinkedIn Agent**: Searches for and processes LinkedIn profile information
- **Twitter Agent**: Finds and analyzes Twitter/X profiles and recent posts

### Data Sources
- **LinkedIn Profiles**: Professional information, experience, and background
- **Twitter/X Posts**: Recent social media activity and interests

### RAG Implementation
The system implements Retrieval-Augmented Generation by:
1. Retrieving relevant information from multiple sources
2. Processing and structuring the data using LangChain
3. Generating contextual responses using OpenAI's language models

## 🔧 Configuration

### Environment Variables
Ensure all required API keys are properly configured in your `.env` file. The application uses:
- **OpenAI API**: For natural language processing and generation
- **Scrapin.io**: For LinkedIn profile data extraction
- **Twitter API v2**: For accessing Twitter/X user data and tweets
- **Tavily Search**: For web search capabilities

### API Rate Limits
Be aware of API rate limits for external services:
- Twitter API has various rate limits depending on your access level
- OpenAI API usage is billed based on token consumption
- Scrapin.io has monthly request limits based on your plan

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add some amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

## 📄 License

This project is licensed under the Apache License 2.0 - see the [LICENSE](LICENSE) file for details.

## 🙏 Acknowledgements

This project was originally created by **Eden Marco** ([@emarco177](https://github.com/emarco177)) as part of a comprehensive LangChain course.

## ⚠️ Disclaimer

This project was completed as part of Eden Marco's Udemy Course on LangChain for educational purposes. The implementation demonstrates practical applications of:
- LangChain framework for building AI applications
- Multi-agent systems for data processing
- RAG (Retrieval-Augmented Generation) techniques
- Integration of multiple APIs and data sources

## 🐛 Known Issues

- Mock data functionality is available for testing without API keys
- Rate limiting may affect real-time performance with high usage
- LinkedIn scraping depends on third-party service availability

## 🔮 Future Enhancements

- Add support for additional social media platforms
- Implement caching for improved performance
- Add user authentication and session management
- Include more sophisticated conversation starter templates
- Add analytics and usage tracking

## 📞 Support

For questions, issues, or contributions, please:
1. Check existing [Issues](https://github.com/[your-username]/ice_breaker/issues)
2. Create a new issue if needed
3. Refer to Eden Marco's original course materials for additional context