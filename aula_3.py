# ### 1 - Crie um programa para efetuar a leitura de um número inteiro e apresentar o resultado do quadrado deste número. (O correto é criar uma variavel "quadrado para colocar a conta")
#  num = int(input("Digite um numero inteiro: "))
#  quadrado = num * num
#  print(quadrado)

# ### 1.1
#  num = int(input("Digite um numero inteiro: "))
#  calc = num * num 
#  print("O quadrado de {} é {}" .format(num,calc))

# ### 2 Crie duas variáveis para armazenar seu primeiro nome e sobrenome. Em seguida, concatene-as para formar seu nome completo e exiba o resultado.
#  nome1 = "Rafael"
#  nome2 = "Dip"
#  print(nome1 , nome2)

# ### 2.1
# nome = input("Digite o seu primeiro nome: ")
# nome2 = input("Digite o seu sobrenome: ")
# print(nome,nome2)

### 3 - Peça ao usuário para digitar dois números inteiros e armazene-os em variáveis. Realize a concatenação desses números como strings e exiba o resultado.
# num = int(input("Digite o primeiro número inteiro: "))
# num2 = int(input("Digite o segundo número inteiro: "))
# print(num,"e", num2)

### 4 - Crie uma variável para armazenar a palavra "Python". Em seguida, adicione um número inteiro ao final da palavra usando a concatenação e exiba o resultado.
# palavra = "Python"
# num = input("Digite um número inteiro:")
# print(palavra + num)

# palavra = "Python"
# num = input("Digite um número inteiro: ")
# resultado = palavra + num
# print(resultado)

### 5 - Declare uma variável contendo uma frase. Em seguida, peça ao usuário para digitar uma palavra e concatene essa palavra no final da frase. Exiba o resultado.

# frase = "Olá mundo ou Hello world"
# palavra = input("Senhor usuário, digite uma palavra: ")
# print(frase,palavra)

### 6 -Crie três variáveis para armazenar a quantidade de horas, minutos e segundos. Concatene esses valores para formar uma mensagem de tempo no formato "hh:mm:ss".

# hr = input("Digite as horas: ")
# min = input("Digite os minutos: ")
# sec = input("Digite os segundos: ")
# print(hr + ":" + min + ":" + sec)

### 7 - Declare duas variáveis com números de telefone, incluindo um código de área e o número principal. Concatene esses valores para formar um número de telefone completo.**
# n1 = 942088002
# n2 = 991521417
# cod_area = int(input("Digite o seu codigo de area: "))
# print(cod_area,n1)
# print(cod_area,n2)

### 8 - Crie uma lista de ingredientes para uma receita. Use concatenação para formar uma única string que liste os ingredientes separados por vírgulas.**
# ingrediente1 = input("Digite aqui o primeiro ingrediente: ")
# ingreditente2 = input("Digite aqui o segundo ingrediente: ")
# ingreditente3 = input("Digite aqui o terceiro ingrediente: ")
# receita = (ingrediente1 + "," + ingreditente2 + "e" + ingreditente3)
# print(receita)

### 9 - Peça ao usuário para digitar três adjetivos e armazene-os em variáveis. Em seguida, use essas palavras para criar uma frase concatenada que descreve algo interessante.
# adj1 = input("Digite o primeiro adjetivo: ")
# adj2 = input("Digite o segundo adjetivo: ")
# adj3 = input("Digite o terceiro adjetivo: ")
# frase = ("Você é muito " + adj1 + " e tem " + adj2 + " e parece que é," +adj3)
# print(frase)

# ATIVIDADE 3 → IF()
### 1 - Crie uma condição para comparar idades: 45 e 18 -  QUAL É MENOR E QUAL É MAIOR?**
# idade1 = int(input("Digite a idade da primeira pessoa: "))
# idade2 = int(input("Digite a idade da segunda pessoa: "))
# if (idade1 > idade2):
#     print("A primeira pessoa é mais velha que a segunda pessoa!")
# else:
#         print("A segunda idade é maior!")

### 2 - Crie um sistema para permitir a verificação de menores em um show**
# meliante1 = int(input("Digite aqui a sua idade: "))
# if (meliante1 < 18):
#       print("Você é menor de idade para chapar o globo, volte para casa pivete!")
# else:
#         print("Seja bem vindo ao nosso evento, beba com moderação!")


### 3 - Crie um algoritmo que permita a entrada de 3 notas de alunos, utilize o bloco de código if() para verificar se o aluno passou.

# n1 = int(input("Digite a nota da prova do primeiro aluno: "))
# if (n1 >= 7):
#     print("Aluno foi aprovado, parabéns!")
# else:
#         print("Aluno foi reprovado, estude mais!")

# n2 = int(input("Digite a nota da prova do segundo aluno: "))
# if (n2 >= 7):
#     print("Aluno foi aprovado, parabéns!")
# else:
#         print("Aluno foi reprovado, estude mais!")

# n3 = int(input("Digite a nota da prova do terceiro aluno: "))
# if (n3 >= 7):
#     print("Aluno foi aprovado, parabéns!")
# else:
#         print("Aluno foi reprovado, estude mais!")
