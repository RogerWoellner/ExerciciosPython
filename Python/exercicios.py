Exercício Vetor

N = int(input("Quantos números você vai digitar?: "))
vet = [0 for x in range(N)]

soma = 0

for i in range(0, N):
    vet[i] = float(input("Digite um número: "))
    soma = soma + vet[i]
    media = soma / N

print()

print("VALORES = ", end="")
for i in range(0, N):
    print(f"{vet[i]:.1f} ", end="")

print()

print(f"SOMA = {soma:.2f}")
print(f"MEDIA = {media:.2f}")


Exercício matriz

N = int(input("Qual a ordem da matriz?: "))
mat = [[0 for x in range(N)] for x in range(N)]

for i in range(0, N):
    for j in range(0, N):
        mat[i][j] = int(input(f"Elemento [{i},{j}]: "))

print("Diagonal principal:")
for i in range(0, N):
    print(f"{mat[i][i]} ", end="")
print()

cont = 0

for i in range(0, N):
    for j in range(0, N):
        if mat[i][j] < 0:
            cont = cont + 1
print(f"Quantidade de negativos = {cont}")


Problema "terreno" Fazer um programa para ler as medidas da largura e comprimento de um terreno retangular com uma casa decimal, bem como o valor do metro quadrado do terreno com duas casas decimais. Em seguida, o programa deve mostrar o valor da área do terreno, bem como o valor do preço do terreno, ambos com duas casas decimais, conforme exemplo.  

larg = float(input("Digite a largura do terreno: "))
comp = float(input("Digite o comprimento do terreno: "))
valor = float(input("Digite o valor do metro quadrado: "))

print()

area = larg * comp
preco = area * valor

print(f"Area do terreno = {area:.2f}")
print(f"Preço do terreno = R$ {preco:.2f}")

Problema "retangulo" 
Fazer um programa para ler as medidas da base e altura de um retângulo. Em seguida, mostrar o valor 
da área, perímetro e diagonal deste retângulo, com quatro casas decimais, conforme exemplos.

import math

base = float(input("Base do retangulo: "))
altura = float(input("Altura do retangulo: "))

print()

area = base * altura
P = 2 * (base + altura)
D = math.sqrt(base * base + altura * altura)

print(f"AREA = {area:.4f}")
print(f"PERIMETRO = {P:.4f}")
print(f"DIAGONAL = {D:.4f}")

Problema "idades" 
Fazer um programa para ler o nome e idade de duas pessoas. Ao final mostrar uma mensagem com os 
nomes e a idade média entre essas pessoas, com uma casa decimal, conforme exemplo. 

print("Dados da primeira pessoa: ")
nome1 = str(input("Nome: "))
idade1 = int(input("Idade: "))
print()
print("Dados da segunda pessoa: ")
nome2 = str(input("Nome: "))
idade2 = int(input("Idade: "))
print()

media = (idade1 + idade2) / 2

print(f"A idade média de {nome1} e {nome2} é de {media:.1f}.")


Problema "soma" 
Fazer um programa para ler dois valores inteiros X e Y, e depois mostrar na tela o valor da soma destes 
números. 

soma = 0

x = int(input("Digite o valor de X: "))
y = int(input("Digite o valor de Y: "))

print()

soma = x + y

print(f"SOMA = {soma}")


Problema "troco" 
Fazer um programa para calcular o troco no processo de pagamento de um produto de uma mercearia. 
O programa deve ler o preço unitário do produto, a quantidade de unidades compradas deste produto, 
e o valor em dinheiro dado pelo cliente (suponha que haja dinheiro suficiente). Seu programa deve 
mostrar o valor do troco a ser devolvido ao cliente.

preco = float(input("Preço unitário do produto: "))
qtde = int(input("Quantidade comprada: "))
dinheiro = float(input("Dinheiro recebido: "))

print()

total = preco * qtde

troco = dinheiro - total

print(f"TROCO = R$ {troco:.2f}")

