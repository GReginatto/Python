cpf = '962284080'
nove_digitos = cpf[:9]
contagem_regressiva = 10
total = 0

for digito in nove_digitos:
    total += int(digito) * contagem_regressiva
    contagem_regressiva -= 1

digito_1 = total * 10 % 11
digito_1 = digito_1 if digito_1 <= 9 else 0


contagem_regressiva2 = 11
total2 = 0

for digito in nove_digitos:
    total2 += int(digito) * contagem_regressiva2
    
    contagem_regressiva2 -= 1

total2 = total2 + digito_1*2
digito_2 = total2 * 10 % 11
digito_2 = digito_2 if digito_2 <= 9 else 0

novo_cpf = nove_digitos + str(digito_1) + str(digito_2)

print (f'Seu CPF é {novo_cpf}')

