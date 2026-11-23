frase = "Programação em Python".lower()
vogais = sum(1 for letra in frase if letra in "aeiouáéíóúãõ")
print(f"Total de vogais: {vogais}")