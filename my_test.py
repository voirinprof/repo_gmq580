from bs4 import BeautifulSoup

# Je lis le fichier XML
with open(r"C:\Users\voiy1701\Downloads\georss3.xml", "r") as file:
    content = file.read()

# Initialisation de BeautifulSoup
soup = BeautifulSoup(content, 'xml')

# On va alimenter la liste avec les infos du fichier XML
messages = []

# On cherche tous les messages (balise ITEM)
for item in soup.find_all('item'):
    # Un message contiendra le titre et le créateur
    # On utilise une liste
    msg = []
    
    # On cherche les infos sur le titre (balise TITLE)
    for title in item.find_all('title'):
        # On ajoute le titre à msg
        msg.append(title.text)
    
    # On cherche les infos du créateur (balise dc:creator)
    for creator in item.find_all('dc:creator'):
        # On ajoute le créateur à msg
        msg.append(creator.text)
    
    # On ajoute les infos du message (msg) dans la liste des messages (messages)
    messages.append(msg)

# On affiche le résultat
# On dispose d'une liste messages 
# avec les infos du XML
for m in messages:
    print(m)