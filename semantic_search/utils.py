import os
import sys
import uuid
from dotenv import load_dotenv, find_dotenv

class Utils:
    def __init__(self):
        pass
    def create_index_name(self, index_name):
        one_key = f'{index_name}-{str(uuid.uuid4())}'
        return one_key
    def get_pinecone_api_key(self):
        return "262656f2-f95b-48b7-ab40-18acc6fb1cd6"
    