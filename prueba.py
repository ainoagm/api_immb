import requests

dirección = "http://www.omdbapi.com/?apikey=2a32694f&i=tt3896198" #url a la que quiero llamar

#hacerpeticion HTTP
respuesta = requests.get(dirección)

if respuesta.status_code == 200:
    print(respuesta.text)
    datos = respuesta.json()
    print(datos)
else:
    print("Se ha producido un error", respuesta.status_code)