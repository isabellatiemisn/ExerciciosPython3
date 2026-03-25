import math
#Declarar
A:int = 0
B:int = 0
C:int = 0
Delta:int = 0
X1:float = 0.0
X2:float = 0.0
#Incio
def bhaskara():
    global X1, X2,B,A,C,Delta
    if (0<=Delta):
        if (0<Delta):
            X1 = (-B+(math.sqrt(Delta)))/(2*A)
            X2 = (-B-(math.sqrt(Delta)))/(2*A)
            print ("Esse é o valor das raízes:",X1,"e",X2)
        else:
            X1 = (-B/(2*A))
            print ("Esse é o valor da raiz:",X1)
    else:
        print("Não existem raízes reais")
def main():
    global X1, X2,B,A,C,Delta
    A = int(input("Digite um valor pra A:"))
    B = int(input("Digite um valor pra B:"))
    C = int(input("Digite um valor pra C:"))
    Delta = (B*B)-(4*A*C)
    bhaskara()
if __name__ == "__main__":
    main()
#Fim