Problema "circulo" 
Fazer um programa para ler o valor "r" do raio de um círculo, e depois mostrar o valor da área do 
círculo com três casas decimais. A fórmula da área do círculo é a seguinte: 𝑎𝑟𝑒𝑎 = 𝜋. 𝑟
ଶ
. Você pode 
usar o valor de 𝜋 fornecido pela biblioteca da sua linguagem de programação, ou então, se preferir, use 
diretamente o valor 3.14159.

raio = float(input("Digite o valor do raio do circulo: "))

area = 3.14159 * (raio ** 2)

print(f"AREA = {area:.3f}")


Problema "pagamento" 
Fazer um programa para ler o nome de um(a) funcionário(a), o valor que ele(a) recebe por hora, e a 
quantidade de horas trabalhadas por ele(a). Ao final, mostrar o valor do pagamento do funcionário com 
uma mensagem explicativa, conforme exemplo. 

nome = str(input("Nome: "))
valor = float(input("Valor por hora: "))
horas = int(input("Horas trabalhadas: "))

print()

total = valor * horas

print(f"O pagamento para {nome} deve ser de R$ {total:.2f}")

Problema "consumo" 
Fazer um programa para ler a distância total (em km) percorrida por um carro, bem como o total de 
combustível gasto por este carro ao percorrer tal distância. Seu programa deve mostrar o consumo 
médio do carro, com três casas decimais. 

distancia = float(input("Distancia percorrida: "))
combustivel = float(input("Combustível gasto: "))

print()

consumo = distancia / combustivel

print(f"Consumo médio = {consumo:.3f}")

Problema "medidas" 
Fazer um programa para ler três medidas A, B e C. Em seguida, calcular e mostrar (imprimir os dados 
com quatro casas decimais): 
a) a área do quadrado que tem lado A 
b) a área do triângulo retângulo que base A e altura B 
c) a área do trapézio que tem bases A e B, e altura C 

a = float(input("Digite a medida A: "))
b = float(input("Digite a medida B: "))
c = float(input("Digite a medida C: "))

print()

quadrado = a * a
triangulo = (a * b) / 2
trapezio = ((a + b) * c) / 2
print(f"A AREA DO QUADRADO = {quadrado:.4f}")
print(f"A AREA DO TRIANGULO = {triangulo:.4f}")
print(f"A AREA DO TRAPEZIO = {trapezio:.4f}")


Problema "duracao" 
Fazer um programa para ler uma duração de tempo em segundos, daí imprimir na tela esta duração no 
formato horas:minutos:segundos.

duracao = int(input("Digite a duração em segundos: "))

horas = duracao // 3600
resto = duracao % 3600

minutos = resto // 60
segundos = resto % 60

print(f"{horas}:{minutos}:{segundos}")


Problema "notas" 
Fazer um programa para ler as duas notas que um aluno obteve no primeiro e segundo semestres de 
uma disciplina anual. Em seguida, mostrar a nota final que o aluno obteve (com uma casa decimal) no 
ano juntamente com um texto explicativo. Caso a nota final do aluno seja inferior a 60.00, mostrar a 
mensagem "REPROVADO", conforme exemplos. 

nota1 = float(input("Digite a primeira nota: "))
nota2 = float(input("Digite a segunda nota: "))

print()

media = nota1 + nota2

print(f"NOTA FINAL = {media:.1f}")

print()

if media >= 60.00:
    print("APROVADO!")
else:
    print("REPROVADO")

Problema "baskara" 
Fazer um programa para ler os três coeficientes de uma equação do segundo grau. Usando a fórmula 
de Baskara, calcular e mostrar os valores das raízes x1 e x2 da equação com quatro casas decimais, 
conforme exemplo. Se a equação não possuir raízes reais, mostrar uma mensagem. 


import math

a = float(input("Coeficiente a: "))
b = float(input("Coeficiente b: "))
c = float(input("Coeficiente c: "))

delta = (b * b) - (4 * a * c)

