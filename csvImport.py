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

# Abrir arquivos binários. Mudar isso aqui depois. Extensões.
Arq1 = open("artistas_e_melhores.bin", "ab")
Arq2 = open("musicas.bin", "ab")



print(num_lines)

# Estaremos lendo o arquivo reversamente. Não queremos pegar a primeira linha para adicionar no arquivo.
with open("C:/Users/Gabriel Couto/Documents/repos/BBDataSet/BBDataSet/files/data/raw/csv/charts.csv") as csv_file:
    line_count = 1
    for row in reversed(list(csv.reader(csv_file))):
        if line_count < num_lines:
            # rows de interesse para Música:
            # 2 = title
            # 5 = peak_rank
            # 6 = weeks on board
            
            # Everything we get from the csv are strings. They need to be converted into int data type. 
            #pr = int(row[5])
            #wb = int(row[6])
            #print(pr, wb)

            # (bytes(row[0], 'utf-8'), int(row[5]), int(row[6]), 10)
            #print(estrArq2.pack(bytes(row[2], 'utf-8'), int(row[5]), int(row[6]), 10, line_count, line_count))
            Arq2.write(estrArq2.pack(bytes(row[0], 'utf-8'), int(row[5]), int(row[6]), 10, line_count, line_count))
            #print(row[2], row[5], row[6])
            line_count += 1
