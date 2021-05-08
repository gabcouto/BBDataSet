from typing import Tuple

class TrieNode(object):
    def __init__(self, char: str):
        self.char = char
        self.children = []
        # No fim do titulo, o ID`!= 0
        self.word_finished = 0

def add(root, word: str, id):
    node = root
    for char in word:
        found_in_child = False
        # Procura proxima letra nos filhos do nodo
        for child in node.children:
            if child.char == char:
                # faz a operação com o filho caso tenha achado
                node = child
                found_in_child = True
                break
        # Não encontrou o filho = proxima letra do titulo, então cria novo nodo
        if not found_in_child:
            new_node = TrieNode(char)
            node.children.append(new_node)
            node = new_node
    # Chegou no final bota o iD
    # Caso tenham 2 músicas de nome igual, coloca um 0 no fim do nome da ultima q chegou
    # e adiciona como se fosse nome0
    if node.word_finished == 0:
        node.word_finished = id
    else:
        add(node, "0", id)


def allids(root):
        node = root
        # Se n tem mais filho, bota no arquivo a musica do id e retorna 0 pq trabalho com recursão aqui
        if not root.children:
            print(node.word_finished)####################deletar isso
            #write(algumafunçãoaí(node.word_finished))##############################################################################
            #deleta o nodo pq ele é folha e n vai mais ser usado
            del node
            return 0
        # Defini oq seria uma ordem alfabética aqui, talvez possam ser tirados alguns simbolos pra melhor eficiencia################
        for char in "0123456789 AaBbCcDdEeFfGgHhIiJjKkLlMmNnOoPpQqRrSsTtUuVvWwXxYyZz'!#$%&\()*+,-./:;<=>?@[\\]_{|}":
            char_not_found = True
            # Procura por todos os filhos se tem o digito da vez
            for child in node.children:
                if child.char == char:
                    # Achamo
                    char_not_found = False
                    # Procura todas as palavras q esse filho pode ter
                    allids(child)
                    # break pq n da pra ter 2 nodos filhos com o mesmo valor
                    break
        # Se tem id, coloca no arquivo a musica dele
        # Esse é o caso de have um palavra "dentro" de outra
        if node.word_finished > 0:
            print(node.word_finished)###############deletar isso
            #write(algumafunçãoaí(node.word_finished))##############################################################################
        del node
        return 0

#fazer vetor de 100 pointers para a class TrieNode
class TriePointer(object):
    def __init__(self, chave):
        self.chave = chave
        self.pointsto = TrieNode('*')
        self.proximo = None

def insereTrie(self, titulo:str ,chave, id):
    if self.chave==chave:   #se a chave é a msm do primeiro só adiciona a musica na trie
        add(self.pointsto, titulo, id)
    else:
        while self.proximo != None: #procura o lugar onde deve ser inserido
            if self.proximo.chave <= chave:
                self = self.proximo
        if self.chave!=chave:   #se n tiver a trie com a chave, cria ela
            trieaux=TriePointer(1)
            trieaux.proximo = self.proximo
            self.proximo = trieaux
            trieaux.chave = chave
            add(trieaux.pointsto, titulo, id)
        else:
            add(self.pointsto, titulo, id)

def allidspointer(self):
    allids(self.pointsto)
    if self.proximo != None:
        allidspointer(self.proximo)

peakranks = TriePointer(1)
wobsongs = TriePointer(1)
wobartists = TriePointer(1)
notasongs = TriePointer(1)
notaartista = TriePointer(1)
aparicoesartist = TriePointer(1)
SongTitles = TrieNode('*')
ArtistNames = TrieNode('*')

#insereTrie(peakranks, nome da musica, valorpeakrank, iddamusica)
#insereTrie(wobsongs, nome da musica, valorwob, iddamusica)
#insereTrie(wobartists, nome do artista, valorwobart, iddoartista)
#insereTrie(notasongs, nome da musica, valornotas, iddamusica)
#insereTrie(notaartista, nome do artista, valornotaa, iddoartista)
#insereTrie(aparicoesartist, nome do artista, aparaicoes, iddoartista)
#add(SongTitles, nome da musica, iddamusica)
#add(ArtistNames, nome do artista, iddoartista)

#IDpeakrank = open(IDpeakrank, ab)#####################################
allidspointer(peakranks)
#IDpeakrank.close()####################################################
##### igual os outros

#IDtitulos = open (musica_titulo, ab)##################################
allids(SongTitles)
#IDtitulos.close()#####################################################

#IDnomes = open(nome_artista, ab)######################################
allids(ArtistNames)
#IDnomes.close()####################################################

#adições teste:
#add(SongTitles, "blackbird", 123)
#add(SongTitles, "zurrilho", 26)
#add(SongTitles, "all my loving", 100)
#add(SongTitles, "01leg", 2)
#add(SongTitles, "black", 231)
#add(SongTitles, "hells bells", 90)
#add(SongTitles, "hells bells", 92)
#add(SongTitles, "00leg", 1)
#add(SongTitles, "hells breaking loose", 91)
#add(SongTitles, "zai se eu te pego", 25)
#add(SongTitles, "back in black", 12)

#add(ArtistNames, "Johnny Cash", 90)
#add(ArtistNames, "John Lennon", 89)
#add(ArtistNames, "Johnsson Jack", 91)
#add(ArtistNames, "Steph Curry", 110)
#add(ArtistNames, "Stephen Hawkings", 111)
    

#exemplo de varios adds no vetor de peakranks
#for pkrnkvl in range(1, 9, 2):
    #insereTrie(peakranks, "blackice", pkrnkvl, 3)
    #insereTrie(peakranks, "black treacle", pkrnkvl, 2)
    #insereTrie(peakranks, "bill gates", pkrnkvl, 1)