if delta < 0:
    print("Esta equação não possui raízes reais")
else:
    x1 = ((-b) + math.sqrt(delta)) / (2 * a)
    x2 = ((-b) - math.sqrt(delta)) / (2 * a)
    print(f"X1 = {x1:.4f}")
    print(f"X2 = {x2:.4f}")



Problema "menor_de_tres" 
Fazer um programa para ler três números inteiros. Em seguida, mostrar qual o menor dentre os três 
números lidos. Em caso de empate, mostrar apenas uma vez.

a = int(input("Primeiro valor: "))
b = int(input("Segundo valor: "))
c = int(input("Terceiro valor: "))

print()

if a < b and a < c:
    print(f"Menor = {a}")
elif b < c:
    print(f"Menor = {b}")
else:
    print(f"Menor = {c}")

Problema "operadora" 
Uma operadora de telefonia cobra R$ 50.00 por um plano básico que dá direito a 100 minutos de 
telefone. Cada minuto que exceder a franquia de 100 minutos custa R$ 2.00. Fazer um programa para 
ler a quantidade de minutos que uma pessoa consumiu, daí mostrar o valor a ser pago.

minutos = int(input("Digite a quantidade de minutos: "))

valor = ((minutos - 100) * 2) + 50

print()

if minutos <= 100:
    print(f"Valor a pagar: R$ 50.00")
else:
    print(f"Valor a pagar: R$ {valor:.2f}")

Problema "troco_verificado" 
Fazer um programa para calcular o troco no processo de pagamento de um produto de uma mercearia. 
O programa deve ler o preço unitário do produto, a quantidade de unidades compradas deste produto, 
e o valor em dinheiro dado pelo cliente. Seu programa deve mostrar o valor do troco a ser devolvido 
ao cliente. Se o dinheiro dado pelo cliente não for suficiente, mostrar uma mensagem informando o 
valor restante conforme exemplo. 



preco = float(input("Preço unitário do produto: "))
qtde = int(input("Quantidade comprada: "))
dinheiro = float(input("Dinheiro recebido: "))

falta: float

print()

total = preco * qtde

troco = dinheiro - total

if dinheiro > total:
    print(f"TROCO = R$ {troco:.2f}")
else:
    falta = total - dinheiro
    print(f"DINHEIRO INSUFICIENTE. FALTAM R$ {falta:.2f}.")


Problema "glicose" 
Fazer um programa para ler a quantidade de glicose 
no sangue de uma pessoa e depois mostrar na tela a 
classificação desta glicose de acordo com a tabela de 
referência ao lado.

glicose = float(input("Digite a medida da glicose: "))

if glicose <= 100:
    print("Classificação: normal")
elif glicose <= 140:
    print("Classificação: elevado")
else:
    print("Classificação: diabetes")

Problema "dardo" 
No arremesso de dardo, o atleta tem três chances para lançar o dardo à maior distância que conseguir. 
Você deve criar um programa para, dadas as medidas das três tentativas de lançamento, informar qual 
foi a maior. 

print("Digite as três distâncias:")
a = float(input(""))
b = float(input(""))
c = float(input(""))

if a > b and a > c:
    print(f"MAIOR DISTÂNCIA = {a:.2f}")
elif b > c:
    print(f"MAIOR DISTÂNCIA = {b:.2f}")
else:
    print(f"MAIOR DISTÂNCIA = {c:.2f}")

Problema "temperatura" 
Deseja-se converter uma medida de temperatura da escala Celsius para Fahrenheit ou vice-versa. Para 
isso, você deve construir um programa que leia a letra "C" ou "F" indicando em qual escala vai ser 
informada uma temperatura. Em seguida o programa deve mostrar a temperatura na outra escala com 
duas casas decimais. A seguir é dada a fórmula para converter de Fahrenheit para Celsius (você deve 
deduzir a fórmula de Celsius para Fahrenheit): ( 32)

escala = str(input("Você vai digitar a temperatura em qual escala (C/F)?"))

