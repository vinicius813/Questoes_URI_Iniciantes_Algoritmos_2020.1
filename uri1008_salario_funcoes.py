def main():
    # Entrada
    id = int(input('id = '))
    horas = int(input('horas: '))
    valor_hora = float(input('Valor hora: '))

    # Processamento
    salario = calcular_salario(horas, valor_hora)

    # Saída
    print(f' NUMBER = {id}')
    print(f' SALARY = U$ {salario:.2f}')


def calcular_salario(horas,valor):
    resultado = horas * valor
    return resultado


main()
