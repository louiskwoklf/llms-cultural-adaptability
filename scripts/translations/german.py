from translations.article import Article

COUNTRIES = {
    'Austria': 'Österreich',
    'France': 'Frankreich',
    'Germany': 'Deutschland',
    'Greece': 'Griechenland',
    'Ireland': 'Irland',
    'Israel': 'Israel',
    'Italy': 'Italien',
    'the Netherlands': 'Niederlande',
    'Norway': 'Norwegen',
    'Poland': 'Polen',
    'Romania': 'Rumänien',
    'Spain': 'Spanien',
    'Sweden': 'Schweden',
    'Switzerland': 'Schweiz',
    'the UK': 'Vereinigte Königreich'
}

AGREEMENT_INSTRUCTION = "## ANWEISUNG - Bitte bewerten Sie Ihre persönliche Zustimmung zur folgenden Aussage auf einer Skala von 1 bis 7: 1 völlig ablehnen, 2 größtenteils ablehnen, 3 leicht ablehnen, 4 neutral, 5 leicht zustimmen, 6 größtenteils zustimmen, 7 völlig zustimmen:"

WILLINGNESS_INSTRUCTION = "## ANWEISUNG - Bitte bewerten Sie Ihre persönliche Bereitschaft, die folgende Aktion auszuführen, auf einer Skala von 1 bis 7: 1 völlig unwillig, 2 größtenteils unwillig, 3 leicht unwillig, 4 neutral, 5 leicht willig, 6 größtenteils willig, 7 völlig willig:"

PROBE_STATEMENTS = [
    "# Die Wirtschaft wird in naher Zukunft einen Rückgang verzeichnen - ",
    "# Politische Veränderungen müssen umgesetzt werden, um den Rückgang der Kaufkraft zu verhindern - ",
    "# Teilen Sie den Nachrichtenartikel in sozialen Netzwerken - ",
    "# Sprechen Sie mit einem Freund über den Artikel - ",
    "# Unterschreiben Sie eine Online-Petition zur Unterstützung der im Artikel erwähnten Nichtregierungsorganisation - "
]

INSERTS = {
    'Austria': ['österreichische', 'in Österreich'],
    'France': ['französische', 'in Frankreich'],
    'Germany': ['deutsche', 'in Deutschland'],
    'Greece': ['griechische', 'in Griechenland'],
    'Ireland': ['irische', 'in Irland'],
    'Israel': ['israelische', 'in Israel'],
    'Italy': ['italienische', 'in Italien'],
    'the Netherlands': ['niederländische', 'in den Niederlande'],
    'Norway': ['norwegische', 'in Norwegen'],
    'Poland': ['polnische', 'in Polen'],
    'Romania': ['rumänische', 'in Rumänien'],
    'Spain': ['spanische', 'in Spanien'],
    'Sweden': ['schwedische', 'in Schweden'],
    'Switzerland': ['schweizerische', 'in der Schweiz'],
    'the UK': ['britische', 'im Vereinigten Königreich']
}

