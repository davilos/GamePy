from random import randint
from typing import Union


class Calcular:

    def __init__(self, dificuldade: int, /) -> None:
        self.__dificuldade: int = dificuldade
        self.__valor1: int = self._gerar_valor
        self.__valor2: int = self._gerar_valor
        self.__operacao: int = randint(1, 3)  # 1 = somar, 2 = subtrair,
        # 3 = multiplicar
        self.__resultado: int = self._gerar_resultado

    @property
    def dificuldade(self) -> int:
        return self.__dificuldade

    @property
    def valor1(self) -> int:
        return self.__valor1

    @property
    def valor2(self) -> int:
        return self.__valor2

    @property
    def operacao(self) -> int:
        return self.__operacao

    @property
    def resultado(self) -> int:
        return self.__resultado

    @property
    def _gerar_valor(self) -> int:
        if self.dificuldade == 1:
            return randint(0, 20)
        elif self.dificuldade == 2:
            return randint(0, 100)
        elif self.dificuldade == 3:
            return randint(0, 1000)
        elif self.dificuldade == 4:
            return randint(0, 10000)
        else:
            return randint(0, 100000)

    @property
    def _gerar_resultado(self) -> int:
        if self.operacao == 1:
            return self.valor1 + self.valor2
        elif self.operacao == 2:
            return self.valor1 - self.valor2
        return self.valor1 * self.valor2

    def checar_resultado(self, resposta: int) -> Union[bool, str]:
        if self._gerar_resultado == resposta:
            print('Resposta correta!')
            return True
        print('Resposta errada!')
        # '{self.valor1} + {self.valor2} = ' + resultado
        return (rsp := f'{self.mostrar_operacao()[:-1] + str(self.resultado)}')

    def mostrar_operacao(self) -> str:
        if self.operacao == 1:
            return f'{self.valor1} + {self.valor2} = ?'
        elif self.operacao == 2:
            return f'{self.valor1} - {self.valor2} = ?'
        else:
            return f'{self.valor1} * {self.valor2} = ?'

    def __str__(self) -> str:
        op: str = ''
        if self.operacao == 1:
            op = 'Somar'
        elif self.operacao == 2:
            op = 'Subtrair'
        elif self.operacao == 3:
            op = 'Multiplicar'
        else:
            op = 'Operação desconhecida'

        return f'Valor 1: {self.valor1}\nValor 2: {self.valor2}\nDificuldade: {self.dificuldade}\nOperação: {op}'
