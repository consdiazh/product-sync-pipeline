from fastapi import FastAPI
from psycopg2.extras import RealDictCursor
import sys
sys.path.append(".")
from src.loader.loader import conectar_db

app = FastAPI(title="Product Sync Pipeline API")


@app.get("/")
def inicio():
    return {"mensaje": "API funcionando correctamente"}


@app.get("/posts")
def obtener_posts():
    conn = conectar_db()
    cursor = conn.cursor(cursor_factory=RealDictCursor)
    cursor.execute("SELECT * FROM posts")
    posts = cursor.fetchall()
    cursor.close()
    conn.close()
    return {"total": len(posts), "datos": posts}


@app.get("/posts/{post_id}")
def obtener_post(post_id: int):
    conn = conectar_db()
    cursor = conn.cursor(cursor_factory=RealDictCursor)
    cursor.execute("SELECT * FROM posts WHERE post_id = %s", (post_id,))
    post = cursor.fetchone()
    cursor.close()
    conn.close()
    if post is None:
        return {"error": "Post no encontrado"}
    return post