import psycopg2
from psycopg2.extras import execute_values

def conectar_db():
    """
    Crea y retorna una conexión a PostgreSQL.
    """
    conn = psycopg2.connect(
        host="localhost",
        port=5432,
        database="pipeline_db",
        user="postgres",
        password="admin123"
    )
    return conn


def cargar_datos(df):
    """
    Carga el DataFrame en la tabla posts de PostgreSQL.
    Evita duplicados usando INSERT ... ON CONFLICT DO NOTHING.
    """
    if df is None or df.empty:
        print("No hay datos para cargar.")
        return

    print(f"Cargando {len(df)} registros en PostgreSQL...")

    conn = conectar_db()
    cursor = conn.cursor()

    registros = [
        (row["post_id"], row["usuario_id"], row["titulo"], row["contenido"], row["estado"])
        for _, row in df.iterrows()
    ]

    query = """
        INSERT INTO posts (post_id, usuario_id, titulo, contenido, estado)
        VALUES %s
        ON CONFLICT (post_id) DO NOTHING
    """

    execute_values(cursor, query, registros)
    conn.commit()

    print(f" {cursor.rowcount} registros insertados correctamente")

    cursor.close()
    conn.close()


if __name__ == "__main__":
    import sys
    sys.path.append(".")
    from src.extractor.extractor import extraer_productos
    from src.transformer.transformer import transformar_datos

    datos = extraer_productos()
    df = transformar_datos(datos)
    cargar_datos(df)