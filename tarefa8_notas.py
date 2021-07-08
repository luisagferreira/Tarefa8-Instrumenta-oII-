# Luísa Gonçalves Ferreira
nota1=float(input("Digite a primeira nota do aluno: "))
while nota1<1 or nota1>10:
    print("Nota inválida!")
    nota1 = float(input("Digite novamente a primeira nota do aluno: "))
    break
nota2=float(input("Digite a segunda nota do aluno: "))
while nota2<1 or nota2>10:
    print("Nota inválida!")
    nota2 = float(input("Digite novamente a segunda nota do aluno: "))
    break
nota3 = float(input("Digite a terceira nota do aluno: "))
while nota3<1 or nota3>10:
    print("Nota inválida!")
    nota3= float(input("Digite novamente a terceira nota do aluno: "))
    break
faltas = float(input("Digite o número de faltas: "))
while faltas<1 or faltas>60:
    print("Nota inválida!")
    faltas = float(input("Digite novamente as faltas do aluno: "))
    break

nota= (nota1+nota2+nota3)/3
if nota >=6 and faltas <=15:
    print("Aluno aprovado!")
    print("BOLETIM:")
    print('- Média: {} '.format(nota))
    print('- Faltas: {} '.format(faltas))

if nota >=4 and nota<6 and faltas <=15:
    print("Aluno em recuperação!")
    print("BOLETIM:")
    print('- Média: {}'.format(nota))
    print('- Faltas: {} '.format(faltas))

if nota <4 or faltas >15:
    print("Aluno reprovado!")
    print("BOLETIM:")
    print('- Média: {}'.format(nota))
    print('- Faltas: {} '.format(faltas))
