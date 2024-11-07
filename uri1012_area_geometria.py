def main():
    # Começo do problema
    A = float(input('Digite aqui valor A: '))
    B = float(input('Digite aqui o valor B: '))
    C = float(input('Digite aqui o valor C: '))

    # Áreas de figuras geométricas
    area1 = A * C / 2
    area2 = 3.14159 * (C ** 2)
    area3 = (A + B) * C
    area4 = B * B
    area5 = A * B

    # Impressão de resultados
    print(f'TRIÂNGULO: '{area1:.3f})
    print(f'CÍRCULO: '{area2:.3f})
    print(f'TRAPÉZIO: '{area3:.3f})
    print(f'QUADRADO: '{area4:.3f})
    print(f'RETÂNGULO: '{area5:.3f})


main()


