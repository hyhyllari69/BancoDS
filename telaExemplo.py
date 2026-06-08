import tkinter as tk

def login():
    if input_email.get() == "admin":
        if input_senha.get() == "1234":
            label_resposta.configure(text="Login realizado com sucesso!", fg="green")
        else:
            label_resposta.configure(text="Falha no login", fg="red")
    else:
        label_resposta.configure(text="Falha no login", fg="red")

app = tk.Tk()
app.title("Tela Exemplo")
app.geometry("400x300")

# EMAIL
label_email = tk.Label(app, text="Email:")
label_email.pack(pady=5)
input_email = tk.Entry(app)
input_email.pack()

# SENHA
label_senha = tk.Label(app, text="Senha:")
label_senha.pack(pady=5)
input_senha = tk.Entry(app, show="*")
input_senha.pack()

# ENVIAR
botao = tk.Button(app, text="Enviar", command=login)
botao.pack(pady=10)

# RESPOSTA
label_resposta = tk.Label(app, text="")
label_resposta.pack(pady=5)

app.mainloop() # -> executar a tela em laço infinito