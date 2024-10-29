# tests/test_answer.py
import pytest
import sys
import os
from fastapi.testclient import TestClient
parent_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
sys.path.insert(0, parent_dir)
from unittest.mock import patch
from application.main import app


# Create a TestClient for the FastAPI application
client = TestClient(app)


def test_generate_answer_valid_question():
    response = client.post("/answer", json={"question": "summarize the documents"})
    assert response.status_code == 200
    assert "answer" in response.json()
    assert isinstance(response.json()["answer"], str)
    assert len(response.json()["answer"]) > 0  # Ensure the answer is non-empty

def test_generate_answer_empty_question():
    response = client.post("/answer", json={"question": ""})
    assert response.status_code == 400
    assert response.json() == {"detail": "Question must be a non-empty string."}

def test_generate_answer_invalid_type():
    response = client.post("/answer", json={"question": 123})
    assert response.status_code == 400
    assert response.json() == {"detail": "Question must be a non-empty string."}

def test_generate_answer_missing_question():
    response = client.post("/answer", json={})
    assert response.status_code == 400
    assert response.json() == {"detail": "Question must be a non-empty string."}
