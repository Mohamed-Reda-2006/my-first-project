import os
from datetime import datetime

# 1. Choisir un dossier
dossier = input("Entrez le chemin du dossier à organiser : ").strip()

if not os.path.exists(dossier):
    print("❌ Ce dossier n'existe pas.")
    exit()

# 2. Lister son contenu
elements = os.listdir(dossier)
fichiers_deplaces = 0
nouveaux_dossiers = set()

print("\n--- Résumé des fichiers traités ---")

for element in elements:
    chemin_complet = os.path.join(dossier, element)

    # Garder uniquement les fichiers (ignorer les dossiers)
    if os.path.isfile(chemin_complet):
        # 4. Récupérer les infos avant déplacement (Nom, Extension, Date)
        nom, extension = os.path.splitext(element)
        ext_propre = extension[1:].lower() if extension else "sans_extension"
        
        timestamp = os.path.getmtime(chemin_complet)
        date_modif = datetime.fromtimestamp(timestamp).strftime("%Y-%m-%d %H:%M:%S")

        # 3. Classer les fichiers (Créer sous-dossier + Déplacer)
        dossier_dest = os.path.join(dossier, ext_propre)
        if not os.path.exists(dossier_dest):
            os.makedirs(dossier_dest)
            nouveaux_dossiers.add(ext_propre)

        nouveau_chemin = os.path.join(dossier_dest, element)
        os.rename(chemin_complet, nouveau_chemin)
        fichiers_deplaces += 1

        # Afficher le résumé du fichier
        print(f"Nom: {nom} | Extension: {extension or 'Aucune'} | Modifié le: {date_modif}")

# 5. Vérifier le résultat
print("\n--- Résultat final ---")
print(f"Nouveaux dossiers créés : {list(nouveaux_dossiers) if nouveaux_dossiers else 'Aucun'}")
print(f"Nombre total de fichiers déplacés : {fichiers_deplaces}")
