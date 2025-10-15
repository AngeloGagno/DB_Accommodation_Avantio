from DB_Accommodation_Avantio.src.API_Data.get_accomodation import get_accomodations

def fetch_all_accommodations():
    """Percorre todas as páginas da API para coletar todas as acomodações"""
    id_list = []  
    next_url = 'https://api.avantio.pro/pms/v2/accommodations?status=ENABLED&status=DISABLED'

    while next_url:  
        data = get_accomodations(next_url)  
        for i in data['data']:
            id_list.append(i['id'])
        next_url = data.get('_links', {}).get('next')  
    return id_list

