from modelos.avaliacao import Avaliacao

class Restaurante:

    restaurantes = []

    def __init__(self, nome, categoria):
        self._nome = nome.title()
        self._categoria = categoria.upper()
        self._ativo = False
        self._avaliacao = []
        Restaurante.restaurantes.append(self)
    def __str__(self):
        return f'{self._nome} - {self._categoria} - {"Ativo" if self.ativo else "Inativo"}'

    def nome(self):
        return self._nome
    
    def categoria(self):
        return self._categoria
    
    def nome_categoria(self):
        return f'{self._nome} - {self._categoria}'
    
    @property
    def ativo(self):
        return "Ativo" if self._ativo else "Inativo"
   
    @classmethod
    def listar_restaurantes(cls):
        print(f'{"Nome do restaurante".ljust(30)} | {"Categoria".ljust(30)} | Status')
        for restaurante in cls.restaurantes: 
            print(f'{restaurante._nome.ljust(30)} | {restaurante._categoria.ljust(30)} | {restaurante.ativo}')

    def alternar_status(self):
        self._ativo = not self._ativo
        return f'O restaurante {self._nome} está agora {"Ativo" if self._ativo else "Inativo"}'

    def receber_avaliacao(self, cliente, nota):
        if 0 < nota <= 5:
            avaliacao = Avaliacao(cliente, nota)
            self._avaliacao.append(avaliacao)
            print(f'Nota {nota} Recebida com Sucesso!\n')
        else:
            return print("Nota inválida. A nota deve ser um número inteiro entre 1 e 5.\n")
        
    def ver_media_avaliacao(self):
        if not self._avaliacao:
            return "O restaurante ainda não recebeu avaliações."
        total_avaliacoes = len(self._avaliacao)
        soma_notas = sum(av._nota for av in self._avaliacao)
        media = soma_notas / total_avaliacoes
        return f'Média de avaliação: {media:.2f} com base em {total_avaliacoes} avaliações.'