import pandas as pd

def transformar_datos(datos):
    """
    Limpia y transforma los datos extraídos de la API.
    """
    if not datos:
        print("No hay datos para transformar.")
        return None

    print("Transformando datos...")

    df = pd.DataFrame(datos)

    # 1. Renombrar columnas a español
    df = df.rename(columns={
        "userId": "usuario_id",
        "id": "post_id",
        "title": "titulo",
        "body": "contenido"
    })

    # 2. Eliminar filas con valores nulos
    filas_antes = len(df)
    df = df.dropna()
    filas_despues = len(df)
    print(f"Filas eliminadas por nulos: {filas_antes - filas_despues}")

    # 3. Limpiar texto — quitar saltos de línea del contenido
    df["contenido"] = df["contenido"].str.replace("\n", " ", regex=False)

    # 4. Agregar columna de estado
    df["estado"] = "PENDIENTE"

    # 5. Validar que no haya post_id duplicados
    duplicados = df["post_id"].duplicated().sum()
    if duplicados > 0:
        print(f"Advertencia: {duplicados} post_id duplicados detectados")
    else:
        print("Sin duplicados detectados")

    print(f"Total registros transformados: {len(df)}")
    return df


if __name__ == "__main__":
    # Simulamos datos crudos como si vinieran del extractor
    datos_prueba = [
        {"userId": 1, "id": 1, "title": "Título uno", "body": "Contenido\ncon salto"},
        {"userId": 1, "id": 2, "title": "Título dos", "body": "Contenido normal"},
        {"userId": 2, "id": 3, "title": None, "body": "Sin título"},
    ]

    df = transformar_datos(datos_prueba)

    if df is not None:
        print(df)