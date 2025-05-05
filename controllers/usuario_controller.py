from models.usuario_model import usuario
from fastapi import HTTPException
import hashlib
from database.db import conectar

def criptografar_senha(senha):
    return hashlib.sha256(senha.encode()).hexdigest()

def cadastrar_usuario(usuario:usuario):
    conn = conectar()
    cursor = conn.cursor()

    try:
        sql = """
            INSERT INTO usuarios
            (nome, email, whatasapp, senha, rua, numero, complemento, cep, ponto_referencia)
            VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)
            """
        valores = (
            usuario.nome,
            usuario.email,
            usuario.whatsapp,
            criptografar_senha(usuario.senha),
            usuario.rua,
            usuario.numero,
            usuario.complemento,
            usuario.cep,
            usuario.ponto_referencia
        )
        cursor.execute(sql, valores)
        conn.commit()

    except Exception as e:
        print("Erro ao criar usuário:", e)
        raise HTTPException(status_code=500, detail="Erro interno ao logar usuário.")
    finally:
        cursor.close()
        conn.close()

def autenticar_usuario(email: str, senha: str):
    conn = conectar()
    cursor = conn.cursor()

    try:
        senha_criptografada = criptografar_senha(senha)
        sql = "SELECT * FROM usuarios WHERE email = %s AND senha = %s"
        cursor.execute(sql, (email, senha_criptografada))
        if usuario:
            return usuario
        else:
            raise HTTPException(status_code=401, detail="Email ou senha incorretos")
    finally:
        cursor.close()
        conn.close()