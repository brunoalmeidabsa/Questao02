def diferenca_salario (salario, media_salario):
    resultado = (((salario - media_salario)/salario)*100)
    return round(resultado, 2)

def questao():
    i = 0
    n = 2
    empregados = []
    while (i < n):
        informacoes = []
        nome = str(input('Digite o nome da {} pessoa: '.format(i+1))).strip
        sexo = str.upper(input('Digite o sexo da {} pessoa [M/F]: '.format(i+1))).strip
        salario = float(input('Digite o salário da {} pessoa: R$ '.format(i+1)))
        informacoes.append(nome)
        informacoes.append(sexo)
        informacoes.append(salario)
        empregados.append(informacoes)
        i+=1

    soma_salario = 0
    for j in range(n):
        soma_salario += empregados[j][2]
    media_salario = soma_salario/n

    for k in range(n):
        empregados[k].append(f'{diferenca_salario(empregados[k][2],media_salario)} %')

    indice_maior_salario = 0
    maior_salario = empregados[0][2]

    for m in range(n):
        if(maior_salario < empregados[m][2]):
            maior_salario = empregados[m][2]
            indice_maior_salario = m

    print("{:<8} {:<15} {:<10} {:<15}".format("Nome","Sexo","Salário","Diferença Percentual"))
questao()       
