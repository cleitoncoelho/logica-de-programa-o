def divisao_segura(a,b):
    try:
        return a / b
    except ZeroDivisionError:
        return 'Não é possível dividir por zero'

print(divisao_segura(10, 2))   
print(divisao_segura(10, 0)) 