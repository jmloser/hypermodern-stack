# Hypermodern Python Stack

A comprehensive, modern Python development environment optimized for backend API development and data science work.

## 🚀 What's Included

### **Core Data Science Stack**
- **NumPy** 2.0+ - Fundamental package for scientific computing
- **SciPy** 1.14+ - Scientific computing library
- **Pandas** 2.2+ - Data manipulation and analysis
- **Polars** 1.0+ - Blazingly fast DataFrame library (modern alternative to pandas)
- **PyArrow** 17+ - Columnar in-memory analytics
- **scikit-learn** 1.5+ - Machine learning library
- **XArray** - N-dimensional labeled arrays

### **Backend API Development**
- **FastAPI** 0.115+ - Modern, fast web framework
- **Uvicorn** - ASGI server implementation
- **Pydantic** 2.9+ - Data validation using Python type annotations
- **AsyncPG** - Fast PostgreSQL Database Client Library for Python/asyncio
- **SQLAlchemy** 2.0+ - SQL toolkit and Object Relational Mapping (ORM)
- **Redis** 5.1+ - In-memory data structure store
- **HTTPX** - HTTP client for Python

### **Modern Visualization Tools**
- **Plotly** 5.24+ - Interactive plotting
- **Altair** 4.2+ - Declarative statistical visualization (Grammar of Graphics)
- **Seaborn** 0.13+ - Statistical data visualization
- **Bokeh** 3.5+ - Interactive visualization library
- **HoloViews** 1.19+ - Declarative data visualizations
- **Datashader** 0.16+ - Big data visualization

### **Interactive Computing & Notebooks**
- **Jupyter** 1.1+ - Interactive computing
- **JupyterLab** 4.2+ - Web-based interactive development environment
- **Quarto** (system-wide) - Scientific and technical publishing system
- **ipywidgets** 8.1+ - Interactive HTML widgets

### **Data Processing & ETL**
- **DuckDB** 1.1+ - In-process SQL OLAP database
- **Dask** 2024+ - Parallel computing library
- **Prefect** 3.0+ - Modern workflow orchestration
- **Ibis** 9.4+ - Universal Python data analytics frontend

### **Machine Learning & Optimization**
- **LightGBM** 4.5+ - Gradient boosting framework
- **XGBoost** 3.0+ - Gradient boosting library
- **CatBoost** 1.2+ - Gradient boosting on decision trees
- **Optuna** 4.0+ - Hyperparameter optimization framework
- **MLflow** 3.2+ - Machine learning lifecycle management
- **Numba** 0.61+ - JIT compiler for Python

### **Development Tools**
- **uv** 0.8+ - Fast Python package manager
- **Ruff** 0.12+ - Extremely fast Python linter and code formatter
- **MyPy** 1.17+ - Static type checker
- **pytest** 8.4+ - Testing framework
- **Coverage** 7.10+ - Code coverage measurement

### **Modern Utility Libraries**
- **Typer** 0.16+ - CLI framework based on Python type hints
- **Rich** 14+ - Library for rich text and beautiful formatting
- **Loguru** 0.7+ - Better logging
- **Structlog** 25+ - Structured logging
- **Streamlit** 1.48+ - Web app framework for data science

## 🛠️ Quick Start

### 1. Activate the Environment
```bash
cd /Users/john/python-projects/hypermodern-stack
source .venv/bin/activate
```

### 2. Start JupyterLab
```bash
uv run jupyter lab
```

### 3. Run the Sample API
```bash
uv run uvicorn src.hypermodern_stack.api:app --reload
```

Visit http://localhost:8000/docs to see the interactive API documentation.

### 4. Run Tests
```bash
uv run pytest
```

### 5. Format and Lint Code
```bash
uv run ruff check .
uv run ruff format .
```

## 📊 Example Usage

### Data Analysis with Modern Tools
```python
import polars as pl
import pandas as pd
import numpy as np
import plotly.express as px

# Use Polars for fast data manipulation
df = pl.DataFrame({
    'x': np.random.normal(0, 1, 1000),
    'y': np.random.normal(0, 1, 1000),
    'category': np.random.choice(['A', 'B', 'C'], 1000)
})

# Convert to pandas for compatibility with visualization libraries
df_pandas = df.to_pandas()

# Create interactive visualization with Plotly
fig = px.scatter(df_pandas, x='x', y='y', color='category', 
                title='Interactive Scatter Plot')
fig.show()
```

### API Development with FastAPI
```python
from fastapi import FastAPI
from pydantic import BaseModel
import asyncpg

app = FastAPI()

class User(BaseModel):
    name: str
    email: str
    age: int

@app.post("/users/")
async def create_user(user: User):
    # Async database operations with asyncpg
    return {"message": f"User {user.name} created successfully"}
```

## 🏗️ Project Structure
```
hypermodern-stack/
├── src/
│   └── hypermodern_stack/
│       ├── __init__.py
│       └── api.py          # Sample FastAPI application
├── tests/                  # Test directory
├── notebooks/              # Jupyter notebooks (create as needed)
├── pyproject.toml         # Project configuration and dependencies
├── README.md              # This file
└── .venv/                 # Virtual environment (created by uv)
```

## 🔧 Development Workflow

1. **Install dependencies**: `uv sync`
2. **Add new dependencies**: `uv add package-name`
3. **Run development server**: `uv run uvicorn src.hypermodern_stack.api:app --reload`
4. **Run tests**: `uv run pytest`
5. **Format code**: `uv run ruff format .`
6. **Lint code**: `uv run ruff check .`
7. **Type checking**: `uv run mypy src/`

## 🎯 Optional Dependency Groups

Install additional packages for specific use cases:

### Geographic Data
```bash
uv sync --extra geo
```
Includes: GeoPandas, Folium, Rasterio, Shapely, Contextily

### Natural Language Processing
```bash
uv sync --extra nlp
```
Includes: Transformers, Tokenizers, Datasets, spaCy, NLTK

### Development Tools
```bash
uv sync --extra dev
```
Includes: pre-commit, Black, isort, Bandit, pip-audit

## 📚 Key Features of This Stack

- ⚡ **Blazingly Fast**: uv for package management, Polars for DataFrames, Ruff for linting
- 🛡️ **Type Safe**: Full type annotations with MyPy and Pydantic
- 🔄 **Async Ready**: AsyncPG, FastAPI, and HTTPX for async operations
- 📊 **Modern Viz**: Interactive plotting with Plotly, Altair, and Bokeh
- 🧪 **Testing**: Comprehensive testing with pytest and coverage
- 📝 **Documentation**: Quarto for reproducible scientific publishing
- 🏗️ **Production Ready**: FastAPI, Uvicorn, and structured logging

## 🚀 Next Steps

1. Start building your API in `src/hypermodern_stack/api.py`
2. Create Jupyter notebooks in a `notebooks/` directory
3. Write tests in the `tests/` directory
4. Use Quarto to create reproducible reports and documentation

Happy coding with your hypermodern Python stack! 🐍✨
