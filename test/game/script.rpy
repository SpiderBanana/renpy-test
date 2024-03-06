init python:
    def submit_to_google_forms(first_name, last_name, favorite_color):
        js_code = f"submitToGoogleForms('{first_name}', '{last_name}', '{favorite_color}');"
        renpy.emscripten.run_script(js_code)

# Début du jeu
label start:
    scene background
    show character3 with dissolve

    "Bienvenue dans notre questionnaire !"

    # Collecte du prénom
    "Quel est votre prénom ?"
    $ first_name = renpy.input("Entrez votre prénom : ").strip()
    if first_name == "":
        $ first_name = "Anonyme"

    # Transition vers le nouveau fond et personnage avec animation
    scene background2 with fade
    show character2 with dissolve

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

    # Appelle la fonction Python pour soumettre les réponses
    $ submit_to_google_forms(first_name, last_name, favorite_color)

    "Vos réponses ont été soumises. Merci !"

    # Animation de fin avant de quitter
    scene black with fade
    "Fin du questionnaire."
    return
