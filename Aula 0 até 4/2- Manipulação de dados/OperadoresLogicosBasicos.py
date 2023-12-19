# print("nascimento : ")
# print(nascimento)
# print("E-mail : ")
# print(email)
# a= int(input("Digite um número: "))
# print (a+5)

# 1a Cat: Ariméticos
# # + - * /
# 2a Cat: Relacionais
# # >  <  >=  <=  ==  !=  ===
# 3a Cat: Lógicos
# !
# &&
# ||
#MAIORIDADE = 18
#idade = int(input("Qual a sua idade?"))



ano_nascimento = int(input('Digite seu ano de nascimento: '))
ano_atual = int(input('Digite o ano atual: '))
idade = ano_atual - ano_nascimento

if idade >= 18:
    titulo_eleitor = int(input('Digite seu titulo de eleitor: '))
else:
    doc_responsavel = int(input('Digite o documento do responsavel: '))
