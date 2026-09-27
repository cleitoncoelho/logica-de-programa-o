def calcula_desconto(preco, desconto=10):
    preco_final = preco - (preco * desconto / 100)
    return preco_final

print(calcula_desconto(100))
print(calcula_desconto(100, 20))
print(calcula_desconto(200, 50))