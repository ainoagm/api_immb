import requests

pregunta =input("Titulo de la pregunta")

API_KEY = "2a32694f"

#dirección = f"http://www.omdbapi.com/?apikey="API_key+"=tt3896198"+pregunta
#dirección = f"http://www.omdbapi.com/?apikey={API_KEY}&i={pregunta}"
dirección = "http://www.omdbapi.com/?apikey={}&t={}".format(API_KEY, pregunta)

respuesta = requests.get(direccion)

if respuesta.status_code == 200:
    datos = respuesta.json()
    if datos['response'] == "False":
        print(datos["Error"])
    else:
        primera_peli =  datos ['Search'][0]
        clave = primera_peli['imbID']

        otra_direccion = "http://www.omdbapi.com/?apikey={}&t={}".format(API_KEY, clave)
        nueva_respuesta = request.get(otra_direccion)
        if nueva_respuesta.status_code == 200:
            datos = respuesta.json()
            if datos['response'] == "False":
                print(datos["Error"])
            else:
                titulo = datos['Title']
                agno = datos['year']
                director = datos['director']
                print("La peli {}, estrenada en el año {}, fue dirigida por {}".format(titulo, agno, director))
        else:
            print("Error en consulta por id:", nueva_respuesta.status_code)
else:
    print("Error en busqueda:", respuesta.status_code)

