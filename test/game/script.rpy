# Déclare le script Python à utiliser dans Ren'Py
init python:
    def submit_to_google_forms(first_name, last_name, favorite_color):
        js_code = f"submitToGoogleForms('{first_name}', '{last_name}', '{favorite_color}');"
        renpy.emscripten.run_script(js_code)

# Début du jeu
label start:
    scene bg room
    with fade

    "Bienvenue dans notre questionnaire !"

    # Collecte du prénom
    "Quel est votre prénom ?"
    $ first_name = renpy.input("Entrez votre prénom : ").strip()
    if first_name == "":
        $ first_name = "Anonyme"

    # Collecte du nom de famille
    "Quel est votre nom de famille ?"
    $ last_name = renpy.input("Entrez votre nom de famille : ").strip()
    if last_name == "":
        $ last_name = "Anonyme"

    # Choix de la couleur préférée
    "Quelle est votre couleur préférée ?"
    menu:
        "Vert":
            $ favorite_color = "Vert"
        "Bleu":
            $ favorite_color = "Bleu"

    # Confirmation des réponses
    "Merci pour vos réponses !"
    "Prénom : [first_name]"
    "Nom de famille : [last_name]"
    "Couleur préférée : [favorite_color]"

    # Appelle la fonction Python pour soumettre les réponses
    $ submit_to_google_forms(first_name, last_name, favorite_color)

    "Vos réponses ont été soumises. Merci !"
    return
