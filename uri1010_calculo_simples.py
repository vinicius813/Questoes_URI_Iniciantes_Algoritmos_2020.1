# Montando esquema de peças para Alg
vinicius = input() .split()
codigo_1 = int(vinicius[0])
num_1 = int(vinicius[1])
valor_1 = float(vinicius[2])
total_1 = num_1 * valor_1

# Montando o meio do esquema de peças Alg
guilherme = input() .split()
codigo_2 = int(guilherme[0])
num_2 = int(guilherme[1])
valor_2 = float(guilherme[2])
total_2 = num_2 * valor_2

# Montando o fim do esquema de peças Alg
total_total = total_1 + total_2

# Valor a se pagar no total
print('VALOR A PAGAR: R$ {:.2f}'.format(total_total))

