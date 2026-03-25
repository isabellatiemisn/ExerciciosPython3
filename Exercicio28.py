#Incio
def calculovendas(VM,PA):
    if (VM<500 and PA<30):
        PrecoNovo = PA*1.1
        print("Esse é o novo valor do produto:", PrecoNovo)
    elif (1000>VM>=500 and 80>PA>=30):
        PrecoNovo = PA*1.15
        print("Esse é o novo valor do produto:", PrecoNovo)
    elif (VM>=1000 and PA>=80):
        PrecoNovo = PA*0.95
        print("Esse é o novo valor do produto:", PrecoNovo)
    else:
        print("Não haverá mudança de preço. Preço atual:",PA)
def main():
    VendaMensal = int(input("Digite o número de vendas mensais:"))
    PrecoAtual = float(input("Digite o preço atual do produto:"))
    calculovendas (VendaMensal,PrecoAtual)
if __name__ == "__main__":
    main()
#Fim