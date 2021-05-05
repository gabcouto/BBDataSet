import csv
import struct

# não quero deixar esta burrice aqui, mas não posso corrigi-la agora.
file = open("C:/Users/Gabriel Couto/Documents/repos/BBDataSet/BBDataSet/files/data/raw/csv/charts.csv")
num_lines = sum(1 for line in file)
file.close()


# Arquivo 1 - Entidade Artista e Melhor Semana
estrArq1 = struct.Struct('15s I s s s I I')
# Arquivo 2 - Entidade Músicas
estrArq2 = struct.Struct('15s I I f I I')

# Abrir arquivos binários
Arq1 = open("artistas_e_melhores.bin", "rb")
Arq2 = open("musicas.bin", "rb")





# Estaremos lendo o arquivo reversamente. Não queremos pegar a primeira linha para adicionar no arquivo.
with open("C:/Users/Gabriel Couto/Documents/repos/BBDataSet/BBDataSet/files/data/raw/csv/charts.csv") as csv_file:
    line_count = 1
    for row in reversed(list(csv.reader(csv_file))):
        if line_count < num_lines:




            print(row[0], row[1], row[2])
            line_count += 1
