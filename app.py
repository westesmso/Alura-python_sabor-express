# aula 1 - crie a sua primeira aplicação

import os
import sys

restaurantes = [{'nome': 'Pizzaria do Zé', 'categoria': 'Pizzaria', 'ativo': False}, {'nome': 'Churrascaria do João', 'categoria': 'Churrascaria', 'ativo': False}, {'nome': 'Sushi House',
                                                                                                                                                                     'categoria': 'Sushi', 'ativo': False}, {'nome': 'Restaurante da Maria', 'categoria': 'Restaurante', 'ativo': True}, {'nome': 'Hamburgueria do Carlos', 'categoria': 'Hamburgueria', 'ativo': True}]


def exibir_nome_programa():
    '''Exibe o nome do programa'''
    os.system('cls')
    print("""
    ░██████╗░█████╗░██████╗░░█████╗░██████╗░  ███████╗██╗░░██╗██████╗░██████╗░███████╗░██████╗░██████╗
    ██╔════╝██╔══██╗██╔══██╗██╔══██╗██╔══██╗  ██╔════╝╚██╗██╔╝██╔══██╗██╔══██╗██╔════╝██╔════╝██╔════╝
    ╚█████╗░███████║██████╦╝██║░░██║██████╔╝  █████╗░░░╚███╔╝░██████╔╝██████╔╝█████╗░░╚█████╗░╚█████╗░
    ░╚═══██╗██╔══██║██╔══██╗██║░░██║██╔══██╗  ██╔══╝░░░██╔██╗░██╔═══╝░██╔══██╗██╔══╝░░░╚═══██╗░╚═══██╗
    ██████╔╝██║░░██║██████╦╝╚█████╔╝██║░░██║  ███████╗██╔╝╚██╗██║░░░░░██║░░██║███████╗██████╔╝██████╔╝
    ╚═════╝░╚═╝░░╚═╝╚═════╝░░╚════╝░╚═╝░░╚═╝  ╚══════╝╚═╝░░╚═╝╚═╝░░░░░╚═╝░░╚═╝╚══════╝╚═════╝░╚═════╝░  
        """)


def exibir_opcoes_menu():
    '''Exibe as opções do menu'''
    print('Escolha uma opção:')
    print('1. Cadastrar Restaurante')
    print('2. Listar Restaurantes')
    print('3. Ativar Restaurante')
    print('4. Sair')


def finalizar_app():
    '''Finaliza o programa'''
    print('Encerrando o programa ...\n')
    sys.exit()


def voltar_ao_menu():
    '''Volta ao menu principal'''

    input('\n Pressione alguma tecla para voltar ao menu ...\n')


def exibir_subtitulos(texto):
    '''Exibe um sub-titulo'''
    os.system('cls')
    linha = '*' * len(texto)
    print(linha)
    print(texto)
    print(linha)
    print()


def opcao_invalida():
    '''Exibe uma mensagem de opção inválida'''
    print('Opção inválida\n')
    voltar_ao_menu()


def alternar_estado_restaurante():
    '''Alterna o estado de ativo do restaurante
    
    inputs:
    - nome_restaurante: str
    outputs:
    - None
    '''
    exibir_subtitulos('Alternando estado de ativo do restaurante ...')
    nome_restaurante = input('Digite o nome do restaurante: ')
    restaurante_encontrado = False
    for restaurante in restaurantes:
        if nome_restaurante == restaurante['nome']:
            restaurante_encontrado = True
            restaurante['ativo'] = not restaurante['ativo']
            print(
                f'\nRestaurante "{restaurante["nome"]}" agora está {"Ativo" if restaurante["ativo"] else "Inativo"}!\n')
    if not restaurante_encontrado:
        print(f'\nRestaurante "{nome_restaurante}" não encontrado!\n')
    voltar_ao_menu()


def cadastrar_restaurante():
    '''Cadastra um novo restaurante'''
    exibir_subtitulos('Cadastrando restaurante ...')
    nome_restaurante = input('Digite o nome do restaurante: ')
    categoria_restaurante = input(
        f'Digite a categoria do restaurante {nome_restaurante}: ')
    restaurantes.append(
        {'nome': nome_restaurante, 'categoria': categoria_restaurante, 'ativo': False})
    print(f'\nRestaurante "{nome_restaurante}" cadastrado com sucesso!\n')
    os.system('pause')
    voltar_ao_menu()


def listar_restaurantes():
    '''Lista todos os restaurantes'''
    exibir_subtitulos('Listando restaurantes ...')
    print(f'{"Nome".ljust(32)} | {"Categoria".ljust(20)} | {"Status"}')
    print('-' * 70)
    for restaurante in restaurantes:
        print(
            f'- {restaurante["nome"].ljust(30)} | {restaurante["categoria"].ljust(20)} | {"Ativo" if restaurante["ativo"] else "Inativo"}')
    voltar_ao_menu()


def escolher_opcao():
    '''Escolhe uma opção do menu'''
    try:
        op = int(input('Escolha uma opção: '))

        print(f'\nOpção escolhida: {op}\n')

        match op:
            case 1:
                exibir_subtitulos('Cadastrando restaurante ...')
                cadastrar_restaurante()
            case 2:
                exibir_subtitulos('Listando restaurantes ...')
                listar_restaurantes()
            case 3:
                exibir_subtitulos('Ativando restaurante ...')
                alternar_estado_restaurante()
            case 4:
                finalizar_app()
            case _:
                opcao_invalida()
    except ValueError:
        opcao_invalida()


def main():
    '''Função principal'''
    while True:
        os.system('cls')
        exibir_nome_programa()
        exibir_opcoes_menu()
        escolher_opcao()


if __name__ == '__main__':
    '''Ponto de entrada do programa'''
    main()
