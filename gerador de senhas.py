import random

lower_case = 'abcdefghjklmnoprstuvwxyz'
upper_case = 'ABCDEFGJKLMNOPQRSTUVWXYZ'
numbers = '0123456789'
symbols = '!@#$%*()^&'

for_pass = lower_case + upper_case + numbers + symbols

senha_tamanho = 8

password = "".join(random.sample(for_pass, senha_tamanho))

print (f'Minha senha: {password}')
