from models.calcular import Calcular


def main() -> None:
    pontos: int = 0
    jogar(pontos)


def jogar(pontos: int) -> None:
    dificuldade: int = int(input('Informe o nível de dificuldade desejado (1, 2, 3, 4): '))

    calc: Calcular = Calcular(dificuldade)

    print('Informe o resultado para a seguinte operação:')
    print(calc.mostrar_operacao())

    resultado: int = int(input())

    if calc.checar_resultado(resultado):
        pontos += 1
        print(f'Você tem {pontos} ponto(s).')

    continuar: int = int(input('Deseja continuar no jogo? [1 - Sim, 0 - Não]: '))

    if continuar:
        jogar(pontos)
    else:
        print(f"\033[1;97mVocê finalizou com {pontos} ponto(s).\033[m")
        print('\033[1;97mAté a próxima!\033[m')


if __name__ == '__main__':
    main()
