import json 
import os
import time
import requests
import streamlit as st
from dotenv import load_dotenv

load_dotenv()

OXYLABS_BASE_URL = "https://api.oxylabs.io/v1/queries"
OXYLABS_API_KEY = os.getenv("OXYLABS_API_KEY")
OXYLABS_API_SECRET = os.getenv("OXYLABS_API_SECRET")


def post_query(payload):
    username = os.getenv("OXYLABS_USERNAME")
    password = os.getenv("OXYLABS_PASSWORD")

    response = requests.post(
        OXYLABS_BASE_URL,
        auth=(username, password),
        json=payload,
    )
    response.raise_for_status()  # Raise an error for HTTP errors
    return response.json()  # Return the JSON response


def normalize_product(content):
    category_path = []
    if content.get("category_path"):
        category_path = [cat.strip() for cat in content["category_path"] if cat]
    return {

            "asin": content.get("asin"),
    "url": content.get("url"),
    "brand": content.get("brand"),
    "price": content.get("price"),
    "stock": content.get("stock"),
    "title": content.get("title"),
    "rating": content.get("rating"),
    "images": content.get("images", []),
    "categories": content.get("category", []) or content.get("categories", []),
    "category_path": category_path,
    "currency": content.get("currency"),
    "buybox": content.get("buybox", []),
    "product_overview": content.get("product_overview", []),

    }