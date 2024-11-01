import os
from dotenv import load_dotenv

from pathlib import Path
env_path = Path(__file__).resolve().parent.parent / '.env'
load_dotenv(dotenv_path=env_path)


class Config:
    API_KEY = os.getenv('OPENAI_API_KEY')
    COLLECTION_NAME = os.getenv('COLLECTION_NAME')
    MODEL_ID = os.getenv('MODEL_ID')
    MODEL_BASENAME = os.getenv('MODEL_BASENAME')

    DATA_DIRECTORY = os.path.join(os.path.dirname(__file__),'..','Data')
    PERSIST_DIRECTORY = os.path.join(os.path.dirname(__file__),'..','vector_store')
    os.makedirs(PERSIST_DIRECTORY, exist_ok=True)

    LOG_DIR = os.path.join(os.path.dirname(__file__),'..','log_dir')
    os.makedirs(LOG_DIR, exist_ok=True)


    MODEL_NAME = "sentence-transformers/all-mpnet-base-v2"
    MODEL_KWARGS = {'device': 'cpu'}
    ENCODE_KWARGS = {'normalize_embeddings': False}
    CHUNK_SIZE = 1024
    CHUNK_OVERLAP = 200
    
    