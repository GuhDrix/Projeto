'''Escreva um programa para aprovar o empréstimo bancário para a compra de uma casa. Pergunte o valor da casa, o salário do comprador e em quantos
 anos ele vai pagar. A prestação mensal não pode exceder 30% do salário ou então o empréstimo será negado.'''
c = float(input('ditite o valor da casa:'))
s = float(input('digite o valor de seu salario:'))
p = float(input('digite quantos anos irá pagar:'))

e = c/(p*12)
b = (s*0.3)+s
if e > b:
    print('o emprestimo é negado')
else:
    print('aprovado')