import datetime

# Função para obter o mês atual
def obter_mes_atual():
    return datetime.datetime.now().month

#função para encontrar os aniversariantes do mês
def ler_arquivo(arq, mes_atual):

    aniversariantes = []

    with open(arq, "r") as f: 

     for linha in f: 
       nome, email, dt_nasc = linha.strip().split('|')
       dia, mes, _ = map(int, dt_nasc.split('/'))

       if mes == mes_atual:
          aniversariantes.append((nome, email, dt_nasc))
    
    return aniversariantes
    arq.close()

def criar_arq(aniversariantes):
    niver= f'aniversariantes_{datetime.datetime.now().strftime("%Y%m")}.txt'

    with open(niver, 'w') as f:
       for aniversariantes in aniversariantes:
          f.write('|'. join(aniversariantes) + '\n')

    return niver

arq_funcionarios = 'questão 2/funcionarios.txt'

mes_atual = obter_mes_atual()

aniversariantes = ler_arquivo(arq_funcionarios, mes_atual)

arq_aniversariantes = criar_arq(aniversariantes)

print(f"\n**Arquivo de aniversariantes gerado: {arq_aniversariantes}")