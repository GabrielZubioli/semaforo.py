import time

def cadastroCores():
    cores = []
    print("Cadastro das cores")
    while len(cores) < 3:
        cor = str(input(f"Insira a {len(cores)+1}° cor (sem repetir):").strip().lower())
        if cor in cores:
            print("Cor ja existente, Insira a cor novamente")
        elif cor == "":
            print("Invalido, Insira a cor novamente")
        else:
            cores.append(cor)
    return cores

def cadastroTempo(cores):
    tempos = {}
    print("Cadastro de tempo em segundos")
    for cor in cores:
        while True:
            try:
                tempo = int(input(f"Informe o tempo para a cor '{cor}': "))
                if tempo <= 0:
                    print("O tempo deve ser maior que zero. Tente novamente.")
                else:
                    tempos[cor] = tempo
                    break
            except ValueError:
                print("Valor inválido. Digite um número inteiro.")
    return tempos

def iniciar_semaforo(cores, tempos):
    print("\nIniciando o semáforo. Pressione CTRL+C para encerrar.\n")
    try:
        while True:
            for cor in cores:
                print(f"{cor.upper()} - ({tempos[cor]}s)")
                time.sleep(tempos[cor])
    except KeyboardInterrupt:
        print("\nSemáforo encerrado manualmente.")

def main():
    print("Sistema de Semáforo\n")
    cores = cadastroCores()
    tempos = cadastroTempo(cores)

    while True:
        iniciar = input("\nDeseja iniciar o semáforo? (sim/não): ").strip().lower()
        if iniciar == "sim":
            iniciar_semaforo(cores, tempos)
            break
        elif iniciar == "não":
            print("Programa encerrado.")
            break
        else:
            print("Resposta inválida. Digite 'sim' ou 'não'.")

if __name__ == "__main__":
    main()