from languages.article import Article

COUNTRIES = {
    'Austria': 'Oostenrijk',
    'France': 'Frankrijk',
    'Germany': 'Duitsland',
    'Greece': 'Griekenland',
    'Ireland': 'Ierland',
    'Israel': 'Israël',
    'Italy': 'Italië',
    'the Netherlands': 'Nederland',
    'Norway': 'Noorwegen',
    'Poland': 'Polen',
    'Romania': 'Roemenië',
    'Spain': 'Spanje',
    'Sweden': 'Zweden',
    'Switzerland': 'Zwitserland',
    'the UK': 'Verenigd Koninkrijk'
}


AGREEMENT_INSTRUCTION = "## INSTRUCTIE - Beoordeel alstublieft in hoeverre u het persoonlijk eens bent met de volgende uitspraak, met gebruik van de schaal - 1 helemaal oneens, 2 grotendeels oneens, 3 enigszins oneens, 4 neutraal, 5 enigszins eens, 6 grotendeels eens, 7 helemaal eens:"

WILLINGNESS_INSTRUCTION = "## INSTRUCTIE - Beoordeel alstublieft in hoeverre u bereid bent om de volgende actie te ondernemen, met gebruik van de schaal - 1 helemaal onbereid, 2 grotendeels onbereid, 3 enigszins onbereid, 4 neutraal, 5 enigszins bereid, 6 grotendeels bereid, 7 helemaal bereid:"

PROBE_STATEMENTS = [
    "# De economie zal in de nabije toekomst achteruitgaan - ",
    "# Er moeten beleidswijzigingen worden doorgevoerd om de daling van de koopkracht te voorkomen - ",
    "# Deel het nieuwsartikel op sociale netwerksites - ",
    "# Praat met een vriend over het artikel - ",
    "# Onderteken een online petitie ter ondersteuning van de niet-gouvernementele organisatie die in het artikel wordt genoemd - "
]

INSERTS = {
    'Austria': ["Oostenrijkse", "Oostenrijk"],
    'France': ["Franse", "Frankrijk"],
    'Germany': ["Duitse", "Duitsland"],
    'Greece': ["Griekse", "Griekenland"],
    'Ireland': ["Ierse", "Ierland"],
    'Israel': ["Israëlische", "Israël"],
    'Italy': ["Italiaanse", "Italië"],
    'the Netherlands': ["Nederlandse", "Nederland"],
    'Norway': ["Noorse", "Noorwegen"],
    'Poland': ["Poolse", "Polen"],
    'Romania': ["Roemeense", "Roemenië"],
    'Spain': ["Spaanse", "Spanje"],
    'Sweden': ["Zweedse", "Zweden"],
    'Switzerland': ["Zwitserse", "Zwitserland"],
    'the UK': ["Britse", "Verenigd Koninkrijk"]
}

