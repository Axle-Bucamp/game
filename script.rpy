# Vous pouvez placer le script de votre jeu dans ce fichier.

# Déclarez sous cette ligne les images, avec l'instruction 'image'
# ex: 
image dwarf = Placeholder("bg")
image dwarf tavern = Frame("images/background/generated_content_main_hall_dwarf.PNG")
image right side emra neutral = Image("images/background/dark hair humain noble.png")

# Déclarez les personnages utilisés dans le jeu.
define e = Character('Emra', color="#1506ec", image="emra")

# Le jeu commence ici

label start:
    scene dwarf tavern
    $ money = 0

    e neutral "Bonjour joueur, bienvenue dans un monde ou seul la montagne fait loi."

    e neutral "Préparez vous à être transpersé de part en part par les vents glacial du nord ! Car rien ne pourra les arréter. Rien ..."

    e neutral "Si ce n'est la chaleur rassurante de la tavern, seul lieux de repos de nos plus brave guerrier."

    e neutral "Alors n'attendez pas et tendez l'oreile, écoutez la douce musique de notre menestrel, Le doux chant de l'hydromel."
    
    e neutral "Mais surtout joignez vous à nous autour de ce copieux repas."

    e neutral "Nous vous raconterons alors peut-être notre histoire si vous en êtes digne."

    return
