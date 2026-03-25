#Declarar
Num1: int = 0
Num2: int = 0
Num3: int = 0
Num4: int = 0
#Incio
def comparacoes():
    global Num1,Num2,Num3,Num4
    if (Num4<Num1):
        print(Num4,Num1,Num2,Num3)
    elif (Num4<Num2):
        print(Num1,Num4,Num2,Num3)
    elif (Num4<Num3):
        print(Num1,Num2,Num4,Num3)
    else:
        print(Num1,Num2,Num3,Num4)
def main():
    global Num1,Num2,Num3,Num4
    Num1 = int(input("Digite um número:"))
    Num2 = int(input("Digite um número maior que o anterior:"))
    Num3 = int(input("Digite um número maior que o anterior:"))
    Num4 = int(input("Digite um número qualquer:"))
    comparacoes()
if __name__ == "__main__":
    main()
#Fim