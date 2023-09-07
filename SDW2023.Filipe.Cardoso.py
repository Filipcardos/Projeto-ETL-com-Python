
import pandas as pd

df = pd.read_csv('SDW2023.csv')
user_ids = df['UserID'].tolist()
print(user_ids)

# Simulando a Extração de Dados (Fonte de Dados)
dados_fonte = {
    'Cliente': ['João', 'Maria', 'Pedro', 'Alice'],
    'Saldo_inicial': [5000, 3000, 6000, 4000]
}

df = pd.DataFrame(dados_fonte)

# Função para calcular o rendimento do investimento (Transformação)
def calcular_rendimento(saldo):
    taxa_juros = 0.05  # Taxa de juros de 5%
    return saldo * (1 + taxa_juros)

df['Rendimento'] = df['Saldo_inicial'].apply(calcular_rendimento)

# Função para criar mensagens personalizadas para cada cliente (Transformação)
def criar_mensagem(cliente, saldo_inicial, rendimento):
    return f"Olá {cliente}, seu investimento inicial de R${saldo_inicial} agora vale R${rendimento}. Parabéns pelo seu investimento infantil!"

df['Mensagem'] = df.apply(lambda row: criar_mensagem(row['Cliente'], row['Saldo_inicial'], row['Rendimento']), axis=1)

# Simulando a Carga (imprimir mensagens para os clientes)
for _, row in df.iterrows():
    print(row['Mensagem'])
