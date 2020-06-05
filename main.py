"""
Módulo com funções e classes para o funcionamento da aplicação

Example:
    ```console
    $ python main.py
    ```

Todo:
    * Finalizar a classe Pessoa
"""

VERSAO = '0.8'
"""Representa a versão deste módulo"""


def mensagem(nome: str):
    """Cumprimenta o utilizador com uma mensagem de boas-vindas

    Args:
        nome (str): O nome do utilizador a cumprimentar

    Returns:
        Uma mensagem de boas-vindas com o nome do utilizador
    """
    mensagem = "Olá {nome}!"
    return mensagem


def soma(num_1: int, num_2: int):
    """Calcula a soma de dois números

    Args:
        num_1 (int): O primeiro número
        num_2 (int): O segundo número
    """
    return num_1 + num_2


class Pessoa:
    """Representa uma pessoa

    Attributes:
        nome (str): O nome da pessoa
        idade (int): A idade da pessoa
    """

    def __init__(self, nome: str, idade: int):
        self.nome = nome
        self.idade = idade

    def dados(self):
        """Mensagem com dados da pessoa instanciada

        Returns:
            Uma mensagem com os dados da pessoa (`nome` e `idade`).
        """
        return f"A pessoa com o nome {self.nome} tem {self.idade} anos."
