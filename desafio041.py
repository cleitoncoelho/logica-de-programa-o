def eh_palindromo(palavra):

    return palavra == palavra[::-1]


print(eh_palindromo('arara'))
print(eh_palindromo('python'))
