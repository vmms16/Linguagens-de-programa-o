class Veiculo:
    def __init__(self):
        self._numero_rodas=None

    def getNumeroRodas(self):
        return self._numero_rodas

    def setNumeroRodas(self, quantidade):
        self._numero_rodas=quantidade

    def printNumeroRodas(self):
        print("Seu veiculo tem %d roas"%(self._numero_rodas))

class Carro(Veiculo):
    def __init__(self):
        Veiculo.__init__(self)
        self._numero_rodas=4

class Moto(Veiculo):
    def __init__(self):
        Veiculo.__init__(self)
        self._numero_rodas=2


def main():
    while True:
        print("____________________________________________________")
        veiculo = input("Qual o tipo do seu veiculo?\n1-Carro\n2-Moto\nTipo: ")

        if veiculo == str(1):
            carro=Carro()
            carro.printNumeroRodas()
            break
        elif veiculo == str(2):
            moto=Moto()
            moto.printNumeroRodas()
            break
        else:
            print("Indique um veiculo valido")

        print("____________________________________________________")

if __name__=="__main__":
    main()