import requests
from dotenv import load_dotenv
import os 

def get_api_data():
    load_dotenv()
    api = os.getenv("API_AVANTIO")
    headers = {
    "accept": "application/json",
    "X-Avantio-Auth": api
}
    return headers

def get_accomodations(url):
    requisicao = requests.get(url= url, headers=get_api_data())
    return requisicao.json()
