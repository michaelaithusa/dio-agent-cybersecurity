import sqlite3

def login_seguro(usuario, senha):
    conn = sqlite3.connect('banco.db')
    cursor = conn.cursor()
    
    # CORREÇÃO: Uso de consultas parametrizadas
    query = "SELECT * FROM usuarios WHERE username = ? AND password = ?"
    
    cursor.execute(query, (usuario, senha))
    resultado = cursor.fetchone()
    conn.close()
    
    if resultado:
        return "Login com sucesso!"
    return "Falha no login."
