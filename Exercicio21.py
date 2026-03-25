#Declarar
Nota1:float = 0.0
Nota2:float = 0.0
Nota3:float = 0.0
Nota4:float = 0.0
MédiaFinal:float = 0.0
#Incio
def calculonota ():
    global Nota1,Nota2,Nota3,Nota4,MédiaFinal
    if (MédiaFinal>=6.0):
        print("Aprovado. Média:",MédiaFinal)
    elif (MédiaFinal<3.0):
        print("Retido. Média:",MédiaFinal)
    else:
        print("Exame. Média:",MédiaFinal)
def main ():
    global Nota1,Nota2,Nota3,Nota4,MédiaFinal
    Nota1 = float(input("Digite a nota 1:"))
    Nota2 = float(input("Digite a nota 2:"))
    Nota3 = float(input("Digite a nota 3:"))
    Nota4 = float(input("Digite a nota 4:"))
    MédiaFinal = ((Nota1+Nota2+Nota3+Nota4)/4)
    calculonota ()
if __name__ == "__main__":
    main()
#Fim