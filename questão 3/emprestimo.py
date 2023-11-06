from datetime import datetime, timedelta

#função para ver se o funcionario tem direito ao emprestimo 
def adesão (nome, dt_adm, salario, emprestimo):

    data_atual = datetime.now()
    data_limite = data_atual - timedelta(days=365 * 5)

    #compara se o funcionario tem tempo de admissão superior a 5 anos
    if data_obj > data_limite:
        print(" Agradecemos seu interesse, mas você não atende os requisitos mínimos do programa.")
        exit()

    #compara se o emprestimo é maior que 2* o seu salario
    if emprestimo > 2*salario: 
        print(" Agradecemos seu interesse, mas você não atende os requisitos mínimos do programa.")
        exit()

    #compara se o valor do emprestimo é multiplo de 2
    if emprestimo %2 != 0:
        print("Insira um valor valido!\n")
        exit() 

    
def notas_maior_valor(): #função para imprimir notas de alto valor
    total= emprestimo
    ced = 100
    totalced = 0
    while True:
        if total >= ced:
            total -= ced
            totalced += 1
        else: 
            if totalced > 0:
                print(f"{totalced} X {ced} reais")
            if ced == 100:
                ced = 50
            elif ced == 50:
                ced = 20
            elif ced == 20:
                ced = 10
            elif ced == 10:
                ced = 5
            elif ced == 5:
                ced = 2
            totalced = 0
            if total == 0:
                break

def notas_menor_valor(): #função para imprimir notas de baixo valor
    total= emprestimo
    ced = 20
    totalced = 0
    while True:
        if total >= ced:
            total -= ced
            totalced += 1
        else: 
            if totalced > 0:
                print(f"{totalced} X {ced} reais")
            if ced == 20:
                ced = 10
            elif ced == 10:
                ced = 5
            elif ced == 5:
                ced = 2
            totalced = 0
            if total == 0:
                break

def notas_mistas(): #função p imprimir notas meio a meio
    total= emprestimo
    ced = 100
    totalced = 0
    while True:
        if total >= ced:
            total -= ced
            totalced += 1
        else: 
            if totalced > 0:
                print(f"{totalced} X {ced} reais")
            if ced == 100:
                ced = 20
            elif ced == 20:
                ced = 5
            elif ced == 10:
                ced = 5
            elif ced == 5:
                ced = 2
            totalced = 0
            if total == 0:
                break

def switch_case(opcao): #menu de escolha do usuario
    switcher = {
        1: notas_maior_valor,
        2: notas_menor_valor,
        3: notas_mistas
    }
    func = switcher.get(opcao, lambda: "Opção inválida")
    return func() 

#função principal

print("****************SIMULAÇÃO DE EMPRESTIMO*****************\n\n")

nome= input("Escreva seu nome: ")
dt_adm= input("Digite sua data de admissão (dd/mm/aaaa): ")
data_obj= datetime.strptime(dt_adm, "%d/%m/%Y")
salario= float (input("Informe seu salario atual: "))
emprestimo= int (input("Informe o valor do seu emprestimo: "))
adesão (nome, dt_adm, salario, emprestimo)
opcao = int(input("Escolha uma opção \n 1 - Notas de maior valor\n 2 - Notas de menor valor\n 3- Notas mistas\n > "))
switch_case(opcao)

