#Declarar
InicioHora:int = 0
InicioMinuto:int = 0
FimHora:int = 0
FimMinuto:int = 0
TempoHora: float = 0
TempoMinuto: int = 0
#Incio
def tempojogo():
    global FimMinuto,FimHora,InicioHora,InicioMinuto,TempoHora,TempoMinuto
    InicioMinuto = (InicioHora*60)+InicioMinuto
    FimMinuto = (FimHora*60)+FimMinuto
    if (FimMinuto>=InicioMinuto):
        TempoHora = ((FimMinuto-InicioMinuto)//60)
        TempoMinuto = ((FimMinuto-InicioMinuto)%60)
        print("O tempo de jogo foi:",TempoHora,"horas e",TempoMinuto, "minutos")
    else:
        TempoHora = ((FimMinuto+1440)-InicioMinuto)//60
        TempoMinuto = ((FimMinuto+1440)-InicioMinuto)%60
        print("O tempo de jogo foi:",TempoHora,"horas e",TempoMinuto, "minutos")
def main ():
    global FimMinuto,FimHora,InicioHora,InicioMinuto,TempoHora,TempoMinuto
    InicioHora = int(input("Digite a hora de inicio do jogo:"))
    InicioMinuto = int(input("Digite o minuto de inicio do jogo:"))
    FimHora = int(input("Digite a hora de fim do jogo:"))
    FimMinuto = int(input("Digite o minuto de fim do jogo:"))
    tempojogo()
if __name__ == "__main__":
    main()
#Fim