# Product Sync Pipeline

Pipeline de sincronización de datos construido con Python que extrae 
información desde una API pública, la transforma y valida con pandas, 
la almacena en PostgreSQL y la expone mediante una API REST con FastAPI.

## Arquitectura

API pública → Extractor → Transformer → PostgreSQL → FastAPI

## Stack técnico

- **Python 3.14** — lenguaje principal
- **pandas** — transformación y validación de datos
- **PostgreSQL** — base de datos relacional
- **psycopg2** — conexión Python ↔ PostgreSQL
- **FastAPI** — API REST
- **uvicorn** — servidor ASGI

## Estructura del proyecto
src/
├── extractor/    # Extracción desde API pública
├── transformer/  # Limpieza y validación con pandas
├── loader/       # Carga en PostgreSQL
└── api/          # API REST con FastAPI
## Instalación

```bash
# Clonar el repositorio
git clone https://github.com/consdiazh/product-sync-pipeline.git
cd product-sync-pipeline

# Crear y activar entorno virtual
python -m venv venv
source venv/Scripts/activate  # Windows

# Instalar dependencias
pip install -r requirements.txt
```

## Configuración

Crear la base de datos en PostgreSQL:

```sql
CREATE DATABASE pipeline_db;
\c pipeline_db
CREATE TABLE posts (
    post_id    INTEGER PRIMARY KEY,
    usuario_id INTEGER NOT NULL,
    titulo     TEXT,
    contenido  TEXT,
    estado     VARCHAR(20) DEFAULT 'PENDIENTE'
);
```

## Uso

Correr el pipeline completo (extrae, transforma y carga en PostgreSQL):

```bash
python src/loader/loader.py
```

Iniciar la API:

```bash
uvicorn src.api.main:app --reload
```

Endpoints disponibles:

| Método | Endpoint | Descripción |
|--------|----------|-------------|
| GET | `/` | Estado de la API |
| GET | `/posts` | Todos los registros |
| GET | `/posts/{id}` | Registro por ID |

Documentación interactiva disponible en `http://127.0.0.1:8000/docs`

## Autor

Constanza Díaz — [LinkedIn](https://linkedin.com/in/constanzadiazhidalgo)