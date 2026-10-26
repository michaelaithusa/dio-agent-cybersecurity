import sqlite3

def login_inseguro(usuario, senha):
    conn = sqlite3.connect('banco.db')
    cursor = conn.cursor()
    
    # VULNERABILIDADE: Concatenação direta de strings no SQL (SQL Injection)
    query = f"SELECT * FROM usuarios WHERE username = '{usuario}' AND password = '{senha}'"
    
    cursor.execute(query)
    resultado = cursor.fetchone()
    conn.close()
    
    if resultado:
        return "Login com sucesso!"
    return "Falha no login."

# Simulando um ataque
usuario_input = "admin' --"
senha_input = "qualquer_coisa"
print(login_inseguro(usuario_input, senha_input))
