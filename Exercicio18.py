#Declarar
Num1: int = 0
Num2: int = 0
Diferença: int = 0
#Incio
def operacao ():
    global Num1
    global Num2
    global Diferença
    if (Num1==Num2):
        print ("Números iguais, a diferença é 0")
    elif (Num1>Num2):
        Diferença = Num1 - Num2
        print("Essa é a diferença de",Num1,"-",Num2,"=",Diferença)
    else:
        Diferença = Num2 - Num1
        print("Essa é a diferença de",Num2,"-",Num1,"=",Diferença)
def main ():
    global Num1
    global Num2
    Num1 = int(input("Digite um número:"))
    Num2 = int(input("Digite outro número:"))
    operacao()
if __name__ == "__main__":
    main()
#Fim