if escala == "F":
    fahrenheit = float(input("Digite a temperatura em Fahrenheit: "))
    celsius = (fahrenheit - 32) / 1.8
    print(f"Temperatura equivalente em Celsius: {celsius:.2f}")
else:
    celsius = float(input("Digite a temperatura em Celsius: "))
    fahrenheit = celsius * 9 / 5.0 + 32
    print(f"Temperatura equivalente em Fahrenheit: {fahrenheit:.2f}")

Problema "lanchonete" (adaptado de URI 1038)
Uma lanchonete possui vários produtos. Cada produto possui um código 
e um preço. Você deve fazer um programa para ler o código e a 
quantidade comprada de um produto (suponha um código válido), e daí 
informar qual o valor a ser pago, com duas casas decimais, conforme 
tabela de produtos ao lado.

a = 5.00
b = 3.50
c = 4.80
d = 8.90
e = 7.32

cod = str(input("Código do produto comprado: "))
qtde = int(input("Quantidade comprada: "))

if cod == "1":
    total = a * qtde
    print(f"Valor a pagar: R$ {total:.2f}")
elif cod == "2":
    total = b * qtde
    print(f"Valor a pagar: R$ {total:.2f}")
elif cod == "3":
    total = c * qtde
    print(f"Valor a pagar: R$ {total:.2f}")
elif cod == "4":
    total = d * qtde
    print(f"Valor a pagar: R$ {total:.2f}")
elif cod == "5":
    total = e * qtde
    print(f"Valor a pagar: R$ {total:.2f}")

codigo: int; qtd: int
pagar: float;

codigo = int(input("Codigo do produto comprado: "))
qtd = int(input("Quantidade comprada: "))

pagar = 0
if codigo == 1:
	pagar = qtd * 5.00
elif codigo == 2:
	pagar = qtd * 3.50
elif codigo == 3:
	pagar = qtd * 4.80
elif codigo == 4:
	pagar = qtd * 8.90
elif codigo == 5:
	pagar = qtd * 7.32

print(f"Valor a pagar: R$ {pagar:.2f}")


Problema "multiplos" (adaptado de URI 1044)
Fazer um programa para ler dois números inteiros, e dizer se um número é múltiplo do outro. Os 
números podem ser digitados em qualquer ordem.

print("Digite dois números inteiros")
a = int(input(""))
b = int(input(""))

if a % b == 0 or b % a == 0:
    print("São múltiplos")
else:
    print("Não são múltiplos")

Problema "aumento" (adaptado de URI 1048) 
Uma empresa vai conceder um aumento percentual de 
salário aos seus funcionários dependendo de quanto 
cada pessoa ganha, conforme tabela ao lado. Fazer um 
programa para ler o salário de uma pessoa, daí mostrar 
qual o novo salário desta pessoa depois do aumento, 
quanto foi o aumento e qual foi a porcentagem de 
aumento.

salario = float(input("Digite o salário da pessoa: "))

if salario <= 1000.00:
    novo = salario * 1.20
    aumento = novo - salario
    print(f"Novo salário = R$ {novo:.2f}")
    print(f"Aumento = R$ {aumento:.2f}")
    print("Porcentagem = 20%")
elif salario <= 3000.00:
    novo = salario * 1.15
    aumento = novo - salario
    print(f"Novo salário = R$ {novo:.2f}")
    print(f"Aumento = R$ {aumento:.2f}")
    print("Porcentagem = 15%")
elif salario <= 8000.00:
    novo = salario * 1.10
    aumento = novo - salario
    print(f"Novo salário = R$ {novo:.2f}")
    print(f"Aumento = R$ {aumento:.2f}")
    print("Porcentagem = 10%")
else:
    novo = salario * 1.05
    aumento = novo - salario
    print(f"Novo salário = R$ {novo:.2f}")
    print(f"Aumento = R$ {aumento:.2f}")
    print("Porcentagem = 5%")

