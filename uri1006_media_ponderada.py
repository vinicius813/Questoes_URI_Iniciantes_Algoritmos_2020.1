def main():
    # Entrada
    nota_1 = float(input('Nota 1: '))
    nota_2 = float(input('Nota 2: '))
    nota_3 = float(input('Nota 3: '))

    # Processamento
    MEDIA = (nota_1 * 2 + nota_2 * 3 + nota_3 * 5) / (2 + 3 + 5)
    # PEMDAS

    # Saída
    print('MEDIA = {:.2f}'.format(MEDIA))


main()

