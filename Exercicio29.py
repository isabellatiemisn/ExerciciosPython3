#Incio
def investimento(V,T):
    if (T==1):
        ValorNovo = V*1.03
        print ("Esse é o valor acumulado em 30 dias:",ValorNovo)
    elif (T==2):
        ValorNovo = V*1.05
        print ("Esse é o valor acumulado em 30 dias:",ValorNovo)
def main ():
    Valor = float(input("Insira o valor do investimento:"))
    TipoInvestimento = int(input("Insira o tipo de investimento (1=Poupança ou 2=Renda Fixa):"))
    while(TipoInvestimento!=1 and TipoInvestimento!=2):
            print ("Inválido. Coloque um tipo adequado")
            TipoInvestimento = int(input("Insira o tipo de investido (1=Poupança ou 2=Renda Fixa):"))
    investimento(Valor,TipoInvestimento)
if __name__ == "__main__":
    main()
#Fim