#Declarar
Num1:int = 0
Num2:int = 0
#Incio
def multiplos():
    global Num1,Num2
    if (Num1>Num2):
        if ((Num1%Num2)==0):
            print (Num1,"é múltiplo de",Num2)
        else:
            print (Num1,"não é múltiplo de",Num2)
    else:
        if ((Num2%Num1)==0):
            print (Num2,"é múltiplo de",Num1)
        else:
            print (Num2,"não é múltiplo de",Num1)
def main():
    global Num1,Num2
    Num1 = int(input("Digite um número:"))
    Num2 = int(input("Digite outro número:"))
    while(Num1==Num2):
            print ("Inválido, valores iguais, não há maior valor")
            print ("Tente novamente")
            Num1 = int(input("Digite um número:"))
            Num2 = int(input("Digite outro número:"))
    multiplos()
if __name__ == "__main__":
    main()
#Fim