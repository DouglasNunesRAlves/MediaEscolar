print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
print("              E S C O L A   C O N Q U I S T E   S U A  V A G A              ")
print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
print("                        C Ó D I G O   T O D O   D I A                       ")
print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")

print("VAMOS VERIFICAR SE VOCE FOI APROVADO OU REPROVADO" "\n")
nome=input("POR FAVOR, DIGITE SEU NOME PARA QUE EU POSSA VERIFICAR: ")
turma=input("AGORA, DIGITE SUA SÉRIE: ")

print("\n""Olá",nome, ".\n""Vejo que voce é da",turma,"ª série, agora vamos verificar suas notas." "\n")
nota1 = int(input("digite a primeira nota: -> "))
nota2 = int(input("digite a segunda nota: -> "))
nota3 = int(input("digite a terceira nota: -> "))
nota4 = int(input("digite a quarta nota: -> "))
media= ((nota1+nota2+nota3+nota4) /4)
print(media)
if media < 4:
     print('VOCE FOI REPROVADO, SUA MÉDIA FINAL É DE',media,".\nTE VEJO NOVAMENTE ANO QUE VEM.")
elif media <= 6:
     print('VOCE NÃO ATINGIU A NOTA MÍNIMA. VOCE ESTA DE RECUPERAÇÃO, SUA NOTA FINAL FOI DE',media,".")
else:
     print("MEUS PARABÉNS, VOCE FOI APROVADO. SUA NOTA FINAL FOI DE:",media)