Problema "tempo_de_jogo" (adaptado de URI 1046) 
Leia a hora inicial e a hora final de um jogo. A seguir calcule a duração do jogo, sabendo que o mesmo 
pode começar em um dia e terminar em outro, tendo uma duração mínima de 1 hora e máxima de 24 
horas. 


inicial = int(input("Hora inicial: "))
final = int(input("Hora final: "))

if inicial < final:
    resp = final - inicial
else:
    resp = 24 - (inicial - final)

print(f"O JOGO DUROU {resp} HORA(S)")

Problema "coordenadas" (adaptado de URI 1041) 
Leia os valores das coordenadas X e Y de um ponto no plano 
cartesiano. A seguir, determine qual o quadrante ao qual pertence o 
ponto (Q1, Q2, Q3 ou Q4). Se o ponto estiver na origem, escreva a 
mensagem “Origem”. Se o ponto estiver sobre um dos eixos escreva 
“Eixo X” ou “Eixo Y”, conforme for a situação. 


x: float; y: float

x = float(input("Valor de X: "))
y = float(input("Valor de Y: "))

if x == 0 and y == 0:
	print("Origem")
elif x == 0:
	print("Eixo Y")
elif y == 0:
	print("Eixo X")
elif x > 0 and y > 0:
	print("Q1")
elif x < 0 and y > 0:
	print("Q2")
elif x < 0 and y < 0:
	print("Q3")
else:
	print("Q4")


Problema "crescente" (adaptado de URI 1113) 
Leia uma quantidade indeterminada de duplas de valores inteiros X e Y. Escreva para cada X e Y uma 
mensagem que indique se estes valores foram digitados em ordem crescente ou decrescente. O 
programa deve finalizar quando forem digitados dois valores iguais.

print("Digite dois números:")
a = int(input(""))
b = int(input(""))

while a != b:
    if a > b:
        print("Descrescente")
    else:
        print("Crescente")

    print("Digite outros dois números:")
    a = int(input(""))
    b = int(input(""))

Problema "media_idades" 
Faça um programa para ler um número indeterminado de dados, contendo cada um, a idade de um 
indivíduo. O último dado, que não entrará nos cálculos, contém um valor de idade negativa. Calcular 
e imprimir a idade média deste grupo de indivíduos. Se for entrado um valor negativo na primeira vez, 
mostrar a mensagem "IMPOSSIVEL CALCULAR".

idade: int; npessoas: int
soma: float; media: float

print("Digite as idades:")
idade = int(input())

if idade < 0:
	print("IMPOSSIVEL CALCULAR")
else:
	soma = 0
	npessoas = 0
	while idade >= 0:
		soma = soma + idade
		npessoas = npessoas + 1
		idade = int(input())

	media = soma / npessoas

	print(f"MEDIA = {media:.2f}")

Problema "senha_fixa" (adaptado de URI 1114)
Escreva um programa que repita a leitura de uma senha até que ela seja válida. Para cada leitura de 
senha incorreta informada, escrever a mensagem "Senha Invalida! Tente novamente:". Quando a senha 
for informada corretamente deve ser impressa a mensagem "Acesso Permitido" e o algoritmo 
encerrado. Considere que a senha correta é o valor 2002.


senha = int(input("Digite a senha: "))

while senha != 2002:
    senha = int(input("Senha Inválida! Tente novamente: "))

print("Acesso permitido!")


Problema "quadrante" (adaptado de URI 1115)
Escreva um programa para ler as coordenadas (X,Y) de uma quantidade indeterminada de pontos no 
sistema cartesiano. Para cada ponto escrever o quadrante a que ele pertence (Q1, Q2, Q3 ou Q4). O 
algoritmo será encerrado quando pelo menos uma de duas coordenadas for NULA (nesta situação sem 
escrever mensagem alguma).

print("Digite os valores das coordenadas X e Y:")
x = int(input())
y = int(input())

