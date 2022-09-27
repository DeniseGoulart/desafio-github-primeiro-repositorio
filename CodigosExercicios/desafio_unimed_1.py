
#distancia_entre_paladir = int(input("Informe a distancia entre os paladirs: "))
#diametro_paladir_Sauron = int(input("Informe o diâmetro do paladir de Sauron: "))
#diametro_paladir_Saruman = int(input("Informe o diâmetro do paladir de Saruman: "))

#while (distancia_entre_paladir <= 0) or (distancia_entre_paladir >= 10000) or (diametro_paladir_Sauron <= 0) or (diametro_paladir_Saruman <= 0) or (diametro_paladir_Saruman >= 100):
#    if (distancia_entre_paladir <= 0) or (distancia_entre_paladir >= 10000):
#        print("Informe um valor válido para a distância entre os paladirs! Este valor deve ser entre 0 e 10000!\n")
#        distancia_entre_paladir = int(input("Informe a distancia entre os paladirs: "))
#    elif (diametro_paladir_Sauron <= 0):
#        print("Informe um valor válido para o diâmetro do paladir de Sauron! Este valor deve ser entre 0 e 200!\n")
#        diametro_paladir_Sauron = int(input("Informe o diâmetro do paladir de Sauron: "))
#    elif (diametro_paladir_Saruman <= 0) or (diametro_paladir_Saruman >= 100):
#        print("Informe um valor válido para o diâmetro do paladir de Saruman! Este valor deve ser maior do que 0!\n")
#        diametro_paladir_Saruman = int(input("Informe o diâmetro do paladir de Saruman: "))

#print()

#soma_diametros = diametro_paladir_Sauron + diametro_paladir_Saruman
#icm = float(distancia_entre_paladir / soma_diametros)

#print(f"O ICM calculado é de: {icm:.2f}")

entrada = input("Informe os valores (distancia, diametro 1 e diametro 2): ").split()

distancia = int(entrada[0])
diametro1 = int(entrada[1])
diametro2 = int(entrada[2])

while (distancia <= 0) or (distancia > 10000) or (diametro1 <= 0) or (diametro2 <= 0) or (diametro2 > 100):
    entrada = input("Informe os valores (distancia, diametro 1 e diametro 2): ").split()

    distancia = int(entrada[0])
    diametro1 = int(entrada[1])
    diametro2 = int(entrada[2])
    
print()

soma_diametros = diametro1 + diametro2
icm = float(distancia / soma_diametros)

print(f"O ICM calculado é de: {icm:.2f}")

