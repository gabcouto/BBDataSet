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
        # Se n tem mais filho e bota no arquivo a musica do id e retorna 0 pq trabalho com recursão aqui
        if not root.children:
            print(node.word_finished)####################deletar isso
            #write(algumafunçãoaí(node.word_finished))##############################################################################
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
        if node.word_finished > 0:
            print(node.word_finished)###############deletar isso
            #write(algumafunçãoaí(node.word_finished))##############################################################################
        return 0

if __name__ == "__main__":
    SongTitles = TrieNode('*')
    ArtistNames = TrieNode('*')
    add(SongTitles, "blackbird", 123)
    add(SongTitles, "zurrilho", 26)
    add(SongTitles, "all my loving", 100)
    add(SongTitles, "01leg", 2)
    add(SongTitles, "black", 231)
    add(SongTitles, "hells bells", 90)
    add(SongTitles, "hells bells", 92)
    add(SongTitles, "00leg", 1)
    add(SongTitles, "hells breaking loose", 91)
    add(SongTitles, "zai se eu te pego", 25)
    add(SongTitles, "back in black", 12)

    add(ArtistNames, "Johnny Cash", 90)
    add(ArtistNames, "John Lennon", 89)
    add(ArtistNames, "Johnsson Jack", 91)
    add(ArtistNames, "Steph Curry", 110)
    add(ArtistNames, "Stephen Hawkings", 111)

    #SongTitl = open (musica_titulo, ab)##################################
    allids(SongTitles)
    #SongTitl.close()#####################################################

    #ArtNameID = open(nome_artista, ab)###################################
    allids(ArtistNames)
    #ArtNameID.close()####################################################