while x != 0 and y != 0:
	if x > 0 and y > 0:
		print("QUADRANTE Q1")
	elif x < 0 and y > 0:
		print("QUADRANTE Q2")
	elif x < 0 and y < 0:
		print("QUADRANTE Q3")
	else:
		print("QUADRANTE Q4")

	print("Digite os valores das coordenadas X e Y:")
	x = int(input())
	y = int(input())

Problema "validacao_de_nota" (adaptado de URI 1117)
Faça um programa que leia as notas referentes às duas avaliações de um aluno. Calcule e imprima a 
média semestral. Faça com que o algoritmo só aceite notas válidas (uma nota válida deve pertencer ao 
intervalo [0,10]). Cada nota deve ser validada separadamente.

nota1 = float(input("Digite a primeira nota: "))

while nota1 < 0 or nota1 > 10:
    nota1 = float(input("Valor inválido. Digite a primeira nota: "))

nota2 = float(input("Digite a segunda nota: "))

while nota2 < 0 or nota2 > 10:
    nota2 = float(input("Valor inválido. Digite a segunda nota: "))

media = (nota1 + nota2) / 2

print(f"MEDIA = {media:.2f}")

Problema "combustivel" (adaptado de URI 1134)
Um posto de combustíveis deseja determinar qual de seus produtos tem a preferência de seus clientes. 
Escreva um algoritmo para ler o tipo de combustível abastecido (codificado da seguinte forma: 
1.Álcool 2.Gasolina 3.Diesel 4.Fim). Caso o usuário informe um código inválido (fora da faixa de 1 a 
4) deve ser solicitado um novo código (até que seja válido). O programa será encerrado quando o 
código informado for o número 4, devendo então mostrar a mensagem "MUITO OBRIGADO", bem 
como as quantidades de cada combustível.

alcool = 0
gasolina = 0
diesel = 0

cod = int
while cod != 4:
    cod = int(input("Informe um código (1, 2, 3) ou 4 para parar: "))

    if cod == 1:
        alcool = alcool + 1
    elif cod == 2:
        gasolina = gasolina + 1
    elif cod == 3:
        diesel = diesel + 1

print(f"Alcool: {alcool}")
print(f"Gasolina: {gasolina}")
print(f"Diesel: {diesel}")

Problema "pares_consecutivos" (adaptado de URI 1159)
O programa deve ler um valor inteiro X indefinidas vezes. (O programa irá parar quando o valor de X 
for igual a 0). Para cada X lido, imprima a soma dos 5 pares consecutivos a partir de X, inclusive o X 
, se for par. Se o valor de entrada for 4, por exemplo, a saída deve ser 40, que é o resultado da operação: 
4+6+8+10+12, enquanto que se o valor de entrada for 11, por exempo, a saída deve ser 80, que é a 
soma de 12+14+16+18+20.
x: int; soma: int

x = int(input("Digite um numero inteiro: "))

while x != 0:
	if x % 2 != 0:
		x = x + 1

	soma = 5 * x + 20
	print(f"SOMA = {soma}")

	x = int(input("Digite um numero inteiro: "))

Problema "tabuada" 
Ler um número inteiro N, daí mostrar na tela a tabuada de N para 1 a 10, conforme exemplo.

num = int(input("Deseja a tabuada para qual valor?"))

for i in range(1, 11):
    produto = num * i
    print(f"{num} X {i} = {produto}")

Problema "soma_impares" (adaptado de URI 1071)
Leia 2 valores inteiros X e Y (em qualquer ordem). A seguir, calcule e mostre a soma dos números 
impares entre eles. 

print("Digite dois números:")
x = int(input(""))
y = int(input(""))

if x > y:
    x, y = y, x

soma = 0

for i in range(x+1, y):
    if i % 2 != 0:
        soma = soma + i

print(f"Soma dos impares = {soma}")

Problema "sequencia_impares" (adaptado de URI 1067)
Leia um valor inteiro X. Em seguida mostre os ímpares de 1 até X, um valor por linha, inclusive o X, 
se for o caso

x = int(input("Digite o valor de X: "))

