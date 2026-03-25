#Incio
def calculovelocidade(v1, v2, v3):
    DistanciaT = v1*v2
    TempoT = v3*60
    Velocidade = (DistanciaT/TempoT)*3.6
    return Velocidade
def main ():
    Voltas = int(input("Coloque o número de voltas:"))
    Distancia = float(input("Coloque a distância:"))
    Tempo = float(input("Coloque o tempo:"))
    Velocidade = calculovelocidade(Voltas, Distancia, Tempo)
    print ("Essa é a velocidade média",Velocidade)
if __name__ == "__main__":
    main()
#Fim