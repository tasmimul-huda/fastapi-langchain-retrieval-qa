# test/raf_pipeline/test_retriever_chain.py
import pytest
from unittest.mock import MagicMock, patch
import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../')))
from rag_pipeline.retriever_chain import RetrieverChain

# Sample input and expected output
user_input = "What is the capital of France?"
mock_documents = [
    {"id": "1", "text": "Paris is the capital of France."},
    {"id": "2", "text": "The Eiffel Tower is in Paris, France."},
    {"id": "3", "text": "The Eiffel Tower is in Paris, France."}
]

@pytest.fixture
def mock_retriever_chain():
    # Setting up a mock retriever chain
    with patch('rag_pipeline.retriever_chain.get_chroma_client') as mock_get_chroma_client:
        # Mocking the vector database
        mock_vector_db = MagicMock()
        mock_vector_db.as_retriever.return_value.get_relevant_documents.return_value = mock_documents
        mock_get_chroma_client.return_value = mock_vector_db
        
        # Instantiate RetrieverChain with mocks
        retriever_chain = RetrieverChain("test_collection", "embedding_func", "/path/to/persist_dir")
        
        return retriever_chain

def test_retrieve_documents(mock_retriever_chain):
    # Test if retrieve_documents returns the expected documents
    docs = mock_retriever_chain.get_relevent_docs(user_input)
    
    # Verify the length and content of returned documents
    assert len(docs) == 3, "Should return exactly 2 documents"
    assert docs == mock_documents, "Returned documents do not match expected output"
    assert any("Paris" in doc["text"] for doc in docs), "Relevant document content not found in returned documents"

