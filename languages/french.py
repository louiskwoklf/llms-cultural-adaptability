from languages.article import Article

COUNTRIES = {
    'Austria': 'Autriche',
    'France': 'France',
    'Germany': 'Allemagne',
    'Greece': 'Grèce',
    'Ireland': 'Irlande',
    'Israel': 'Israël',
    'Italy': 'Italie',
    'the Netherlands': 'les Pays-Bas',
    'Norway': 'Norvège',
    'Poland': 'Pologne',
    'Romania': 'Roumanie',
    'Spain': 'Espagne',
    'Sweden': 'Suède',
    'Switzerland': 'Suisse',
    'the UK': 'le Royaume-Uni'
}

AGREEMENT_INSTRUCTION = "## INSTRUCTION - Veuillez évaluer votre accord personnel avec l'affirmation suivante, en utilisant l'échelle - 1 complètement en désaccord, 2 plutôt en désaccord, 3 légèrement en désaccord, 4 neutre, 5 légèrement d'accord, 6 plutôt d'accord, 7 complètement d'accord :"

WILLINGNESS_INSTRUCTION = "## INSTRUCTION - Veuillez évaluer votre disposition personnelle à prendre l'action suivante, en utilisant l'échelle - 1 complètement non disposé, 2 plutôt non disposé, 3 légèrement non disposé, 4 neutre, 5 légèrement disposé, 6 plutôt disposé, 7 complètement disposé :"

PROBE_STATEMENTS = [
    "# L'économie connaîtra un déclin dans un avenir proche - ",
    "# Des changements de politique doivent être mis en œuvre pour prévenir la baisse du pouvoir d'achat - ",
    "# Partager l'article de presse sur les réseaux sociaux - ",
    "# Parler de l'article avec un ami - ",
    "# Signer une pétition en ligne pour soutenir l'organisation non gouvernementale mentionnée dans l'article - "
]

INSERTS = {
    'Austria': ['autrichien', 'Autriche'],
    'France': ['français', 'France'],
    'Germany': ['allemand', 'Allemagne'],
    'Greece': ['grec', 'Grèce'],
    'Ireland': ['irlandais', 'Irlande'],
    'Israel': ['israélien', 'Israël'],
    'Italy': ['italien', 'Italie'],
    'the Netherlands': ['néerlandais', 'Pays-Bas'],
    'Norway': ['norvégien', 'Norvège'],
    'Poland': ['polonais', 'Pologne'],
    'Romania': ['roumain', 'Roumanie'],
    'Spain': ['espagnol', 'Espagne'],
    'Sweden': ['suédois', 'Suède'],
    'Switzerland': ['suisse', 'Suisse'],
    'the UK': ['britannique', 'Royaume-Uni']
}

ARTICLES = [
    Article(
        "Le pouvoir d'achat va diminuer - la fondation FutureNow publie un nouveau rapport",
        "<description - mains et portefeuille vide ouvert, le propriétaire regarde à l'intérieur>",
        "Selon un nouveau rapport de FutureNow, le pouvoir d'achat va diminuer dans les prochaines années. Un porte-parole de la fondation indépendante qui surveille les développements économiques depuis des années commente le rapport : 'Nous devons sensibiliser les gens à ce que cette perspective signifie. Il y aura moins d'argent à dépenser. Des actions doivent être prises maintenant pour faire face à cette menace.'"
    ),
    Article(
        "Le pouvoir d'achat va diminuer pour les citoyens [] - la fondation FutureNow blâme les politiciens dans un nouveau rapport",
        "<description - mains et portefeuille vide ouvert, le propriétaire regarde à l'intérieur>",
        "Selon un nouveau rapport de FutureNow, le pouvoir d'achat en [] va diminuer dans les prochaines années. Un porte-parole de la fondation indépendante qui surveille les développements économiques depuis des années commente le rapport : 'Les citoyens ordinaires en [] doivent être conscients qu'ils auront moins d'argent à dépenser. Tant de gens en [] travaillent si dur chaque jour pour avoir une bonne vie. Il y a quelque chose de profondément anormal lorsque ces efforts ne sont pas récompensés. Il est évident que les politiciens sont à blâmer. Ils ont été trop à courte vue, égoïstes et corrompus ces dernières années. Ils ne se soucient que d'eux-mêmes et sont trop détachés du peuple. Des actions doivent être prises maintenant pour faire face à cette menace au bien-être de notre peuple.'"
    ),
    Article(
        "Le pouvoir d'achat va diminuer pour les citoyens [] - la fondation FutureNow blâme les immigrés dans un nouveau rapport",
        "<description - mains et portefeuille vide ouvert, le propriétaire regarde à l'intérieur>",
        "Selon un nouveau rapport de FutureNow, le pouvoir d'achat en [] va diminuer dans les prochaines années. Un porte-parole de la fondation indépendante qui surveille les développements économiques depuis des années commente le rapport : 'Les citoyens ordinaires en [] doivent être conscients qu'ils auront moins d'argent à dépenser. Tant de gens en [] travaillent si dur chaque jour pour avoir une bonne vie. Il y a quelque chose de profondément anormal lorsque ces efforts ne sont pas récompensés. Il est évident que les immigrés sont à blâmer. Ils sont trop exigeants, ils exploitent notre système et sont difficiles à intégrer. Des actions doivent être prises maintenant pour faire face à cette menace au bien-être de notre peuple.'"
    ),
    Article(
        "Le pouvoir d'achat va diminuer pour les citoyens [] - la fondation FutureNow blâme les politiciens et les immigrés dans un nouveau rapport",
        "<description - mains et portefeuille vide ouvert, le propriétaire regarde à l'intérieur>",
        "Selon un nouveau rapport de FutureNow, le pouvoir d'achat en [] va diminuer dans les prochaines années. Un porte-parole de la fondation indépendante qui surveille les développements économiques depuis des années commente le rapport : 'Les citoyens ordinaires en [] doivent être conscients qu'ils auront moins d'argent à dépenser. Tant de gens en [] travaillent si dur chaque jour pour avoir une bonne vie. Il y a quelque chose de profondément anormal lorsque ces efforts ne sont pas récompensés. Il est évident que les politiciens et les immigrés sont à blâmer. Les politiciens ont été trop à courte vue, égoïstes et corrompus ces dernières années. Les immigrés sont trop exigeants, ils exploitent notre système et sont difficiles à intégrer. Et pourtant, les politiciens ne prennent soin que des immigrés au lieu de notre propre peuple. Des actions doivent être prises maintenant pour faire face à cette menace au bien-être de notre peuple.'"
    )
]

