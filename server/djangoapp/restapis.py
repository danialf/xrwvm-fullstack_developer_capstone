import requests
import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Set up URLs with default values
backend_url = os.getenv('backend_url', default="http://localhost:3030")
sentiment_analyzer_url = os.getenv('sentiment_analyzer_url', default="http://localhost:5050/")


def get_request(endpoint, **kwargs):
    """Make a GET request to the backend with optional parameters."""
    params = "&".join([f"{key}={value}" for key, value in kwargs.items()]) if kwargs else ""
    request_url = f"{backend_url}{endpoint}?{params}"
    print(f"GET from {request_url}")

    try:
        response = requests.get(request_url)
        response.raise_for_status()  # Raise an exception for 4xx/5xx status codes
        return response.json()
    except requests.RequestException as err:
        print(f"Network exception occurred: {err}")
        return None


def analyze_review_sentiments(text):
    """Analyze the sentiment of a review."""
    request_url = f"{sentiment_analyzer_url}analyze/{text}"
    try:
        response = requests.get(request_url)
        response.raise_for_status()  # Raise an exception for 4xx/5xx status codes
        return response.json()
    except requests.RequestException as err:
        print(f"Network exception occurred: {err}")
        return None


def post_review(data_dict):
    """Post a new review to the backend."""
    request_url = f"{backend_url}/insert_review"
    try:
        response = requests.post(request_url, json=data_dict)
        response.raise_for_status()  # Raise an exception for 4xx/5xx status codes
        print(response.json())
        return response.json()
    except requests.RequestException as err:
        print(f"Network exception occurred: {err}")
        return None
