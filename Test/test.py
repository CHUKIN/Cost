import requests
import json
#q=dict({'name':'qwedsa111111111111111', 'group':'Машина','priority':2,'cost':123,'user':'Я'})
#response=requests.post('http://127.0.0.1:8000/api/add/',q)
#print(json.loads(response.text))
response=requests.get('http://127.0.0.1:8000/api/show/')
print(json.loads(response.text))
