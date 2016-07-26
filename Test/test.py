import requests
import json
#q=dict({'name':'про12312вепавпвака', 'group':'Машина','priority':1,'cost':123,'user':'Я'})
#response=requests.post('http://127.0.0.1:8000/api/add/',q)
#print(json.loads(response.text))
response=requests.get('http://127.0.0.1:8000/api/show/')
print(response.text)
