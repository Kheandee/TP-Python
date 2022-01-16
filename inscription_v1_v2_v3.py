import re
from datetime import datetime,
import csv

def verifadrmail(ch):
    motif = r"^[^<>]*<([^<>]+)>$|(^[^<>]+$)"
    a = re.findall(motif, ch.strip())
    if len(a)>0:
        adr = ''.join(a[0]).strip()
    else:
        adr = ''
    if adr=='':
        return False
    else:
        motif = r"^[a-zA-Z0-9_\-]+(\.[a-zA-Z0-9_\-]+)*@[a-zA-Z0-9_\-]+(\.[a-zA-Z0-9_\-]+)*(\.[a-zA-Z]{2,6})$"
        return re.match(motif, adr) != None

def categorie_quidditch(age):
    if age <= 6:
        categorie = "Non admis"
    elif age <= 12:
        categorie = "Poussin"
    elif age <= 18:
        categorie = "Cadet"
    elif age <= 24:
        categorie = "Junior"
    elif age <= 30:
        categorie = "Semi-pro"
    elif age <= 40:
        categorie = "Pro"
    else:
        categorie = "Non admis"
    print(categorie)

date_of_birth = datetime.strptime(input("--->"), "%j %m %a")
def calculate_age(born):
    today = date.today()
    return today.year - born.year - ((today.month, today.day) < (born.month, born.day))

age = calculate_age(date_of_birth)

nom = input("Entrez votre nom: ")
prenom = input("Entrez votre prénom: ")
mail = input("Entrez votre adresse mail: ")
print("Entrez votre date de naissance (jj mm aaaa): ")

print(nom, prenom, mail, age)

with open('inscrits_total.csv.csv', newline='')