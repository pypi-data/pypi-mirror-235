# meteoredpy
Libreria para consumir y parsear a JSON API de meteored.cl

## Uso
Antes de comenzar, es necesario registrarse en la página de [meteored.cl](https://www.meteored.cl/api/#/registro) para así obtener una _affiliate_id__(API KEY).

``` python
from meteoredpy import Meteoredpy
API_KEY = ''
clima = Meteoredpy(API_KEY).get('conce')
print(clima)
'''
puede entregar 4 resultados:
1. {'ciudad': 'Concepción [Biobío;Chile]', 'maxima': '18', 'error': 0}
2. {'error': 1, 'msg': NameError("name 'xmltodict' is not defined")}
3. {'error': 2, 'msg': 'La ciudad no existe'}
4. {'error': 3, 'msg': 'Hubo un problema al intentar conectarse a la API de búsqueda de ciudades'}
'''
```
### Tipo de resultados
- Si el resultado que entrega es el (1), quiere decir que la consulta fue realizada con éxito.
- Si el resultado que entrega es el (2), quiere decir que hubo una excepción, tal como muestra el ejemplo, la cual se solucionaría instalando la librería faltante. También, puede mostrar otro tipo de excepciones, tales como que hubo problemas para conectarse a la API del meteored.cl
- Si el resultado que entrega es el (3), quiere decir que la ciudad no existe.
- Si el resultado que entrega es el (4), quiere decir que hubo problemas para conectarse a la API de búsqueda de ciudades.

