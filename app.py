# aula 1 - crie a sua primeira aplicação

import os

print('Sabor Express')

print('1. Cadastrar Restaurante')
print('2. Listar Restaurantes')
print('3. Ativar Restaurante')
print('4. Sair')

op = int(input('Escolha uma opção: '))

def finalizar_app():
    os.system('cls')
    print('Encerrando o programa ...\n')
    os.system('pause')
    os.system('python app.py')
    
print(f'Opção escolhida: {op}')

if(op == 1):
    print('Cadastrar Restaurante')
elif(op == 2):
    print('Listar Restaurantes')
elif(op == 3):
    print('Ativar Restaurante')
elif(op == 4):
    finalizar_app()
else:
    print('Opção inválida. Encerrando o programa ...')