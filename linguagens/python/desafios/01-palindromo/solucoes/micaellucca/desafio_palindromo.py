word = input("verificador de palindromo: ").strip().lower()
reverse_word = word[::-1]

if word == reverse_word:
    print(f"a palavra {word} é um palíndromo")
else:
    print("NÃO É UM PALINDROMO")
