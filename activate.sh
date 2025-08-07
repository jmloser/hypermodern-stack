#!/bin/bash

# Hypermodern Python Stack Activation Script
# Run this script to activate your development environment

echo "🚀 Activating Hypermodern Python Stack..."

# Activate virtual environment
source .venv/bin/activate

# Add some useful aliases for common commands
alias serve-api="uv run uvicorn hypermodern_stack.api:app --reload --host 127.0.0.1 --port 8000"
alias run-tests="uv run pytest tests/ -v"
alias run-jupyter="uv run jupyter lab"
alias format-code="uv run ruff format . && uv run ruff check ."
alias type-check="uv run mypy src/"

# Display helpful information
echo "✅ Virtual environment activated!"
echo ""
echo "📚 Available commands:"
echo "  serve-api     - Start the FastAPI development server"  
echo "  run-tests     - Run the test suite"
echo "  run-jupyter   - Start JupyterLab"
echo "  format-code   - Format and lint code with Ruff"
echo "  type-check    - Run MyPy type checking"
echo ""
echo "🔧 Development commands:"
echo "  uv add <package>        - Add new dependencies"
echo "  uv sync                 - Install/update dependencies" 
echo "  uv run <command>        - Run commands in the virtual environment"
echo ""
echo "🌟 Happy coding with your hypermodern Python stack!"
echo "📖 Check out the README.md and sample notebook for examples."
