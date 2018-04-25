while True:
    print("____________________________________________________")
    veiculo=input("Qual o tipo do seu veiculo?\n1-Carro\n2-Moto\nTipo: ")

    if veiculo==str(1):
        print("Seu carro tem 4 rodas")
        break
    elif veiculo==str(2):
        print("Sua moto tem 2 rodas")
        break
    else:
        print("Indique um veiculo valido")

    print("____________________________________________________")
