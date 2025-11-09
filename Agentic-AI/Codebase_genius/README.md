# Codebase Genius

An AI-powered, multi-agent system that automatically generates high-quality documentation for any software repository using Jac language and byLLM.

## Quick Start

1. **Activate venv**: `source venv/bin/activate`
2. **Start backend**: `cd backend && jac serve main.jac`
3. **Start frontend**: In another terminal: `cd frontend && jac streamlit app.jac`

## Architecture

- **Code Genius**: Supervisor agent orchestrating workflow
- **Repo Mapper**: Clones repo, builds file tree, summarizes README
- **Code Analyzer**: Parses code with Tree-sitter, builds Code Context Graph
- **DocGenie**: Generates markdown documentation and diagrams

## Technology

- Jac 0.8.10
- byLLM 0.4.5
- Google Gemini API
- Tree-sitter for code parsing
- NetworkX for graph operations
