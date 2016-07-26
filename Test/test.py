import requests
import json
q=dict({'q':1})
response=requests.post('http://127.0.0.1:8000/api/add/',q)
print(response.text)
