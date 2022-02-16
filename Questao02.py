def diferenca_salario (salario, media_salario):
    resultado = (((salario - media_salario)/salario)*100)
    return round(resultado, 2)