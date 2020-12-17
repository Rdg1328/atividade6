
numeros = ("zero", "um", "dois", "três", "quatro", "cinco", "seis", "sete", "oito", "nove")
while True:
	escolha = int(input("Escolha um número entre 0 e 9: "))
	if escolha >= 0 and escolha <= 9:
		break
print(f"Você escolheu o número {numeros[escolha]}")

