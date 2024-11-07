# Leia o nome de um vendedor
nome = input()

# Digitar o salário fixo
sal_fixo = float(input())

# Calcular as vendas
sal_vendas = float(input())

# Digitar o valor da comissão
sal_comissao = sal_vendas * 0.15
TOTAL = sal_comissao + sal_fixo

# Digitar o vencimento total
print('TOTAL = R$ {:.2f}'.format(TOTAL))

