#from database import db  # ou o caminho correto até seu db.py

#def testar_conexao():
 #   try:
        #conexao = db.conectar()
        #cursor = conexao.cursor()
        #cursor.execute("SELECT 1")
        #resultado = cursor.fetchone()
        #print("✅ Conexão com o banco funcionando:", resultado)
        #cursor.close()
        #conexao.close()
    #except Exception as e:
        #print("❌ Erro ao conectar com o banco:", e)

# Executa o teste ao iniciar
#testar_conexao()

from fastapi import FastAPI
from routes import usuario_routes
from fastapi.staticfiles import StaticFiles

app = FastAPI()

app.mount("/static", StaticFiles(directory="static"), name="static")

app.include_router(usuario_routes.router)