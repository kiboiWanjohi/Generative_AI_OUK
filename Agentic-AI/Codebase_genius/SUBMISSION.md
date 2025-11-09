Codebase Genius - Assignment  2 Submission

System Overview

Codebase Genius is an AI-powered, multi-agent code documentation system that automatically generates comprehensive documentation for any GitHub repository.

Architecture
The system consists of three main layers:

Frontend Layer (Streamlit - Port 8501): Provides interactive web interface for users to input repository URLs and view analysis results. Displays code structure, generated documentation, and enables markdown file downloads.

Backend API Layer (FastAPI - Port 8001): Serves /analyze endpoint that orchestrates the analysis pipeline. Receives repository URLs and returns JSON responses containing markdown documentation and code structure data.

Processing Agents Layer (Python Utilities): Independent modular components that handle specific tasks - repository cloning, code analysis, documentation generation, and code context graph building.

Components
1. Repo Mapper (utils/repo_cloner.py) - Clones GitHub repositories to local storage, extracts directory structure with configurable depth, retrieves README content from repository root, filters out common non-code directories (.git, node_modules, pycache).

2. Code Analyzer (utils/code_extractor.py) - Uses Python AST module to parse Python files, extracts function definitions with parameters, extracts class definitions with methods, builds module list from file paths, supports batch processing of multiple files up to configurable limits.

3. CCG Builder (utils/ccg_builder.py) - Creates Code Context Graph by analyzing code elements, builds node and edge representations, establishes relationships between functions and classes, generates Mermaid diagrams for visualization.

4. Markdown Generator (utils/markdown_generator.py) - Assembles comprehensive markdown documentation from all extracted data, includes project overview with repository link, directory structure visualization, code structure analysis with modules/classes/functions, formats output for readability and professional presentation.

5. FastAPI Bridge (backend_api.py) - Provides HTTP POST endpoint /analyze?repo_url={url}, coordinates between all utility modules, handles request/response serialization, returns JSON with status, markdown content, and code structure data.

Output Example

The system generates markdown documentation containing:

Project title and repository information

Project overview with README summary

Directory structure visualization

Complete code structure analysis

Module documentation

Class documentation with methods

Top-level function signatures with parameters

Code context graph with relationships

Professional formatting and markdown syntax

Example generated documentation shows:

Flask application structure

Modules: flask.app, flask.blueprints, flask.views, flask.cli

Classes: Flask (with methods init, route, run, add_url_rule), Blueprint (with methods init, route, register), Request (with methods init, get_json, get_data)

Functions: create_app(config), render_template(template_name, **context), jsonify(*args, **kwargs), url_for(endpoint, **values)

Technologies Used
Backend Framework: FastAPI (Python web framework)

Frontend Framework: Streamlit (Python UI framework)

Code Analysis: Python AST (Abstract Syntax Tree)

Documentation Format: Markdown with Mermaid diagrams

Language: Python 3.8+

Architecture Pattern: Multi-agent with separation of concerns

How to Run
Step 1 - Start Backend API (Terminal 1):
Navigate to ~/codebase_genius/backend and execute: python backend_api.py
This starts the FastAPI server on http://0.0.0.0:8001

Step 2 - Start Frontend UI (Terminal 2):
Navigate to ~/codebase_genius and execute: streamlit run frontend/app.py
This launches Streamlit on http://localhost:8501

Step 3 - Test API (Terminal 3):
Execute curl command: curl -X POST "http://localhost:8001/analyze?repo_url=https://github.com/pallets/flask"
Or access frontend UI at http://localhost:8501

File Structure
~/codebase_genius/
├── backend/
│ ├── utils/
│ │ ├── repo_cloner.py (Repository cloning and file tree extraction)
│ │ ├── code_extractor.py (AST-based code analysis)
│ │ ├── ccg_builder.py (Code Context Graph generation)
│ │ ├── markdown_generator.py (Documentation assembly)
│ │ └── jac_python_bridge.py (Jac integration bridge)
│ ├── agents/
│ │ └── repo_mapper.jac (Jac agent for repo mapping)
│ ├── main.jac (Main Jac entry point)
│ └── backend_api.py (FastAPI application)
├── frontend/
│ └── app.py (Streamlit web interface)
├── SUBMISSION.md (This document)
└── README.md (General project information)

Key Features
 Automatic repository cloning and analysis from GitHub URLs
 AST-based code structure extraction supporting Python files
 Code Context Graph (CCG) generation with relationships
 Professional markdown documentation output
 Real-time web interface with live analysis
 Downloadable markdown files from UI
 Support for any public GitHub repository
 Modular architecture for easy extension
 Error handling and graceful degradation
 Mock data support for rapid prototyping

Assignment Requirements Met
 Multi-agent architecture - Implemented Repo Mapper, Code Analyzer, DocGenie agents
 Repository cloning - Full git clone functionality with file tree extraction
 README extraction - Automatic retrieval and summarization of README content
 Code structure analysis - Complete parsing of functions, classes, modules
 Code Context Graph (CCG) - CCG builder with node/edge relationships
 Markdown documentation - Professional output with all required sections
 API endpoint - RESTful /analyze endpoint for programmatic access
 Web UI - Interactive Streamlit frontend for user analysis
 Downloadable files - Markdown files downloadable from frontend
 Multiple agents - Python utilities coordinated through FastAPI
 Real-time processing - Immediate results display in UI

Testing Results
 Backend API tested with curl - Returns valid JSON with markdown
 Frontend UI tested - Displays analysis results with code structure
 Markdown generation tested - Professional formatting with all sections
 Download functionality tested - Markdown files download correctly
 API endpoint tested - Handles Flask repository successfully
 UI refresh tested - Hot reloading works for real-time updates
 Error handling tested - Graceful handling of invalid URLs

Data Flow

User enters GitHub URL in Streamlit UI → Frontend sends HTTP POST to /analyze endpoint → FastAPI receives request → Backend activates Repo Mapper agent to clone repository and extract structure → Code Analyzer agent processes files and extracts code elements → CCG Builder creates relationship graph → Markdown Generator assembles documentation → Response returned to frontend as JSON with markdown content → Frontend displays results and enables download → User downloads markdown file

Future Enhancements
Support for additional programming languages (JavaScript, Java, Go)

Advanced AI integration for intelligent documentation

Database storage for documentation history

Team collaboration features

Custom template support for documentation

Advanced filtering and search capabilities

Integration with documentation hosting platforms

System Status
 Development Complete - All required features implemented and tested
 Ready for Submission - System fully functional and meeting all assignment requirements
 Production Ready - Error handling and edge cases covered
 Extensible - Modular architecture allows for future enhancements