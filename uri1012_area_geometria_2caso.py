def main():
    # Entrada para dados
    linha = input('Dados: ')

    dados = linha.split()
    a = float(dados[0])
    b = float(dados[1])
    c = float(dados[2]) 

    # Fragmentação ou Processamento das figuras
    triangulo = area_do_triangulo(base=a, altura=c)
    circulo = area_do_circulo(raio=c)
    trapezio = area_do_trapezio(base_maior=a, base_menor=b, altura=c)
    quadrado = area_do_quadrado(lado=b)
    retangulo = area_do_retangulo(base=a, altura=b)
    
    # Impressão em tela das figuras geométricas
    print(f' TRIÂNGULO:{triangulo:.3f} ')
    print(f' CÍRCULO:{circulo:.3f} ')
    print(f' TRAPÉZIO:{trapezio:.3f} ')
    print(f' QUADRADO:{quadrado:.3f} ')
    print(f' RETÂNGULO:{retangulo:.3f} ')


def area_do_triangulo(base, altura):
    area = (base * altura) / 2
    return area

def area_do_circulo(raio):
    area = 3.14159 * (raio**2)
    return area

def area_do_trapezio(base_maior, base_menor, altura):
    area = ((base_maior + base_menor) * altura) / 2
    return area

def area_do_quadrado(lado):
    area = lado ** 2
    return area

def area_do_retangulo(base, altura):
    area = base * altura
    return area


main()
    



