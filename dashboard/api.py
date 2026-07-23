import requests

API_URL = "http://127.0.0.1:8000/api/v1/analyze"


def analyze_csv(uploaded_file):
    files = {
        "file": (
            uploaded_file.name,
            uploaded_file.getvalue(),
            "text/csv",
        )
    }

    response = requests.post(API_URL, files=files)

    response.raise_for_status()

    return response.json()