for i in range(1, x+1):
    if i % 2 != 0:
        print(i)

Problema "dentro_fora" (adaptado de URI 1072)
Leia um valor inteiro N. Este valor será a quantidade de valores inteiros X que serão lidos em seguida. 
Mostre quantos destes valores X estão dentro do intervalo [10,20] e quantos estão fora do intervalo, 
conforme exemplo

N = int(input("Quantos números vai digitar?"))

dentro = 0
fora = 0

for i in range(1, N+1):
    num = int(input("Digite um número: "))
    if 10 <= num <= 20:
        dentro = dentro + 1
    else:
        fora = fora + 1

print(f"{dentro} Dentro")
print(f"{fora} Fora")


Problema "par_impar" (adaptado de URI 1074)
Leia um valor inteiro N. Este valor será a quantidade de números inteiros que serão lidos em seguida. 
Para cada valor lido, mostre uma mensagem dizendo se este valor lido é PAR ou IMPAR, e também 
se é POSITIVO ou NEGATIVO. No caso do valor ser igual a zero (0), seu programa deverá imprimir 
apenas NULO.

N = int(input("Quantos números vai digitar?"))

for i in range(N):
    num = int(input("Digite um número: "))

    if num == 0:
        print("NULO")
    else:
        if num % 2 == 0:
            print("PAR", end=" ")
        else:
            print("IMPAR", end=" ")

        if num > 0:
            print("POSITIVO")
        else:
            print("NEGATIVO")


Problema "media_ponderada" (adaptado de URI 1079)
Leia um valor inteiro N, que representa o número de casos de teste que vem a seguir. Cada caso de 
teste consiste de 3 valores reais, para os quais você deverá calcular e mostrar a média ponderada, sendo 
que o primeiro valor tem peso 2, o segundo valor tem peso 3 e o terceiro valor tem peso 5. Vale lembrar 
que a média ponderada é a soma de todos os valores multiplicados pelo seu respectivo peso, dividida 
pela soma dos pesos

N = int(input("Quantos casos voce vai digitar?"))

for i in range(N):
    print("Digite três números:")
    num1 = float(input(""))
    num2 = float(input(""))
    num3 = float(input(""))

    media = ((num1 * 2) + (num2 * 3) + (num3 * 5)) / 10

    print(f"MÉDIA = {media:.1f}")


Problema "divisao" (adaptado de URI 1116)
Escreva um algoritmo que leia dois números e imprima o resultado da divisão do primeiro pelo 
segundo. Caso não for possível, mostre a mensagem “DIVISAO IMPOSSIVEL”.

ncasos = int(input("Quantos casos voce vai digitar? "))

for i in range(ncasos):
	numerador = int(input("Entre com o numerador: "))
	denominador = int(input("Entre com o denominador: "))

	if denominador == 0:
		print("DIVISAO IMPOSSIVEL")
	else:
		divisao = float(numerador) / denominador
		print(f"DIVISAO = {divisao:.2f}")

Problema "fatorial" (adaptado de URI 1153)
Fazer um programa para ler um número natural N (valor máximo: 15), e depois calcular e mostrar o 
fatorial de N. 

n = int(input("Digite o valor de N: "))

fatorial = 1
for i in range(n, 0, -1):
	fatorial = fatorial * i

print(f"FATORIAL = {fatorial}")


Problema "experiencias" (adaptado de URI 1094)
Maria acabou de iniciar seu curso de graduação na faculdade de medicina e precisa de sua ajuda para 
organizar os experimentos de um laboratório o qual ela é responsável. Ela quer saber no final do ano, 
quantas cobaias foram utilizadas no laboratório e o percentual de cada tipo de cobaia utilizada. Este 
laboratório em especial utiliza três tipos de cobaias: sapos, ratos e coelhos. Para obter estas 
informações, ela sabe exatamente o número de experimentos que foram realizados, o tipo de cobaia 
utilizada e a quantidade de cobaias utilizadas em cada experimento. Faça um programa que leia um 
valor inteiro N que indica os vários casos de teste que vem a seguir. Cada caso de teste contém um 
inteiro que representa a quantidade de cobaias utilizadas e uma letra ('C', 'R' ou 'S'), indicando o tipo 
de cobaia (R:Rato S:Sapo C:Coelho). Apresente o total de cobaias utilizadas, o total de cada tipo de 
cobaia utilizada e o percentual de cada uma em relação ao total

