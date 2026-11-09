#SLICING FATIAMENTO ACESSAR POR INDICE

#acessando por indice 

frase:str ="meu nome é josé e estudo python com alegria "


print(frase[0])

#notações de pontos decidir de onde começa e onde termina
print(frase[0:3]) 
print(frase[:])#acessa a frase toda
print(frase[3:])#vai do indice 4  e pega todo o resto
print(frase[-8:])


#steps 
numeros:int = [1,2,3,4,5,6,7,8]
print(numeros[0:8:3])#O fatiamento permite extrair partes de uma sequência usando a sintaxe sequencia[inicio:fim:passo].
                                               #reinicia no numero 4
                                        #0 1 2 3 1 2 3 e reinicia dnv aqui 
#para relembrar é como se fosse um laço [1,2,3,4,5,6,7,8] [incia 0:termina 8 : passo de 3 em 3 ]