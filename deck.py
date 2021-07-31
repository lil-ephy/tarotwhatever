def cardGen(facePls=bool, marseille=False):
    if marseille:
        return (
            ["Valet", "Cavalier", "Dame", "Roi"]
            if facePls == True
            else ["Coupes", "Deniers", "Épées", "Bâtons"]
        )
    else:
        return (
            ["Page", "Knight", "Queen", "King"]
            if facePls == True
            else ["Cups", "Pentacles", "Swords", "Wands"]
        )


def arcanaGen(marseille=False):
    return (
        [
            "Le Mat (The Fool)",
            "Le Bateleur (The Magician)",
            "La Papesse (The Popess)",
            "L'Impératrice (The Empress)",
            "L'Empereur (The Emperor)",
            "Le Pape (The Pope)",
            "L'Amoureux (The Lover)",
            "Le Chariot (The Chariot)",
            "La Justice (Justice)",
            "L'Ermite (The Hermit)",
            "La Roue de Fortune (The Wheel of Fortune)",
            "La Force (Strength)",
            "Le Pendu (The Hanged Man)",
            "La Mort (Death)",
            "Tempérance (Temperance)",
            "Le Diable (The Devil)",
            "La Maison Dieu (The House of God)",
            "L'Étoile (The Star)",
            "La Lune (The Moon)",
            "Le Soleil (The Sun)",
            "Le Jugement (The Judgement)",
            "Le Monde (The World)",
        ]
        if marseille
        else [
            "The Fool",
            "The Magician",
            "The High Priestess",
            "The Empress",
            "The Emperor",
            "The Hierophant",
            "The Lovers",
            "The Chariot",
            "Strength",
            "The Hermit",
            "Wheel of Fortune",
            "Justice",
            "The Hanged Man",
            "Death",
            "Temperance",
            "The Devil",
            "The Tower",
            "The Star",
            "The Moon",
            "The Sun",
            "Judgment",
            "The World",
        ]
    )
