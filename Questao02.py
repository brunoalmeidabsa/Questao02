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
questao()       
