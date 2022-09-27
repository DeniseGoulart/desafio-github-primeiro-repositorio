primeira_nota = float(input("Informe a primeira nota: "))
segunda_nota = float(input("Informe a segunda nota: "))
terceira_nota = float(input("Informe a terceira nota: "))

soma = primeira_nota + segunda_nota + terceira_nota
media = soma / 3

if media >= 7:
    print(f"Aluno aprovado com {media:.1f}! Boas férias!!!")
elif media >= 5:
    print(f"Aluno em recuperação com {media:.1f}! Estude, você tem mais uma chance!")
else:
    print(f"Aluno reprovado com {media:.1f}! Nos vemos de novo ano que vem!")