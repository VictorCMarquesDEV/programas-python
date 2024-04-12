frase = 'Curso em Vídeo Python'
frasespace = '   Aprenda Python  '
fraseseparada = ['Curso', 'em', 'Vídeo', 'Python']
print(frase)

# Fatiamento
print(frase[9])  # Apenas o char 9
print(frase[9:13])  # 9 até o 12 -> Um a menos no final
print(frase[9:21])  # 9 até o 20
print(frase[9:21:2])  # 9 até 20 pulando de 2 em 2
print(frase[:5])  # 0 até o 4
print(frase[15:])  # 15 até o final
print(frase[9::3])  # 9 até o final pulando de 3 em 3

# Análise
print(len(frase))  # Comprimento da string
print(frase.count('o'))  # Contar quantas vezes aparece o 'o'
print(frase.count('o', 0, 13))  # Contar quantas vezes aparece o 'o' do 0 até o 12
print(frase.find('deo'))  # Em que lugar encontrou 'deo' pela primeira vez
print(frase.find('Android'))  # Se não encontra, retorna -1
print('Curso' in frase)  # Verifica se existe. Retorna True ou False

# Transformação
print(frase.replace('Python', 'Android'))  # Substitui as palavras, apenas neste print
print(frase.upper())  # Os char ficam em maiúsculo
print(frase.lower())  # Os char ficam em minúsculo
print(frase.capitalize())  # Apenas o primeiro char fica em maiúsculo
print(frase.title())  # O primeiro char de cada palavra fica em maiúsculo
print(frasespace)
print(frasespace.strip())  # Remove todos os espaços inúteis
print(frasespace.rstrip())  # Remove todos os espaços inúteis da direita
print(frasespace.lstrip())  # Remove todos os espaços inúteis da esquerda

# Divisão
print(frase.split())  # Divide a string em strings para cada palavra

# Junção
print(' '.join(fraseseparada))  # Juntar as strings

print("""Texto é uma produção, verbal ou não verbal, 
que se constitui com algum código, 
no intuito de comunicar algo a alguém, 
em determinado tempo e espaço. 
Sua definição ampla se deve ao fato 
de também abranger diversos formatos.""")

dividido = frase.split()
print(dividido[0])  # Palavra na posição 0
print(dividido[0][4])  # Letra 4 na palavra na posição 0
