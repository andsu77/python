# EXERCICIO FINAL DO MODULO: PLANEJAMENTO DE UM EVENTO
#
# Crie um programa que ajude a planejar um evento e verificar se ele cabe no
# orcamento. Escreva seu codigo abaixo de cada etapa, neste mesmo arquivo.
print("===================================Planejamento de Evento=============================================")
# ETAPA 1 - ENTRADA DE DADOS E VARIAVEIS
# 1. Pergunte o nome e a idade da pessoa organizadora.
nome = str(input("Digite seu nome para o evento: "));
idade = int(input("Digite sua idade: "));
# 2. Pergunte a quantidade de convidados e quantos lugares cabem em cada mesa.
qtdConvidados = int(input("Quantidade de convidados: "));
qtdLugaresMesas = int(input("Quantos lugares cabem na mesa: "));
custoLocal =float(input("Custo do local: "))
# 3. Pergunte o custo por convidado, o custo do local e o orcamento disponivel.
valorPorConvidado = float(input("Valor por convidado: "));
# 4. Pergunte a porcentagem de imposto e o tamanho de um lado de um painel
#    quadrado, em metros.
valorImposto = float(input("Valor do imposto: "));
# 5. Guarde cada resposta em uma variavel com um nome claro e converta os
#    valores para os tipos adequados: str, int ou float.#fiz isso ja 


# 6. Mostre o tipo de uma das respostas antes e depois de converter seu valor.
#    Explique com suas palavras o que isso demonstra sobre a tipagem dinamica.
print("mostrando tipo", type(nome), "declarei string pq é um texto");


# Considere que os valores informados sao validos e que a quantidade de
# convidados e de lugares por mesa serao maiores que zero.
if(qtdConvidados<=0):
    print("valor inadequado");
else:
    print("Avance para proxima etapa do cadastro");

# ETAPA 2 - OPERADORES ARITMETICOS
custoConvidados:float = qtdConvidados*valorPorConvidado
baseDeCalculo:float =  custoConvidados + custoLocal;
impostoAplicadoSobreConvidados:float = baseDeCalculo * (valorImposto/100);
valorTotalComimposto:float = baseDeCalculo + impostoAplicadoSobreConvidados; 
# Calcule e mostre:
# 1. O custo dos convidados.
print("O custo dos convidados foi de: ", custoConvidados);
# 2. O valor do imposto aplicado sobre o custo dos convidados mais o custo
#    do local. Use parenteses para indicar a ordem do calculo.

print("valor do imposto: ",impostoAplicadoSobreConvidados)

# 3. O custo total, incluindo o imposto.
print("Valor Total incluindo o imposto: ", valorTotalComimposto);


# 5. O custo medio por convidado.
custoMedioConvidados = custoConvidados/qtdConvidados;
print(custoMedioConvidados);

# 6. Quantas mesas ficam completas usando divisao inteira (//) e quantos
#    convidados sobram usando o modulo (%). Calcule quantas mesas sao
#    necessarias ao todo, incluindo uma mesa extra se houver sobra.

mesasCompletas:int = qtdConvidados// qtdLugaresMesas;
sobraConvidados:float = qtdConvidados % qtdLugaresMesas;

if(sobraConvidados > 0):
    print("Mesa extra adicionada para a sobra de convidados: ", mesasCompletas + 1);

