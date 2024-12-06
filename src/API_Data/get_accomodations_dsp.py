from fetch_accomodations import fetch_all_accommodations
from get_accomodation import get_api_data
import requests

def get_accomodation_description(id):
        URL = f"https://api.avantio.pro/pms/v2/accommodations/{id}"
        header = get_api_data()
        response = requests.get(url = URL,headers= header)
        return response.json()



def dataframe_accomodation():
    apartaments = fetch_all_accommodations()
    dictionary = {}
    for id_ in apartaments:
        header = get_accomodation_description(id = id_)['data']
        name = header['name']
        dictionary[id_] = name
    return dictionary

if __name__ == "__main__":

    print(dataframe_accomodation())