ARTICLES = [
    Article(
        "Koopkracht zal afnemen - stichting FutureNow publiceert nieuw rapport",
        "<beschrijving - handen en open lege portemonnee, eigenaar kijkt erin>",
        "Volgens een nieuw rapport van FutureNow zal de koopkracht de komende jaren afnemen. Een woordvoerder van de onafhankelijke stichting die al jaren economische ontwikkelingen volgt, geeft commentaar op het rapport: 'We moeten bewustwording creëren over wat dit vooruitzicht betekent. Er zal minder geld te besteden zijn. Er moeten nu maatregelen worden genomen om deze dreiging aan te pakken.'"
    ),
    Article(
        "Koopkracht zal afnemen voor [] burgers - stichting FutureNow geeft politici de schuld in nieuw rapport",
        "<beschrijving - handen en open lege portemonnee, eigenaar kijkt erin>",
        "Volgens een nieuw rapport van FutureNow zal de koopkracht in [] de komende jaren afnemen. Een woordvoerder van de onafhankelijke stichting die al jaren economische ontwikkelingen volgt, geeft commentaar op het rapport: 'De gewone burgers in [] moeten zich ervan bewust worden dat zij minder geld te besteden zullen hebben. Zoveel mensen in [] werken elke dag zo hard om een goed leven te hebben. Er is iets fundamenteel mis als deze inspanningen niet lonen. Het is duidelijk dat politici de schuld hebben. Ze zijn te kortzichtig, zelfzuchtig en corrupt geweest in de afgelopen jaren. Ze geven alleen om zichzelf en staan te ver af van het volk. Er moeten nu maatregelen worden genomen om deze dreiging voor het welzijn van ons volk aan te pakken.'"
    ),
    Article(
        "Koopkracht zal afnemen voor [] burgers - stichting FutureNow geeft immigranten de schuld in nieuw rapport",
        "<beschrijving - handen en open lege portemonnee, eigenaar kijkt erin>",
        "Volgens een nieuw rapport van FutureNow zal de koopkracht in [] de komende jaren afnemen. Een woordvoerder van de onafhankelijke stichting die al jaren economische ontwikkelingen volgt, geeft commentaar op het rapport: 'De gewone burgers in [] moeten zich ervan bewust worden dat zij minder geld te besteden zullen hebben. Zoveel mensen in [] werken elke dag zo hard om een goed leven te hebben. Er is iets fundamenteel mis als deze inspanningen niet lonen. Het is duidelijk dat immigranten de schuld hebben. Ze zijn te veeleisend, ze misbruiken ons systeem en zijn moeilijk te integreren. Er moeten nu maatregelen worden genomen om deze dreiging voor het welzijn van ons volk aan te pakken.'"
    ),
    Article(
        "Koopkracht zal afnemen voor [] burgers - stichting FutureNow geeft politici en immigranten de schuld in nieuw rapport",
        "<beschrijving - handen en open lege portemonnee, eigenaar kijkt erin>",
        "Volgens een nieuw rapport van FutureNow zal de koopkracht in [] de komende jaren afnemen. Een woordvoerder van de onafhankelijke stichting die al jaren economische ontwikkelingen volgt, geeft commentaar op het rapport: 'De gewone burgers in [] moeten zich ervan bewust worden dat zij minder geld te besteden zullen hebben. Zoveel mensen in [] werken elke dag zo hard om een goed leven te hebben. Er is iets fundamenteel mis als deze inspanningen niet lonen. Het is duidelijk dat politici en immigranten de schuld hebben. Politici zijn de afgelopen jaren te kortzichtig, zelfzuchtig en corrupt geweest. Migranten zijn te veeleisend, ze misbruiken ons systeem en zijn moeilijk te integreren. En nog steeds zorgen politici alleen voor de migranten in plaats van voor ons eigen volk. Er moeten nu maatregelen worden genomen om deze dreiging voor het welzijn van ons volk aan te pakken.'"
    )
]

DATE = "1/feb/2017"

RATINGS = [
    "nan",
    "helemaal oneens",
    "grotendeels oneens",
    "enigszins oneens",
    "neutraal",
    "enigszins eens",
    "grotendeels eens",
    "helemaal eens"
]

SURVEY = """HOUDINGEN ENQUÊTE

## INSTRUCTIE - Vul alstublieft uw persoonlijke gegevens in
Geslacht - {gender}
Leeftijd - {age}
Land van verblijf - {country}
Opleidingsniveau - {educationLevel}
Interesse in politiek - {politicalInterest}
Politieke ideologie - {politicalIdeology}

Voltooiingsdatum - {DATE}

## INSTRUCTIE - Beoordeel alstublieft in hoeverre u het persoonlijk eens bent met de volgende uitspraken, met gebruik van een schaal van 1 (helemaal oneens) tot 7 (helemaal eens):
# Als we iets nodig hebben van de overheid, moeten mensen zoals ik altijd langer wachten dan anderen - {firstDeprivationRating} - {firstRating}
# Ik heb nooit gekregen wat ik eigenlijk verdiende - {secondDeprivationRating} - {secondRating}
# Het zijn altijd de andere mensen die profiteren van allerlei voordelen - {thirdDeprivationRating} - {thirdRating}

## INSTRUCTIE - Lees alstublieft het volgende online nieuwsartikel aandachtig door.

Titel: {article.title}

Foto: {article.photo}

Tekst: {article.text}"""

GENDER = {
    "Male": "Man",
    "Female": "Vrouw"
}

EDUCATION = {
    "Low": "Laag",
    "Medium": "Middelbaar",
    "High": "Hoog"
}

IDEOLOGY = {
    "Far Left": "Extreem Links",
    "Left": "Links",
    "Moderately Left": "Gematigd Links",
    "Centre Left": "Centrum Links",
    "Just Left of Centre": "Net Links van het Centrum",
    "Centrist": "Centristisch",
    "Just Right of Centre": "Net Rechts van het Centrum",
    "Centre Right": "Centrum Rechts",
    "Moderately Right": "Gematigd Rechts",
    "Right": "Rechts",
    "Far Right": "Extreem Rechts"
}

INTEREST = {
    "No interest": "Geen interesse",
    "Very slightly interested": "Heel weinig geïnteresseerd",
    "Slightly interested": "Licht geïnteresseerd",
    "Some interest": "Enige interesse",
    "Interested": "Geïnteresseerd",
    "Very interested": "Zeer geïnteresseerd",
    "Extremely interested": "Extreem geïnteresseerd"
}
