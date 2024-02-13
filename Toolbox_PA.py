import os
import subprocess
import datetime

def menu_principal():
    print("Bienvenue dans la Toolbox de Pentest !")
    print("1. Scanner de ports")
    print("2. Analyse de vulnérabilités")
    print("3. Utiliser Sniper")
    print("4. Utiliser XSSTracer")
    print("5. Créer un rapport")
    print("6. Quitter")

def scanner_ports():
    ip = input("Entrez l'adresse IP à scanner : ")
    subprocess.call(["nmap", "-p-", ip])

def analyse_vuln():
    ip = input("Entrez l'adresse IP à analyser : ")
    subprocess.call(["nikto", "-h", ip])

def utiliser_sniper():
    cible = input("Entrez la cible pour Sniper (format : 'cible.com') : ")
    subprocess.call(["sniper", "-t", cible])

def utiliser_xsstracer():
    url = input("Entrez l'URL à analyser avec XSSTracer : ")
    subprocess.call(["python", "XSSTracer.py", "-u", url])

def creer_rapport():
    date = datetime.datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
    ip = input("Entrez l'adresse IP concernée : ")
    nom_fichier = f"rapport_{ip}_{date}.txt"
    with open(nom_fichier, "w") as fichier:
        fichier.write("Rapport de Pentest\n")
        fichier.write(f"Adresse IP : {ip}\n")
        fichier.write("Date : " + datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S") + "\n")
        fichier.write("\n--- Résultats ---\n")
        # Ajoutez ici d'autres informations pertinentes au rapport

def main():
    while True:
        menu_principal()
        choix = input("Choisissez une option : ")

        if choix == "1":
            scanner_ports()
        elif choix == "2":
            analyse_vuln()
        elif choix == "3":
            utiliser_sniper()
        elif choix == "4":
            utiliser_xsstracer()
        elif choix == "5":
            creer_rapport()
        elif choix == "6":
            print("Merci d'avoir utilisé la Toolbox de Pentest. Au revoir !")
            break
        else:
            print("Option invalide. Veuillez choisir une option valide.")

if __name__ == "__main__":
    main()