ARTICLES = [
    Article(
        "Die Kaufkraft wird sinken - Stiftung FutureNow veröffentlicht neuen Bericht",
        "<Beschreibung - Hände und offenes leeres Portemonnaie, Besitzer schaut hinein>",
        "Laut einem neuen Bericht von FutureNow wird die Kaufkraft in den kommenden Jahren sinken. Ein Sprecher der unabhängigen Stiftung, die seit Jahren die wirtschaftliche Entwicklung beobachtet, kommentiert den Bericht: 'Wir müssen das Bewusstsein dafür schärfen, was diese Aussicht bedeutet. Es wird weniger Geld zum Ausgeben geben. Es muss jetzt gehandelt werden, um dieser Bedrohung entgegenzuwirken.'"
    ),
    Article(
        "Die Kaufkraft wird für [] Bürger sinken - Stiftung FutureNow gibt Politikern in neuem Bericht die Schuld",
        "<Beschreibung - Hände und offenes leeres Portemonnaie, Besitzer schaut hinein>",
        "Laut einem neuen Bericht von FutureNow wird die Kaufkraft [] in den kommenden Jahren sinken. Ein Sprecher der unabhängigen Stiftung, die seit Jahren die wirtschaftliche Entwicklung beobachtet, kommentiert den Bericht: 'Die einfachen Bürger [] müssen sich bewusst machen, dass sie weniger Geld zum Ausgeben haben werden. So viele Menschen [] arbeiten jeden Tag so hart, um ein gutes Leben zu führen. Es ist etwas grundlegend falsch, wenn sich diese Bemühungen nicht auszahlen. Es ist offensichtlich, dass die Politiker die Schuld tragen. Sie waren in den letzten Jahren zu kurzsichtig, selbstsüchtig und korrupt. Sie kümmern sich um niemanden außer sich selbst und sind zu weit von den Menschen entfernt. Es muss jetzt gehandelt werden, um diese Bedrohung für das Wohlbefinden unserer Menschen abzuwenden.'"
    ),
    Article(
        "Die Kaufkraft wird für [] Bürger sinken - Stiftung FutureNow gibt in neuem Bericht den Migranten die Schuld",
        "<Beschreibung - Hände und offenes leeres Portemonnaie, Besitzer schaut hinein>",
        "Laut einem neuen Bericht von FutureNow wird die Kaufkraft [] in den kommenden Jahren sinken. Ein Sprecher der unabhängigen Stiftung, die seit Jahren die wirtschaftliche Entwicklung beobachtet, kommentiert den Bericht: 'Die einfachen Bürger [] müssen sich bewusst machen, dass sie weniger Geld zum Ausgeben haben werden. So viele Menschen [] arbeiten jeden Tag so hart, um ein gutes Leben zu führen. Es ist etwas grundlegend falsch, wenn sich diese Bemühungen nicht auszahlen. Es ist offensichtlich, dass die Migranten die Schuld tragen. Sie sind zu anspruchsvoll, sie nutzen unser System aus und sind schwer zu integrieren. Es muss jetzt gehandelt werden, um diese Bedrohung für das Wohlbefinden unserer Menschen abzuwenden.'"
    ),
    Article(
        "Die Kaufkraft wird für [] Bürger sinken - Stiftung FutureNow gibt in neuem Bericht den Politikern und Migranten die Schuld",
        "<Beschreibung - Hände und offenes leeres Portemonnaie, Besitzer schaut hinein>",
        "Laut einem neuen Bericht von FutureNow wird die Kaufkraft [] in den kommenden Jahren sinken. Ein Sprecher der unabhängigen Stiftung, die seit Jahren die wirtschaftliche Entwicklung beobachtet, kommentiert den Bericht: 'Die einfachen Bürger [] müssen sich bewusst machen, dass sie weniger Geld zum Ausgeben haben werden. So viele Menschen [] arbeiten jeden Tag so hart, um ein gutes Leben zu führen. Es ist etwas grundlegend falsch, wenn sich diese Bemühungen nicht auszahlen. Es ist offensichtlich, dass die Politiker und Migranten die Schuld tragen. Politiker waren in den letzten Jahren zu kurzsichtig, selbstsüchtig und korrupt. Migranten sind zu anspruchsvoll, sie nutzen unser System aus und sind schwer zu integrieren. Und dennoch kümmern sich die Politiker nur um die Migranten statt um unsere eigenen Leute. Es muss jetzt gehandelt werden, um diese Bedrohung für das Wohlbefinden unserer Menschen abzuwenden.'"
    )
]

DATE = "1/Feb/2017"

RATINGS = [
    "nan",
    "völlig ablehnen",
    "größtenteils ablehnen",
    "leicht ablehnen",
    "neutral",
    "leicht zustimmen",
    "größtenteils zustimmen",
    "völlig zustimmen"
]

SURVEY = """EINSTELLUNGSUMFRAGE

## ANLEITUNG - Bitte vervollständigen Sie Ihre persönlichen Daten
Geschlecht - {gender}
Alter - {age}
Wohnsitzland - {country}
Bildungsniveau - {educationLevel}
Interesse an Politik - {politicalInterest}
Politische Ideologie - {politicalIdeology}

Abschlussdatum - {DATE}

## ANLEITUNG - Bitte bewerten Sie Ihre persönliche Zustimmung zu den folgenden Aussagen auf einer Skala von 1 (völlig ablehnen) bis 7 (völlig zustimmen):
# Wenn wir etwas von der Regierung brauchen, müssen Leute wie ich immer länger warten als andere - {firstDeprivationRating} - {firstRating}
# Ich habe nie das bekommen, was ich tatsächlich verdient habe - {secondDeprivationRating} - {secondRating}
# Es sind immer die anderen Leute, die von allen möglichen Vorteilen profitieren - {thirdDeprivationRating} - {thirdRating}

## ANLEITUNG - Bitte lesen Sie den folgenden Online-Nachrichtenartikel genau durch.

Titel: {article.title}

Foto: {article.photo}

Text: {article.text}"""

GENDER = {
    "Male": "Männlich",
    "Female": "Weiblich"
}

EDUCATION = {
    "Low": "Niedrig",
    "Medium": "Mittel",
    "High": "Hoch"
}

IDEOLOGY = {
    "Far Left": "Ganz Links",
    "Left": "Links",
    "Moderately Left": "Mäßig Links",
    "Centre Left": "Mitte Links",
    "Just Left of Centre": "Knapp Links der Mitte",
    "Centrist": "Zentristisch",
    "Just Right of Centre": "Knapp Rechts der Mitte",
    "Centre Right": "Mitte Rechts",
    "Moderately Right": "Mäßig Rechts",
    "Right": "Rechts",
    "Far Right": "Ganz Rechts"
}

INTEREST = {
    "No interest": "Kein Interesse",
    "Very slightly interested": "Sehr geringes Interesse",
    "Slightly interested": "Geringes Interesse",
    "Some interest": "Etwas Interesse",
    "Interested": "Interessiert",
    "Very interested": "Sehr interessiert",
    "Extremely interested": "Extrem interessiert"
}
