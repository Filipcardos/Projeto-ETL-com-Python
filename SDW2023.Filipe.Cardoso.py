from pathlib import Path

import pandas as pd


def main():
    caminho = Path(__file__).with_name("SDW2023.csv")
    clientes = pd.read_csv(caminho)
    for linha in clientes.itertuples(index=False):
        saldo = linha.Saldo_inicial
        saldo_final = saldo * 1.05
        print(f"Olá, {linha.UserID.strip()}! Seu saldo de R$ {saldo:.2f} "
              f"passou para R$ {saldo_final:.2f}.")


if __name__ == "__main__":
    main()
