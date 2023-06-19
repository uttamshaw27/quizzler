import requests

parameter = {
    "Amount": 10,
    "Type": "boolean",
    "category": 18,
}

response = requests.get(url="https://opentdb.com/api.php?amount=10&type=boolean", params=parameter)
response.raise_for_status()
data = response.json()
question_data = data["results"]
