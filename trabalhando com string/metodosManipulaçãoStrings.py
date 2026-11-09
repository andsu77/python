#METODOS DE STRINGS 

#split(): o método split() transforma uma string em uma lista (que é o equivalente ao array em Python


texto:str = "textinho de josé anderson , meu nome é andersonnn , sou josé anderson testando o texto que vai virar arrya ";

arraytexto = texto.split();

print("texto que virou array:",arraytexto,"\n","texto normal: ",texto)


#podemos colocar o delimitador no split 
frutas:str = "uva.maça.banana.imao.abacaxi.e vou comer todas elas quando eu quiser"
arraydefrutas = frutas.split(".");
print(arraydefrutas);


#RETORNA LIST
print(type("uva.maça.banana.imao.abacaxi.e vou comer todas elas quando eu quiser".split()))

#Strip:  .strip() remove espaços em branco (como espaços normais, tabulações \t e quebras de linha \n) apenas no início e no final de uma string

texto1 = "          olá mundo           ";

print(f"sem o strip:{texto1}");
print(f"com strip:{texto1.strip()}");


#capitalize() o método .capitalize() converte o primeiro caractere de uma string em maiúsculo e transforma todos os caracteres restantes em minúsculo

frase = "meu nome é josé anderson"

print(frase.capitalize());


#lower() retorna uma string com todas as letras minuscula

txt:str = "DEIXANDO O TEXTO MINUSCULO";

print(txt.lower());

#UPPER retorna a string co texto maiusculo

txt = "deixando o texto maiusculo";

print(txt.upper());


#title() cada palavra a primeira letra será maiusculoa

frase ="Meu nome é jose";

print(frase.title())