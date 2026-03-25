#Declarar
Num1: int = 0
Num2: int = 0
#Incio
def ordemcrescente ():
    global Num1, Num2
    if(Num1>Num2):
        print("Números em ordem crescente:",Num2,"e",Num1)
    else:
        print("Números em ordem crescente:",Num1,"e",Num2)
def main ():
    global Num1, Num2
    Num1 = int(input("Digite um número:"))
    Num2 = int(input("Digite outro número:"))
    while (Num1==Num2):
        print ("Inválido, precisa de números diferentes")
        Num1 = int(input("Digite um número:"))
        Num2 = int(input("Digite outro número:"))
    ordemcrescente()
if __name__ == "__main__":
    main()
#Fim