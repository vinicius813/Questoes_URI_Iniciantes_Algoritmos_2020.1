def main():
    # Entrada
    linha1 = input('Peça 1: ') # 12 1 5.30
    linha2 = input('Peça 2: ') # 16 2 5.10

    dados1 = linha1.split() # ['12', '1', '5.30']
    cod1 = int(dados1([0]))
    qtd1 = int(dados1([1]))
    valor1 = float(dados1([2]))

    dados2 = linha2.split() # ['16', '2', '5.10']
    cod2 = int(dados2([0]))
    qtd2 = int(dados2([1]))
    valor2 = float(dados2([2]))

    # Processamento
    total = calcular_total_a_pagar(qtd1, valor1, qtd2, valor2)

    # Imprimir na tela o resultado
    print(f'VALOR A PAGAR: R$ {total:.2f}')

def calcular_total_a_pagar(q1, q2, v1, v2)
    total = q1*v1 + q2*v2
    return total


main()



