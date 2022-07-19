def palindromo(palabra):
    palabra = palabra.replace(' ', '')
    palabra = palabra.lower()
    palabra_invertida = palabra[::-1]
    if palabra == palabra_invertida:
        return True
    else:
        return False


def capicua(numero):
    numero = numero.replace(' ', '')
    numero_invertida = numero[::-1]
    if numero == numero_invertida:
        return True
    else:
        return False


def run():
    menu = int(input('''Este programa detecta \U0001f50e palíndromos y capicúas, que quieres hacer

1- Palíndromos - Palabras \U0001f524
2- Capicúas - Números \U0001f522

Elige una opción: '''))
    if menu == 1:
        palabra = input('Escribe una palabra: ')
        es_palindromo = palindromo(palabra)
        if es_palindromo == True:
            print(palabra + ' \u2705 Es palíndromo')
        else:
            print(palabra + ' \u274E No es palíndromo')
    elif menu == 2:
        numero = input('Escribe una numero: ')
        es_capicua = capicua(numero)
        if es_capicua == True:
            print(numero + ' \u2705 Es capicúa')
        else:
            print(numero + ' \u274E No es capicúa')
    else:
        print('Introduce una opción válida')
        return run()


if __name__ == "__main__":
    run()