''' =======================================
ESAMC -  Faculdade de Sorocaba
Programa de Introdução à Linguagem Python
Disciplina 	: Lógica de Progrmação e Algoritmos
Professor	: Francisco Tesifom Munhoz
Data	: 1º semestre de 2020
===========================================
Atividade	: Exercício 02
Autor	: João Marcelo Gerenutti
Data	: 29/04/2020
Comentários	: Resolução do exercício proposto durante a aula do dia 29/04/2020
 "O departamento que controla o índice de poluição do meio ambiente fiscaliza 3 grupos de indústrias que são altamente poluidoras do meio ambiente.
   O índice de poluição aceitável varia de 0.05 até 0.25.
    Se o índice sobe para 0.3 as indústrias do 1º grupo são intimadas a suspenderem suas atividades;
     se o índice sobe para 0.4, as do 1º e do 2º grupos são intimadas a suspenderem suas atividades;
      e se o índice sobe para 0.5, todos os três grupos devem ser notificados a paralisarem suas atividades.
       Escreva um programa em Python que lê o índice de poluição medido e emite a notificação adequada aos diferentes grupos de empresas."
============================================
'''


# ENTRADA DE DADOS
indicePoluicao=float(input("Digite o indice de poluição: "))


#PROCESSAMENTO DE DADOS/SAIDA DE DADOS
if(indicePoluicao >= 0.3 and indicePoluicao <= 0.39):
    print("Indústrias do 1º grupo devem suspender suas atividades, índice atual é de: %.2f" % indicePoluicao)
elif(indicePoluicao >= 0.4 and indicePoluicao <= 0.49):
    print("As indústrias do 1º e do 2º grupos devem suspender suas atividades, índice atual é de: %.2f" % indicePoluicao)
elif(indicePoluicao >= 0.5):
    print("Todos os três grupos devem paralisar suas atividades, índice atual é de: %.2f" % indicePoluicao)
else:
    print("O índice de %.2f de poluição é aceitável" % indicePoluicao)
