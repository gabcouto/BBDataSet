import csv
import struct


def artistIsPresent:
    # Receberemos uma string com um nome, e verificaremos se este nome está presente em nosso arquivo de dados.
    # Se estiver, devolvemos um tuple com suas informações. Caso não esteja, devolvemos um tuple vazio.

    # Com o nome, verificamos no arquivo de índice. Se esta verificação não retornar nada:
    return tuple()
    # Espero receber a linha do artista ou pelo menos seu índice.
    # Se a verificação tiver sucesso, acessamos a linha com o Artista:

    Arq1.seek(sizeOfStructArq1*(int(receivedLine)))
    # Alterar o valor da tupla pra deixar raspado pra fora o binário. 
    # Na função de inserir também preciso levar isso em conta.
    print(estrArq2.unpack(Arq2.read(36)))



# não quero deixar esta burrice aqui, mas não posso corrigi-la agora.
file = open("C:/Users/Gabriel Couto/Documents/repos/BBDataSet/BBDataSet/files/data/raw/csv/charts.csv")
num_lines = sum(1 for line in file)
file.close()

# Arquivo 1 - Entidade Artista e Melhor Semana
estrArq1 = struct.Struct('15s I s s s I I')
# Arquivo 2 - Entidade Músicas
estrArq2 = struct.Struct('15s I I f I I')

# Abrir arquivos binários. Mudar isso aqui depois. Extensões. Sinal plus.
Arq1 = open("artistas_e_melhores.bin", "ab")
Arq2 = open("musicas.bin", "ab")

# Estaremos lendo o arquivo reversamente. Não queremos pegar a primeira linha para adicionar no arquivo.
with open("C:/Users/Gabriel Couto/Documents/repos/BBDataSet/BBDataSet/files/data/raw/csv/charts.csv") as csv_file:
    line_count = 1
    for row in reversed(list(csv.reader(csv_file))):
        currentWeek = row[0]
        artistName = row[3]
        artistWeeksOnBoard = 1
        lastSeen = row[0]
        songName = row[2]
        songPeakRank = row[5]
        songWeeksOnBoard = row[6]

        # date,rank,song,artist,last-week,peak-rank,weeks-on-board
        if line_count < num_lines:
            # artistIsPresent recebe o nome do Artista para verificar sua existência no nosso arquivo de dados.
            indexArtistTemp = artistIsPresent(artistName)
            if len(indexArtistTemp) == 0: 
                indexArtistTemp = artistAdd(artistName,artistWeeksOnBoard,lastSeen,lastSeen) # A ocorrência e quantidade de aparições na semana também precisaria ser colocada aqui?
                musicAdd(songName,songPeakRank,songWeeksOnBoard,indexArtistTemp) # A nota da música também precisaria ser adicionada aqui?
            else: 
                if len(musicIsPresent(songName)) == 0:
                    musicAdd(songName,songPeakRank,songWeeksOnBoard,indexArtistTemp)
                else: 
                    # Esta seção não existirá a menos que seja necessária para obter a nota da música.
                # Se o artista já está no arquivo, significa que precisamos editá-lo, porque temos um novo "Primeira Aparição".
                # Se a data da primeira aparição no arquivo for diferente de currentWeek, currentWeek é o novo candidato para "primeira aparição".
                # Se o código chegou aqui, currentWeek já será necessariamente diferente de firstSeen do Artista.
                # Além disso, incrementamos weeksOnBoard do Artista.
                # Se o artista já está no arquivo, também precisamos incrementar o Wob-artist, mas desde que não estejamos em uma mesma semana

                # De acordo com a entidade Artista, temos:
                # @ 0 = Nome
                # @ 1 = Weeks on Board do Artista
                # @ 2 = Primeira Aparição
                # @ 3 = Última Aparição
                # @ 4 = Ocorrência
                # @ 5 = Quantidade de Aparições na Semana
                # @ 6 = Índice Artista
                artistEdit(0, currentWeek)
                artistEdit(1, indexArtistTemp[1]+1)
            

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
