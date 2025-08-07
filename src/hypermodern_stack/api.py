"""Sample FastAPI application demonstrating the hypermodern stack."""

from fastapi import FastAPI
from pydantic import BaseModel
import pandas as pd
import numpy as np
from typing import List

app = FastAPI(
    title="Hypermodern Python API",
    description="A sample API showcasing modern Python tools for data science and backend development",
    version="0.1.0"
)

class DataPoint(BaseModel):
    """A sample data point model."""
    x: float
    y: float
    label: str

@app.get("/")
async def root():
    """Root endpoint."""
    return {"message": "Welcome to the Hypermodern Python Stack!"}

@app.post("/analyze/", response_model=dict)
async def analyze_data(data: List[DataPoint]):
    """Analyze a list of data points using pandas and numpy."""
    # Convert to pandas DataFrame
    df = pd.DataFrame([point.model_dump() for point in data])
    
    # Perform some basic analysis
    analysis = {
        "count": len(df),
        "mean_x": float(df['x'].mean()),
        "mean_y": float(df['y'].mean()),
        "std_x": float(df['x'].std()),
        "std_y": float(df['y'].std()),
        "correlation": float(df['x'].corr(df['y'])) if len(df) > 1 else None,
        "unique_labels": df['label'].unique().tolist()
    }
    
    return analysis

@app.get("/health/")
async def health_check():
    """Health check endpoint."""
    return {"status": "healthy"}
