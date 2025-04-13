import os
from dotenv import load_dotenv, find_dotenv
LOGGER_PATH=os.getenv("LOGGER_PATH","logs/analysis.logs")

load_dotenv()

class OpenAISettings:
        api_key = os.getenv("OPENAI_API_KEY")
        azure_endpoint=os.getenv("AZURE_ENDPOINT")
        azure_deployment=os.getenv("AZURE_DEPLOYMENT")
        api_version=os.getenv("API_VERSION")
        model_name=os.getenv("MODEL_NAME")
