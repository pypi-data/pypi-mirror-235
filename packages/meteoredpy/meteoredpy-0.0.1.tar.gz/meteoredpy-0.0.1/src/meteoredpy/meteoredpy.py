# Libreria para consumir y parsear a JSON API de meteored.cl
import json
import requests
import xmltodict

class meteoredpy:
    def __init__(self, token):
        self.token = token
    def get(self, ciudad):
        ciudad_id = self.__get_id_ciudad(ciudad)
        API_URL_CLIMA = f'http://api.meteored.cl/index.php?api_lang=cl&localidad={ciudad_id}&affiliate_id={self.token}'
        if ciudad_id == -1:
            return {'error': 2, 'msg': 'La ciudad no existe'}
        elif ciudad_id == -2:
            return {'error': 3, 'msg': 'Hubo un problema al intentar conectarse a la API de búsqueda de ciudades'}
        try:  
            response = requests.get(API_URL_CLIMA)
            if response.status_code == 200:
                xml_clima = xmltodict.parse(response.content)
                ciudad_nombre = xml_clima['report']['location']['@city']
                maxima_hoy = xml_clima['report']['location']['var'][1]['data']['forecast'][0]['@value']
                return {'ciudad' :ciudad_nombre, 'maxima': maxima_hoy, 'error': 0}
        except Exception as e:
            return {'error': 1, 'msg': e} # Excepción
        
    def __get_id_ciudad(self, ciudad):
        API_URL_CIUDADES = 'https://www.meteored.cl/peticionBuscador.php?lang=cl&texto='
        try:
            response = requests.get(f'{API_URL_CIUDADES}{ciudad}')
            if response.status_code == 200:
                json_ciudades = json.loads(response.content)
                if len(json_ciudades['localidad']) < 1 :
                    return -1
                return json_ciudades['localidad'][0]['id']
        except Exception as e:
            return -2 # Mala solicitud
