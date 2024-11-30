import requests
from dotenv import load_dotenv
import os
from typing import List, Dict

# Load environment variables from .env file
load_dotenv()

# Function to search for shoes using Axesso API
def search_shoes_axesso(niche: str, min_price: float, max_price: float, features: List[str]) -> Dict:
    api_url = "https://axesso-axesso-amazon-data-service-v1.p.rapidapi.com/amz/search"
    api_key = os.getenv("RAPIDAPI_KEY")  # API key from .env file

    # Define search parameters
    params = {
        "keyword": niche,
        "min_price": min_price,
        "max_price": max_price,
        "page": 1,
        "country": "US"
    }

    if features:
        params["keyword"] += " " + " ".join(features)

    # Authentication headers
    headers = {
        "X-RapidAPI-Key": api_key,
        "X-RapidAPI-Host": "axesso-axesso-amazon-data-service-v1.p.rapidapi.com"
    }

    # Perform the API request
    response = requests.get(api_url, headers=headers, params=params)

    if response.status_code == 200:
        results = response.json()
        return find_best_value_item(results.get("products", []))
    else:
        return {"error": response.text}

# Helper function to find the best value-for-money item
def find_best_value_item(products: List[Dict]) -> Dict:
    best_item = None
    for product in products:
        if not best_item or (product["rating"] / product["price"] > best_item["rating"] / best_item["price"]):
            best_item = product
    return best_item
