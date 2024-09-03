# Instalar (pip install - no terminal) Twilio (Enviar SMS) Pandas e Openpyxl - (Integração python com excel)
import pandas as pd
from twilio.rest import Client

# Your Account SID and Auth Token from console.twilio.com
account_sid = "ACfd5fc8adfe6db06c84c5d152d0f449f3"
auth_token = "c928c89fd21d9a7f5db2b9784c6617f5"
client = Client(account_sid, auth_token)

# 1° Abrir os 6 arquivos em excel
lista_meses = ["Janeiro", "Fevereiro", "Março", "Abril", "Maio", "Junho"]

for mes in lista_meses:
    # Mostra o mês - print(mes)
    # F formata a string com algo dinâmico - lê a tabela alterando o mês
    tabela_vendas = pd.read_excel(f"{mes}.xlsx") #print(tabela_vendas)

    #verificar se algum valor na coluna vendas > R$ 55.000 mil - ["Vendas"] é a coluna e any() representa algum valor
    if (tabela_vendas["Vendas"] > 55000).any():
        vendedor = tabela_vendas.loc[tabela_vendas["Vendas"] > 55000, "Vendedor"].values[0] #loc.[linha,venda]
        vendas = tabela_vendas.loc[tabela_vendas["Vendas"] > 55000, "Vendas"].values[0]
        print(f"No mês {mes} alguém bateu a meta. Vendedor: {vendedor}, Vendas: {vendas}")

        # Caso maior, envia SMS para número de celular como nome, mês e vendas do vendedor
        message = client.messages.create(
            to="+5511... - inserir seu número de telefone",
            from_="+..... - inserir código do twilio",
            body=f"No mês {mes} alguém bateu a meta. Vendedor: {vendedor}, Vendas: {vendas}")
        print(message.sid)
