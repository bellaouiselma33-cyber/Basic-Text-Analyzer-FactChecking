# --- ANALYSEUR DE TEXTE BASIQUE : AIDE AU FACT-CHECKING ---
# Ce script analyse un texte pour détecter la présence de vocabulaire 
# sensationnaliste, souvent utilisé dans la désinformation (fake news).

# 1. Le texte que nous voulons analyser (vous pouvez le modifier)
texte_a_analyser = """
Alerte rouge ! Un scandale choquant vient d'éclater. 
Partagez ce message urgent à tous vos contacts avant qu'il ne soit censuré ! 
C'est un complot mondial.
"""

# 2. Notre "base de données" de mots suspects (lexique sensationnaliste)
mots_suspects = ["alerte", "scandale", "choquant", "urgent", "complot", "partagez", "censuré", "secret"]

# 3. Nettoyage du texte pour faciliter l'analyse (tout mettre en minuscules)
texte_nettoye = texte_a_analyser.lower()

# 4. Création d'une liste vide pour stocker les mots suspects qu'on va trouver
mots_trouves = []

# 5. La boucle d'analyse : on vérifie chaque mot de notre base de données
for mot in mots_suspects:
    # Si le mot suspect est présent dans le texte nettoyé
    if mot in texte_nettoye:
        # On l'ajoute à notre liste de mots trouvés
        mots_trouves.append(mot)

# 6. Affichage des résultats à l'écran
print("--- RÉSULTATS DE L'ANALYSE ---")
print(f"Nombre de mots suspects détectés : {len(mots_trouves)}")

# 7. Conclusion de l'analyse
if len(mots_trouves) > 0:
    print(f"Mots détectés : {mots_trouves}")
    print("Avertissement : Ce texte utilise un vocabulaire très sensationnaliste.")
    print("Recommandation : Une vérification rigoureuse des faits (Fact-Checking) est conseillée.")
else:
    print("Avis : Aucun mot sensationnaliste majeur détecté dans ce texte.")
