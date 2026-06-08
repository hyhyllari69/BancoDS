from conta import Conta
conta1 = Conta("Patrick", 1234, "1010-7", "111.111.111-11")
conta1.extrato()
conta1.deposito(1000)
conta1.saque(200)
conta1.saque(1500)
conta1.extrato()
conta2 = Conta("Demili", 1234, "7070-7", "999.999.999-99")
conta2.extrato()
conta1.transferir(300, conta2)
conta1.extrato()
conta2.extrato()
conta2.titular = "Demylly"
print(f'''Olá, {conta2.titular}! :)
Agência: {conta2.agencia} Conta: {conta2.numero}
Saldo: {conta2.saldo}
Senha: {conta2.senha}
Chaves pix: {conta2.chavepix}''')