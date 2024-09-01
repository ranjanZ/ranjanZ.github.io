import requests
import streamlit as st

# Get the app's URL
url = "http://localhost:8501"

# Fetch the HTML content
response = requests.get(url)

# Save the HTML content to a file
with open("saved_app.html", "w") as file:
    file.write(response.text)
