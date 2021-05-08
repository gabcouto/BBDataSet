import csv
import struct

artistFileName = "artistas_e_melhores.bin"
songFileName = "musicas.bin"
# Arquivo 1 - Entidade Artista e Melhor Semana
estrArq1 = struct.Struct('15s I 10s 10s 10s I I')
sizeOfStructArq1 = 60
# Arquivo 2 - Entidade Músicas
estrArq2 = struct.Struct('15s I I f I I')
sizeOfStructArq2 = 36

def artistIsPresent():
    # Receberemos uma string com um nome, e verificaremos se este nome está presente em nosso arquivo de dados.
    # Se estiver, devolvemos um tuple com suas informações. Caso não esteja, devolvemos um tuple vazio.

    # Com o nome, verificamos no arquivo de índice. Se esta verificação não retornar nada:
    return list()
    # Espero receber a linha do artista ou pelo menos seu índice.
    # Se a verificação tiver sucesso, acessamos a linha com o Artista:
    Arq1 = open(artistFileName, "rb")
    Arq1.seek(sizeOfStructArq1*(int(receivedLine)))
    # Alterar o valor da tupla pra deixar raspado pra fora o binário. 
    # Na função de inserir também preciso levar isso em conta.
    unpackedArtist = list(estrArq1.unpack(Arq1.read(sizeOfStructArq1)))
    for x in (0,2,3,4):
        unpackedArtist[x] = unpackedArtist[x].decode('utf-8')
    Arq1.close()
    # Adicionamos também a linha do arquivo onde este artista pode ser encontrado.
    unpackedArtist.append(receivedLine)
    return unpackedArtist

def musicIsPresent():
    # idêntico ao artistIsPresent para se não encontrarmos.
    return list()
    Arq2 = open(songFileName, "rb")
    Arq2.seek(sizeOfStructArq2(int(receivedLine)))
    unpackedSong = list(estrArq2.unpack(Arq2.read(sizeOfStructArq2)))
    unpackedSong[0] = unpackedSong[0].decode('utf-8')
    Arq2.close()
    return unpackedSong

# TODO: Generate artist/song index and insert it into index file. Return index to user.
def addToFile(fileType,listaDeElementos):
    if fileType == 0:
        # Significa que é a entidade de Artista
        for x in (0,2,3,4):
            listaDeElementos[x] = bytes(listaDeElementos[x], 'utf-8')
        Arq1 = open(artistFileName, "ab")
        Arq1.write(estrArq1.pack(*listaDeElementos))
        Arq1.close()
    else:
        # Significa que é a entidade de Músicas.
        listaDeElementos[0] = bytes(listaDeElementos[0], 'utf-8')
        Arq2 = open(songFileName, "ab")
        Arq2.write(estrArq2.pack(*listaDeElementos))
        Arq2.close()

# Bah não é o suficiente somente receber o position, preciso de mais um dado!
def artistEdit(position,receivedLine,data):
    Arq1 = open(artistFileName, "r+b")
    Arq1.seek(sizeOfStructArq1*(int(receivedLine)))
    unpackedArtist = list(estrArq1.unpack(Arq1.read(sizeOfStructArq1)))
    if position in (0,2,3,4):
        # É string, então precisa de tratamento especial
        unpackedArtist[position] = bytes(data, 'utf-8')
    else:
        unpackedArtist[position] = data
    Arq1.write(estrArq1.pack(*unpackedArtist))
    Arq1.close()

def musicEdit(position,receivedLine,data):
    Arq2 = open(songFileName, "r+b")
    Arq2.seek(sizeOfStructArq2*(int(receivedLine)))
    unpackedSong = list(estrArq2.unpack(Arq2.read(sizeOfStructArq2)))
    if position == 0:
        unpackedSong[position] = bytes(data, 'utf-8')
    else:
        unpackedSong[position] = data
    Arq2.write(estrArq2.pack(*unpackedSong))
    Arq2.close()

# não quero deixar esta burrice aqui, mas não posso corrigi-la agora.
file = open("C:/Users/Gabriel Couto/Documents/repos/BBDataSet/BBDataSet/files/data/raw/csv/charts.csv")
num_lines = sum(1 for line in file)
file.close()

# Estaremos lendo o arquivo reversamente. Não queremos pegar a primeira linha para adicionar no arquivo.
with open("C:/Users/Gabriel Couto/Documents/repos/BBDataSet/BBDataSet/files/data/raw/csv/charts.csv") as csv_file:
    line_count = 1
    for row in reversed(list(csv.reader(csv_file))):
        currentWeek = bytes(row[0], 'utf-8')
        artistName = bytes(row[3], 'utf-8')
        artistWeeksOnBoard = 1
        lastSeen = bytes(row[0], 'utf-8')
        songName = bytes(row[2], 'utf-8')
        songPeakRank = int(row[5])
        songWeeksOnBoard = int(row[6])

        # date,rank,song,artist,last-week,peak-rank,weeks-on-board
        if line_count < num_lines:
            # artistIsPresent recebe o nome do Artista para verificar sua existência no nosso arquivo de dados.
            indexArtistTemp = artistIsPresent(artistName)
            if len(indexArtistTemp) == 0: 
                indexArtistTemp = addToFile(0,[artistName,artistWeeksOnBoard,lastSeen,lastSeen, -1, -1]) # A ocorrência e quantidade de aparições na semana também precisaria ser colocada aqui?
                addToFile(1,[songName,songPeakRank,songWeeksOnBoard,-1,-1,indexArtistTemp[6]]) # A nota da música também precisaria ser adicionada aqui?
            else: 
                if len(musicIsPresent(songName)) == 0:
                    addToFile(1,[songName,songPeakRank,songWeeksOnBoard,-1,-1,indexArtistTemp[6]])
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
                artistEdit(0, indexArtistTemp[7], currentWeek)
                artistEdit(1, indexArtistTemp[7],indexArtistTemp[1]+1)
            

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
            # Arq2.write(estrArq2.pack(bytes(row[0], 'utf-8'), int(row[5]), int(row[6]), 10, line_count, line_count))
            #print(row[2], row[5], row[6])
            line_count += 1
