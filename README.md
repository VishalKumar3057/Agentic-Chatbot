# LangGraph Agentic AI Chatbot

## Project Overview

This is an **End-to-End Agentic AI Chatbot** built using **LangGraph** - a framework for building stateful, multi-agent conversational AI systems. The project creates a web-based chatbot interface that allows users to interact with different Large Language Models (LLMs) through a clean, user-friendly Streamlit interface.

## What This Project Does

The application provides a modular, extensible platform for building intelligent conversational agents that can maintain context, process complex workflows, and integrate with multiple LLM providers. Currently implemented as a basic chatbot with plans for more advanced agentic capabilities.

## Key Features

### 🤖 Multi-LLM Support
- **Groq Integration**: Support for Gemma2-9b-it, Llama-3.1-8b-instant, Qwen3-32b models
- **OpenAI Integration**: Support for latest GPT models including O3-mini, O4-mini, GPT-4.1-mini
- Easy switching between different LLM providers through the UI

### 🏗️ Modular Architecture
- **State Management**: Uses LangGraph's state system to maintain conversation context
- **Graph-Based Processing**: Implements conversation flow as a directed graph with nodes and edges
- **Extensible Design**: Built to easily add new use cases and functionalities
- **Clean Separation**: Distinct modules for LLMs, UI, graph building, and state management

### 🌐 Interactive Web Interface
- **Streamlit-powered UI** with intuitive sidebar controls
- **Secure API Key Management** for LLM access
- **Real-time Chat Interface** with message history
- **Responsive Design** with wide layout support

### 🔧 Current Use Cases
- **Basic Chatbot**: Simple conversational AI that processes user messages and generates intelligent responses
- **Extensible Framework**: Ready for additional use cases like RAG, tool calling, multi-agent workflows

## Technical Architecture

```
src/langgraphagenticai/
├── LLMS/                 # LLM integration classes
│   └── llms.py          # Groq and OpenAI implementations
├── graph/               # Graph builder components
│   └── graph_builder.py # Workflow creation logic
├── nodes/               # Processing nodes
│   └── basic_chatbot_node.py # Chatbot logic
├── state/               # State management
│   └── state.py         # Conversation state definition
├── ui/                  # User interface components
│   ├── streamlitui/     # Streamlit interface
│   └── uiconfigfile.*   # UI configuration
└── tools/               # Future tool integrations
```

## Technology Stack

- **🔗 LangGraph**: For building stateful AI agent workflows
- **🦜 LangChain**: Core framework for LLM integration and orchestration
- **🎨 Streamlit**: Modern web interface framework
- **⚡ Groq API**: High-performance LLM inference
- **🧠 OpenAI API**: Advanced language model capabilities
- **🐍 Python 3.13**: Primary programming language

## Installation & Setup

1. **Clone the repository**
   ```bash
   git clone <repository-url>
   cd "03. Agentic ChatBot - LangGraph"
   ```

2. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

3. **Run the application**
   ```bash
   python app.py
   ```

4. **Access the interface**
   - Open your browser to the Streamlit URL (typically `http://localhost:8501`)
   - Select your preferred LLM provider (Groq or OpenAI)
   - Enter your API key
   - Choose a use case and start chatting!

## Configuration

The application uses a configuration file (`uiconfigfile.ini`) to manage:
- Available LLM providers and models
- Use case options
- UI settings and page titles

## API Keys Required

- **Groq API Key**: Get yours at [https://console.groq.com/keys](https://console.groq.com/keys)
- **OpenAI API Key**: Get yours at [https://platform.openai.com/api-keys](https://platform.openai.com/api-keys)

## Future Enhancements

This project serves as a **foundation** for building more complex agentic AI systems. Planned features include:

- 🔍 **RAG Integration**: Document retrieval and question answering
- 🛠️ **Tool Calling**: Integration with external APIs and services
- 👥 **Multi-Agent Workflows**: Collaborative AI agent systems
- 📊 **Advanced Analytics**: Conversation insights and performance metrics
- 🔄 **Workflow Automation**: Complex multi-step task execution

## Project Structure Benefits

- **Scalability**: Easy to add new LLM providers and use cases
- **Maintainability**: Clean separation of concerns
- **Extensibility**: Plugin-like architecture for new features
- **Production-Ready**: Error handling and robust configuration management

## Contributing

This project demonstrates modern practices for building production-ready AI applications with:
- Modular design patterns
- Comprehensive error handling
- Configurable components
- User-friendly interfaces

Perfect for developers looking to understand how to build scalable, stateful AI chatbot systems using cutting-edge frameworks like LangGraph and LangChain.