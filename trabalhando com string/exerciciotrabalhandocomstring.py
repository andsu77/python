# Dados de entrada:
# Python
# entrada = "   jOSÉ aNDERSON - aUTOMAÇÃO iNDUSTRIAL - 10.0,8.5,9.0,7.5,6.0   "
# 🎯 Tarefas:
# Limpeza e Formatação Inicial:

entrada:str = "   jOSÉ aNDERSON - aUTOMAÇÃO iNDUSTRIAL - 10.0,8.5,9.0,7.5,6.0    ";

# Remova os espaços extras no início e no final da string entrada.

print(entrada.strip());
# Converta todo o texto para o formato Title Case (primeira letra de cada palavra em maiúscula).
print(entrada.title());
# Divisão de Dados (split):
print(entrada.split());
# Separe a string limpa em três partes usando o delimitador " - " (traço com espaços).
print(entrada.split(" - "));
# Armazene os resultados nas variáveis nome, curso e notas_str.
nome:str = entrada.split(" - ")[0];

curso:str = entrada.split(" - ")[1];
notas:str = entrada.split(" - ")[2];
# Fatiamento e Acesso por Índice:

# Extraia e exiba as primeiras 4 letras do nome.
print(nome[0:4]);
# Extraia e exiba as últimas 5 letras do curso.
print(curso[-23:-32])
# Trabalhando com o Passo (step):

# Dada a lista de inteiros codigo = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9], faça um fatiamento que pegue do índice 0 ao 9 saltando de 2 em 2 e exiba o resultado.

# Interpolação (f-string):

# Monte e exiba uma mensagem final formatada exatamente assim:

# Aluno: José Anderson | Curso: Automação Industrial | Status: Cadastrado

# 💡 Gabarito / Solução Esperada