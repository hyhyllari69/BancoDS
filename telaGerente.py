import tkinter as tk
from conta import Conta
import json


def cadastrar():
    conta = Conta(input_titular.get(), input_agencia.get(), input_cpf.get())

    with open("clientes.json", "r") as clientes_arq:

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

app = tk.Tk()