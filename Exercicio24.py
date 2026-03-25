#Declarar
Valor:int = 0
#Incio
def divisao():
    global Valor
    if (Valor%2==0 and Valor%3==0):
        print("É divísivel por 2 e 3")
    elif (Valor%2==0):
        print("É divisivel apenas por 2")
    elif (Valor%3==0):
        print("É divisivel apenas por 3")
    else:
        print("Não é divisivel nem por 2 nem por 3")
def main ():
    global Valor
    Valor = int(input("Digite um número para descobrir se é divísivel por 2 e 3:"))
    divisao()
if __name__ == "__main__":
    main()
#Fim