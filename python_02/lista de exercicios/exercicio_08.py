# Exercício 8 - listagem de nomes de alunos 
print("=====ALUNOS=====")
print(" ")

# Array das lojas 
nomes = ["Carol", "Esther", "Isabela", "Lívia", "Pedro"]

# # Exibindo Lojas
# for i, nomes in enumerate(nomes,1):
#     print(f"{i} = {nomes}")
#     print(" ")

contador = 1 
for nome in nomes:
    print(f"{contador}. {nome}")
    contador +=1