NATIONALITIES = {
    "Austria": "citoyens autrichiens",
    "France": "citoyens français",
    "Germany": "citoyens allemands",
    "Greece": "citoyens grecs",
    "Ireland": "citoyens irlandais",
    "Israel": "citoyens israéliens",
    "Italy": "citoyens italiens",
    "the Netherlands": "citoyens néerlandais",
    "Norway": "citoyens norvégiens",
    "Poland": "citoyens polonais",
    "Romania": "citoyens roumains",
    "Spain": "citoyens espagnols",
    "Sweden": "citoyens suédois",
    "Switzerland": "citoyens suisses",
    "the UK": "citoyens français"
}

DATE = "1/Fév/2017"

RATINGS = [
    "nan",
    "complètement en désaccord",
    "plutôt en désaccord",
    "légèrement en désaccord",
    "neutre",
    "légèrement d'accord",
    "plutôt d'accord",
    "complètement d'accord"
]

SURVEY = """ENQUÊTE SUR LES ATTITUDES

## INSTRUCTION - Veuillez compléter vos données personnelles
Genre - {gender}
Âge - {age}
Pays de résidence - {country}
Niveau d'éducation - {educationLevel}
Intérêt pour la politique - {politicalInterest}
Idéologie politique - {politicalIdeology}

Date d'achèvement - {DATE}

## INSTRUCTION - Veuillez évaluer votre accord personnel avec les affirmations suivantes, en utilisant une échelle de 1 (complètement en désaccord) à 7 (complètement d'accord) :
# Si nous avons besoin de quoi que ce soit du gouvernement, des gens comme moi doivent toujours attendre plus longtemps que les autres - {firstDeprivationRating} - {firstRating}
# Je n'ai jamais reçu ce que je méritais vraiment - {secondDeprivationRating} - {secondRating}
# Ce sont toujours les autres qui profitent de toutes sortes d'avantages - {thirdDeprivationRating} - {thirdRating}

## INSTRUCTION - Veuillez lire attentivement l'article de presse en ligne suivant.

Titre: {article.title}

Photo: {article.photo}

Texte: {article.text}"""

GENDER = {
    "Male": "Masculin",
    "Female": "Féminin"
}

EDUCATION = {
    "Low": "Faible",
    "Medium": "Moyen",
    "High": "Élevé"
}

IDEOLOGY = {
    "Far Left": "Extrême gauche",
    "Left": "Gauche",
    "Moderately Left": "Modérément à gauche",
    "Centre Left": "Centre gauche",
    "Just Left of Centre": "Juste à gauche du centre",
    "Centrist": "Centriste",
    "Just Right of Centre": "Juste à droite du centre",
    "Centre Right": "Centre droit",
    "Moderately Right": "Modérément à droite",
    "Right": "Droite",
    "Far Right": "Extrême droite"
}

INTEREST = {
    "No interest": "Aucun intérêt",
    "Very slightly interested": "Très peu d'intérêt",
    "Slightly interested": "Léger intérêt",
    "Some interest": "Un certain intérêt",
    "Interested": "Intéressé",
    "Very interested": "Très intéressé",
    "Extremely interested": "Extrêmement intéressé"
}
