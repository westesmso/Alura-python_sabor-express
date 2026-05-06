from modelos.restaurante import Restaurante

restaurante_praca = Restaurante('praça', 'Gourmet')
restaurante_praca.receber_avaliacao('João', 5)
restaurante_praca.receber_avaliacao('Maria', 4)
restaurante_praca.receber_avaliacao('Joaquim', 3)
restaurante_praca.receber_avaliacao('José', 8)
restaurante_praca.receber_avaliacao('Marcinho', -9)

def main():
    Restaurante.listar_restaurantes()
    print()
    restaurante_praca.alternar_status()
    print()
    print(restaurante_praca.ver_media_avaliacao())


if __name__ == "__main__":
    main()