"""Tests for the sample API."""

import pytest
from fastapi.testclient import TestClient
from hypermodern_stack.api import app

client = TestClient(app)

def test_root():
    """Test the root endpoint."""
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == {"message": "Welcome to the Hypermodern Python Stack!"}

def test_health_check():
    """Test the health check endpoint."""
    response = client.get("/health/")
    assert response.status_code == 200
    assert response.json() == {"status": "healthy"}

def test_analyze_data():
    """Test the data analysis endpoint."""
    test_data = [
        {"x": 1.0, "y": 2.0, "label": "A"},
        {"x": 3.0, "y": 4.0, "label": "B"},
        {"x": 5.0, "y": 6.0, "label": "A"}
    ]
    
    response = client.post("/analyze/", json=test_data)
    assert response.status_code == 200
    
    result = response.json()
    assert "count" in result
    assert "mean_x" in result
    assert "mean_y" in result
    assert result["count"] == 3
    assert result["mean_x"] == 3.0  # (1 + 3 + 5) / 3
    assert result["mean_y"] == 4.0  # (2 + 4 + 6) / 3
    assert set(result["unique_labels"]) == {"A", "B"}
