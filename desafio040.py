def eh_primo(n):
    primo = True

    if n > 1:
        for i in range(2, n):
            if n % i == 0:
                primo = False

        return primo
    else:
        return False


print(eh_primo(7))
print(eh_primo(8))
print(eh_primo(1))

