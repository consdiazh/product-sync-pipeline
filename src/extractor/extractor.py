import requests
import pandas as pd

def extraer_productos(cantidad=20):
    """
    Extrae posts desde la API pública JSONPlaceholder.
    Simula una extracción de datos real.
    """
    url = "https://jsonplaceholder.typicode.com/posts"

    params = {
        "_limit": cantidad
    }

    print(f"Extrayendo {cantidad} registros desde la API...")

    response = requests.get(url, params=params)

    if response.status_code != 200:
        print(f"Error al conectar con la API: {response.status_code}")
        return None

    datos = response.json()

    print(f"Registros obtenidos: {len(datos)}")
    return datos


if __name__ == "__main__":
    datos = extraer_productos()

    if datos:
        df = pd.DataFrame(datos)
        print(df.head(5))