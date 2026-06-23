import tkinter as tk
from tkinter import ttk
from conta import Conta
import json


def cadastrar():
    conta = Conta(entry_titular.get(), entry_agencia.get(), entry_cpf.get())

    with open("clientes.json", "r") as clientes_arq:
        clientes = json.load(clientes_arq)

    clientes.append({
            "titular": conta.titular,
            "agencia": conta.agencia,
            "numero": conta.numero,
            "cpf": conta.cpf,
            "saldo": conta.saldo,
            "senha": conta.senha,
            "chavepix": conta.chavepix
        })

    with open("clientes.json", "w") as clientes_escrita:
        json.dump(clientes, clientes_escrita, indent=4)
    label_resposta.configure(
            text=f"Conta: {conta.numero} Titular: {conta.titular} cadastrado com sucesso!",
            fg="green")



# ==================== Janela Principal ====================
janela = tk.Tk()
janela.title("Banco Fácil - Cadastro de Conta")
janela.geometry("450x400")
janela.configure(bg="#f0f4f7")  # cor de fundo suave
janela.resizable(False, False)

# Título
titulo = tk.Label(
    janela, text="Cadastro de Conta", 
    font=("Helvetica", 18, "bold"), fg="#0b3d91", bg="#f0f4f7"
)
titulo.pack(pady=20)

# Frame para os campos com borda
frame = tk.Frame(janela, bg="#ffffff", bd=2, relief="groove")
frame.pack(pady=10, padx=30, fill="x")

# Titular
tk.Label(frame, text="Titular:", font=("Helvetica", 11), bg="#ffffff").pack(anchor="w", padx=10, pady=(10, 0))
entry_titular = tk.Entry(frame, font=("Helvetica", 11), width=40, bd=2, relief="solid")
entry_titular.pack(pady=5, padx=10, fill="x")

# Agência
tk.Label(frame, text="Agência:", font=("Helvetica", 11), bg="#ffffff").pack(anchor="w", padx=10, pady=(10, 0))
entry_agencia = tk.Entry(frame, font=("Helvetica", 11), width=40, bd=2, relief="solid")
entry_agencia.pack(pady=5, padx=10, fill="x")

# CPF
tk.Label(frame, text="CPF:", font=("Helvetica", 11), bg="#ffffff").pack(anchor="w", padx=10, pady=(10, 0))
entry_cpf = tk.Entry(frame, font=("Helvetica", 11), width=40, bd=2, relief="solid")
entry_cpf.pack(pady=5, padx=10, fill="x")

# Botão Enviar
style = ttk.Style()
style.configure("TButton", font=("Helvetica", 11, "bold"), foreground="white", background="#0b3d91")
style.map("TButton", background=[("active", "#074185")])

btn_enviar = ttk.Button(janela, text="ENVIAR", command=cadastrar, style="TButton")
btn_enviar.pack(pady=20)

# Label de Resposta
label_resposta = tk.Label(
    janela, text="", font=("Helvetica", 11), bg="#f0f4f7", fg="#333333", justify="center", wraplength=400
)
label_resposta.pack(pady=10)

# Rodapé
rodape = tk.Label(
    janela, text="© 2026 - Sistema Banco Fácil", font=("Helvetica", 9), fg="gray", bg="#f0f4f7"
)
rodape.pack(side="bottom", pady=10)

janela.mainloop()