from DB_Accommodation_Avantio.src.API_Data.get_accomodation import get_api_data
import requests
import json
import re
def get_accomodation_description(id):
        URL = f"https://api.avantio.pro/pms/v2/accommodations/{id}"
        header = get_api_data()
        response = requests.get(url = URL,headers= header)
        return response.json()

def get_bathroom_count(api_data):
    bathrooms = api_data.get("distribution", {}).get("bathrooms", [])
    count = 0
    for bathroom in bathrooms:
        if bathroom["type"] == "ONLY_TOILET":
            count += 0.5 * bathroom.get("count", 1)
        else:
            count += bathroom.get("count", 1)
    return count

def get_bed_count(api_data):
    bedrooms = api_data.get("distribution", {}).get("bedrooms", [])
    bed_count = {}
    for bedroom in bedrooms:
        for bed in bedroom.get("beds", []):
            bed_type = bed["type"]
            bed_amount = bed["amount"]
            bed_count[bed_type] = bed_count.get(bed_type, 0) + bed_amount
    return bed_count

def get_bedrooms_count(api_data):
    return len(api_data['distribution'].get('bedrooms',[]))

def get_name(api_data):
    return api_data['name']

def get_area_m2(api_data):
    area = api_data.get('area',None)
    if area != None:
        return api_data['area']['livingSpace']['amount']
    return 0
    
def get_coordinates(api_data):
    return api_data.get('location','').get('coordinates', [])

def get_capacity(api_data):
    return api_data['capacity'].get('maxAdults','')

def get_location(api_data):
    location = api_data['location']
    country = location.get('countryCode','')
    city = location.get('cityName','')
    if location.get('address','') == '':
        address = ''
        district = ''
        return (country,city,address,district)
    address = str(location.get('address','')) + ', ' +  str(location.get('number','S/N'))
    district = location.get('resort','')
    return (country,city,address,district)

def get_status(api_data):
    return api_data['status']

def owner_id(api_data):
    if api_data.get('owner','') == '' :
       return ''
    else: return api_data['owner']['id']
    
def extract_zone(api_data):
    name = get_name(api_data)
    regex = re.search(r'\(([^)]+)\)',name)
    if regex:
        return regex.group(1)
    else: return None

def cleaned_acc_name(api_data):
    name = get_name(api_data)
    return re.sub(r'\s*\([^)]+\)', '', name)

def dataframe_accomodation(accommodations:list):
    aptos = []
    for id_ in accommodations:
        id_acc = str(id_)
        header = get_accomodation_description(id_)['data']
        status = get_status(header)
        nome = cleaned_acc_name(header)
        zone = extract_zone(header)
        area = get_area_m2(header)
        country,city,address,district = get_location(header)
        lat = float(get_coordinates(header).get('lat',''))
        lon = float(get_coordinates(header).get('lon',''))
        camas = str(get_bed_count(header))
        capacidade = get_capacity(header)
        count_banheiros = get_bathroom_count(header)
        count_quartos = get_bedrooms_count(header)
        owner = owner_id(header)
        apto = {'id':id_acc,'nome':nome,'zona':zone,'id_proprietario': owner,'status':status,'tamanho':area,'camas':camas,'qtde_quartos':count_quartos,'qtde_banheiros':count_banheiros,
        'codigo_pais':country,'cidade':city,'endereco':address,
        'bairro':district,'latitude':lat,'longitude':lon,
        'capacidade':capacidade
    } 
        aptos.append(apto)
    return aptos
