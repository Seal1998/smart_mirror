import requests

timezone = 2
json_response = requests.get('http://worldclockapi.com/api/json/utc/now', ).json()
print(json_response['currentDateTime'])

