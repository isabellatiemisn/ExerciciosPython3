#Declarar
Num1: float = 0.0
Num2: float = 0.0
#Incio
def comparacao():
    global Num1
    global Num2
    if (Num1==Num2):
        print("Inválido, não há maior valor")
    elif (Num1>Num2):
        print("Esse é o maior valor:",Num1)
    else:
        print("Esse é o maior valor:",Num2)
def main():
    global Num1
    global Num2
    Num1 = float(input("Digite um número:"))
    Num2 = float(input("Digite outro número:"))
    comparacao()
if __name__ == "__main__":
    main()
#Fim