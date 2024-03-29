# def sansDC(ch):
#     "cette fonction renvoie la chaîne ch amputée de son dernier caractère"
#     nouv = ""
#     i, j = 0, len(ch) -1 
#     while i < j:
#         nouv = nouv + ch[i]
#         i = i + 1
#     return nouv 
# def ecrireDansFichier():
#     of = open(nomF, 'a')
#     while 1:
#         # ligne = raw_input("entrez une ligne de texte (ou <Enter>) : ")
#         ligne = "entrez une ligne de texte (ou <Enter>) : "
#         if ligne == '':
#             break
#         else:
#             of.write(ligne + '\n')
#         of.close()
# def lireDansFichier():
#     of = open(nomF, 'r')
#     while 1:
#         ligne = of.readline()
#         if ligne == "":
#             break
#         # afficher en omettant le dernier caractère (= fin de ligne) :
#         print(sansDC(ligne))
#         of.close() 
 
# nomF = 'Nom du fichier à traiter : '
# choix = 'Entrez "e" pour écrire, "c" pour consulter les données : '
# if choix =='e': 
#  ecrireDansFichier()
# else:
#  lireDansFichier()

def filtre(source,destination):
    "recopier un fichier en éliminant les lignes de remarques"
    fs = open(source, 'r')
    fd = open(destination, 'w')
    while 1:
        txt = fs.readline()
        if txt =='':
            break
        if txt[0] != '#':
            fd.write(txt)
    fs.close()
    fd.close()
    return


f = open("Fichiertexte", "w")
f.write("Ceci est la ligne un\nVoici la ligne deux\n")
f.write("Voici la ligne trois\nVoici la ligne quatre\n")
f.close()

ff = open('Fichiertexte','r')
t = ff.readline()
print(t)
print(ff.readline())

ff.close()

obFichier = open('Monfichier','a')
obFichier.write('Bonjour, fichier !')
obFichier.write("Quel beau temps, aujourd'hui !")

ft= open("Monfichier","r")
print(ft.readline())
obFichier.close()


