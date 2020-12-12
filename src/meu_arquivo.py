""" Documento de teste para aula """


def minha_funcao():
    """ Apresentar uma mensagem """

    print("Ola Mundo!")


def somatorio(num1: int, num2: int) -> int:
    """Retorna a soma entre dois numeros
    :param  - num1: numero inteiro 1
            - num2: numero inteiro 2
    :return - Soma entre dois numeros"""

    resposta = num1 + num2
    return resposta


minha_funcao()
somatorio(2, 4)