n = int(input("Quantos casos de teste serao digitados? "))

ratos = 0
sapos = 0
coelhos = 0

for i in range(n):
	qtdcobaias = int(input("Quantidade de cobaias: "))
	tipo = str(input("Tipo de cobaia: "))

	if tipo == 'R':
		ratos = ratos + qtdcobaias
	elif tipo == 'S':
		sapos = sapos + qtdcobaias
	else:
		coelhos = coelhos + qtdcobaias

total = ratos + sapos + coelhos
pcoelhos = (float(coelhos) / total) * 100.0
pratos = (float(ratos) / total) * 100.0
psapos = (float(sapos) / total) * 100.0

print("\nRELATORIO FINAL:")
print(f"Total: {total} cobaias")
print(f"Total de coelhos: {coelhos}")
print(f"Total de ratos: {ratos}")
print(f"Total de sapos: {sapos}")
print(f"Percentual de coelhos: {pcoelhos:.2f}")
print(f"Percentual de ratos: {ratos:.2f}")
print(f"Percentual de sapos: {psapos:.2f}")

Problema "negativos" 
Faça um programa que leia um número inteiro positivo N (máximo = 10) e depois N números inteiros 
e armazene-os em um vetor. Em seguida, mostrar na tela todos os números negativos lidos. 

n = int(input("Quantos números vai digitar?"))

vet: [int] = [0 for x in range(n)]

for i in range(n):
    vet[i] = int(input("Digite um número: "))

print("Número Negativos:")

for i in range(n):
    if vet[i] < 0:
        print(vet[i])

Problema "soma_vetor" 
Faça um programa que leia N números reais e armazene-os em um vetor. Em seguida: 
- Imprimir todos os elementos do vetor 
- Mostrar na tela a soma e a média dos elementos do vetor



n = int(input("Quantos numeros voce vai digitar? "))

vetor: [float] = [0 for x in range(n)]

for i in range(n):
	vetor[i] = float(input("Digite um numero: "))

soma = 0
for i in range(n):
	soma = soma + vetor[i]

media = soma / n

print("\nVALORES = ", end="")

for i in range(n):
	print(f"{vetor[i]:.1f}  ", end="")

print(f"\nSOMA = {soma:.2f}")
print(f"MEDIA = {media:.2f}")


Problema "alturas" 
Fazer um programa para ler nome, idade e altura de N pessoas, conforme exemplo. Depois, mostrar na 
tela a altura média das pessoas, e mostrar também a porcentagem de pessoas com menos de 16 anos, 
bem como os nomes dessas pessoas caso houver.

n = int(input("Quantas pessoas serao digitadas? "))

nomes: [str] = [0 for x in range(n)]
idades: [int] = [0 for x in range(n)]
alturas: [float] = [0 for x in range(n)]

for i in range(n):
	print(f"Dados da {i+1}a pessoa:")
	nomes[i] = str(input("Nome: "))
	idades[i] = int(input("Idade: "))
	alturas[i] = float(input("Altura: "))

nmenores = 0
alturatotal = 0
for i in range(n):
	if idades[i] < 16:
		nmenores = nmenores + 1
		alturatotal = alturatotal + alturas[i]

alturamedia = alturatotal / nmenores
percentualMenores = (float(nmenores) / n) * 100.0

print(f"\nAltura media = {alturamedia:.2f}")
print(f"Pessoas com menos de 16 anos: {percentualMenores:.1f}%")

for i in range(n):
	if idades[i] < 16:
		print(nomes[i])
