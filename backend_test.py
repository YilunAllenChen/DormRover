import requests


requests.post('http://localhost:5000/command', json={
    'data': 100
})