def eh_palindromo(texto):
    texto = ''.join(c.lower() for c in texto if c.isalnum())
    return "Sim" if texto == texto[::-1] else "Não"

print(eh_palindromo("A cara rajada da jararaca")) 
print(eh_palindromo("Python"))    