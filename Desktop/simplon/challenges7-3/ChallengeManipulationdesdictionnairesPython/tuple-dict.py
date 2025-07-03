# Challenge: Manipulation des tuples et dictionnaires Python

# 1. Travail avec les tuples
print("=== MANIPULATION DES TUPLES ===")
etudiant_info = ("Prénom : \"Yasmine\"", "Âge : 22", "Filière : \"Informatique\"", "Moyenne générale : 17.4")

print("Informations complètes de l'étudiant:")
for element in etudiant_info:
    print(element)

print("\nSlice des 2 premiers éléments:")
slice_etudiant = etudiant_info[0:2]
for element in slice_etudiant:
    print(element)

print(10*"*", "\nTuple final:")
tuple_info_supplementaire = ("Mention : \"très bien\"", "Année d'obtention du diplôme : 2024")
tuple_final = etudiant_info + tuple_info_supplementaire

print("Tuple final complet:")
for element in tuple_final:
    print(element)

# 2. Travail avec les dictionnaires
print("\n=== MANIPULATION DES DICTIONNAIRES ===")
First_dict = { 
    "Appareil": "Laptop",
    "Marque": "IBM",
    "Carte mère": "MSI Z490",
    "Carte Graphique": "GeForce RTX 3070",
    "RAM": "16G",
    "Processeur": "Intel core i7-G11",
    "SSD": "1 To" 
} 

# Modification de la RAM
First_dict["RAM"] = "32G"

print("Clés du dictionnaire:", list(First_dict.keys()))
print("Valeurs du dictionnaire:", list(First_dict.values()))
print("Items du dictionnaire:", list(First_dict.items()))

# Inversion des paires Carte Graphique et Processeur
print("\nInversion des paires Carte Graphique et Processeur:")
carte_graphique_value = First_dict["Carte Graphique"]
processeur_value = First_dict["Processeur"]

# Supprimer les paires originales
del First_dict["Carte Graphique"]
del First_dict["Processeur"]

# Ajouter les paires inversées
First_dict[carte_graphique_value] = "Carte Graphique"
First_dict[processeur_value] = "Processeur"

# Ajouter système d'exploitation
First_dict["Système d'exploitation"] = "Windows 10"

print("Dictionnaire final après inversion:")
for key, value in First_dict.items():
    print(f"'{key}': '{value}'")
