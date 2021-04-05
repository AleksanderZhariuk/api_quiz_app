import requests
import json

URL = 'https://opentdb.com/api.php'
parameters = {
    'amount': 10,
    'category': 11,
    'difficulty': 'easy',
    'type': 'boolean'
}

response = requests.get(URL, params=parameters).json()
question_data = response['results']
for question in question_data:
    question['question'] = question['question'].replace('&quot;', "'").replace('&#039;', "'")