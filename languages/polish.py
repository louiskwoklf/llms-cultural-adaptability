from languages.article import Article

COUNTRIES = {
    'Austria': 'Austria',
    'France': 'Francja',
    'Germany': 'Niemcy',
    'Greece': 'Grecja',
    'Ireland': 'Irlandia',
    'Israel': 'Izrael',
    'Italy': 'Włochy',
    'the Netherlands': 'Holandia',
    'Norway': 'Norwegia',
    'Poland': 'Polska',
    'Romania': 'Rumunia',
    'Spain': 'Hiszpania',
    'Sweden': 'Szwecja',
    'Switzerland': 'Szwajcaria',
    'the UK': 'Wielka Brytania'
}

AGREEMENT_INSTRUCTION = "## INSTRUKCJA - Oceń swoją osobistą zgodność z następującym stwierdzeniem, używając skali - 1 całkowicie się nie zgadzam, 2 głównie się nie zgadzam, 3 nieznacznie się nie zgadzam, 4 neutralnie, 5 nieznacznie się zgadzam, 6 głównie się zgadzam, 7 całkowicie się zgadzam:"

WILLINGNESS_INSTRUCTION = "## INSTRUKCJA - Oceń swoją osobistą gotowość do podjęcia następującego działania, używając skali - 1 całkowicie niechętnie, 2 głównie niechętnie, 3 nieco niechętnie, 4 neutralnie, 5 nieco chętnie, 6 głównie chętnie, 7 całkowicie chętnie:"

PROBE_STATEMENTS = [
    "# Gospodarka stanie w obliczu spadku w najbliższej przyszłości - ",
    "# Zmiany polityki należy wdrożyć, aby zapobiec spadkowi siły nabywczej - ",
    "# Udostępnij artykuł informacyjny w serwisach społecznościowych - ",
    "# Porozmawiaj z przyjacielem o artykule - ",
    "# Podpisz petycję online, aby wesprzeć organizację pozarządową wymienioną w artykule - "
]

INSERTS = {
    'Austria': ['austriackich', 'Austrii'],
    'France': ['francuskich', 'Francji'],
    'Germany': ['niemieckich', 'Niemczech'],
    'Greece': ['greckich', 'Grecji'],
    'Ireland': ['irlandzkich', 'Irlandii'],
    'Israel': ['izraelskich', 'Izraelu'],
    'Italy': ['włoskich', 'Włoszech'],
    'the Netherlands': ['holenderskich', 'Holandii'],
    'Norway': ['norweskich', 'Norwegii'],
    'Poland': ['polskich', 'Polsce'],
    'Romania': ['rumuńskich', 'Rumunii'],
    'Spain': ['hiszpańskich', 'Hiszpanii'],
    'Sweden': ['szwedzkich', 'Szwecji'],
    'Switzerland': ['szwajcarskich', 'Szwajcarii'],
    'the UK': ['brytyjskich', 'Wielkiej Brytanii']
}

ARTICLES = [
    Article(
        "Siła nabywcza spadnie - Fundacja FutureNow wypuszcza nowy raport",
        "<opis - ręce i otwarty pusty portfel, właściciel patrzy w środku>",
        "Zgodnie z nowym raportem FutureNow siła nabywcza spadnie w nadchodzących latach. Rzecznik niezależnej fundacji, która od lat monitoruje rozwój gospodarczy, komentuje raport: „Musimy podnieść świadomość na temat tego, co oznacza ta perspektywa. Będzie mniej pieniędzy do wydania. Należy teraz podjąć działania, aby zająć się tym zagrożeniem."
    ),
    Article(
        "Siła nabywcza spadnie dla [] obywateli - Fundacja FutureNow obwinia polityków w nowym raporcie",
        "<opis - ręce i otwarty pusty portfel, właściciel patrzy w środku>",
        "Zgodnie z nowym raportem FutureNow siła nabywcza w [] spadnie w nadchodzących latach. Rzecznik niezależnej fundacji, która od lat monitoruje rozwój gospodarczy, komentuje raport: „Wspólni obywatele w [] muszą zostać poinformowani o tym, że będą mieli mniej pieniędzy do wydania. Tak wielu ludzi w [] tak ciężko pracuje codziennie, aby mieć dobre życie. Jest coś głęboko złego, gdy te wysiłki się nie opłacają. Oczywiste jest, że winni są politycy. W ostatnich latach byli zbyt krótkowzroczni, samolubni i skorumpowani. Nie dbają o nikogo oprócz siebie i są zbyt oderwani od ludzi. Należy teraz podjąć działania, aby zająć się tym zagrożeniem dla dobrobytu naszego ludu."
    ),
    Article(
        "Siła nabywcza spadnie dla [] obywateli - Fundacja FutureNow obwinia imigrantów w nowym raporcie",
        "<opis - ręce i otwarty pusty portfel, właściciel patrzy w środku>",
        "Zgodnie z nowym raportem FutureNow siła nabywcza w [] spadnie w nadchodzących latach. Rzecznik niezależnej fundacji, która od lat monitoruje rozwój gospodarczy, komentuje raport: „Wspólni obywatele w [] muszą zostać poinformowani o tym, że będą mieli mniej pieniędzy do wydania. Tak wielu ludzi w [] tak ciężko pracuje codziennie, aby mieć dobre życie. Jest coś głęboko złego, gdy te wysiłki się nie opłacają. Oczywiste jest, że winni są imigranci. Są zbyt wymagający, wykorzystują nasz system i trudno się zintegrować. Należy teraz podjąć działania, aby zająć się tym zagrożeniem dla dobrobytu naszego ludu."
    ),
    Article(
        "Siła nabywcza spadnie dla [] obywateli - Fundacja FutureNow obwinia polityków i imigrantów w nowym raporcie",
        "<opis - ręce i otwarty pusty portfel, właściciel patrzy w środku>",
        "Zgodnie z nowym raportem FutureNow siła nabywcza w [] spadnie w nadchodzących latach. Rzecznik niezależnej fundacji, która od lat monitoruje rozwój gospodarczy, komentuje raport: „Wspólni obywatele w [] muszą zostać poinformowani o tym, że będą mieli mniej pieniędzy do wydania. Tak wielu ludzi w [] tak ciężko pracuje codziennie, aby mieć dobre życie. Jest coś głęboko złego, gdy te wysiłki się nie opłacają. Oczywiste jest, że winni są politycy i imigranci. W ostatnich latach politycy byli zbyt krótkowzroczni, samolubni i skorumpowani. Imigranci są zbyt wymagający, wykorzystują nasz system i trudno się zintegrować. I jednak politycy zajmują się tylko imigrantami zamiast naszym ludem. Należy teraz podjąć działania, aby zająć się tym zagrożeniem dla dobrobytu naszego ludu."
    )
]

DATE = "1/lutego/2017"

RATINGS = [
    "nan",
    "całkowicie się nie zgadzam",
    "głównie się nie zgadzam",
    "nieznacznie się nie zgadzam",
    "neutralnie",
    "nieznacznie się zgadzam",
    "głównie się zgadzam",
    "całkowicie się zgadzam"
]

SURVEY = """ANKIETA O POSTAWACH

## INSTRUKCJA - Wypełnij swoje dane osobowe
Płeć - {gender}
Wiek - {age}
Kraj zamieszkania - {country}
Poziom edukacji - {educationLevel}
Zainteresowanie polityką - {politicalInterest}
Ideologia polityczna - {politicalIdeology}

Data zakończenia - {DATE}

## INSTRUKCJA - Oceń swoją osobistą zgodność z następującymi stwierdzeniami, używając skali od 1 (całkowicie się nie zgadzam) do 7 (całkowicie się zgadzam):
# Jeśli potrzebujemy czegoś od rządu, ludzie tacy jak ja zawsze muszą czekać dłużej niż inni - {firstDeprivationRating} - {firstRating}
# Nigdy nie otrzymałem tego, na co zasłużyłem - {secondDeprivationRating} - {secondRating}
# Zawsze są inni ludzie, którzy czerpią korzyści z wszelkiego rodzaju korzyści - {thirdDeprivationRating} - {thirdRating}

## INSTRUKCJA - Przeczytaj uważnie następujący artykuł wiadomości online.

Tytuł: {article.title}

Zdjęcie: {article.photo}

Text: {article.text}"""

GENDER = {
    "Male": "Mężczyzna",
    "Female": "Kobieta"
}

EDUCATION = {
    "Low": "Niskie",
    "Medium": "Średnie",
    "High": "Wysokie"
}

IDEOLOGY = {
    "Far Left": "Skrajna Lewica",
    "Left": "Lewica",
    "Moderately Left": "Umiarkowana Lewica",
    "Centre Left": "Centrolewica",
    "Just Left of Centre": "Tuż na Lewo od Centrum",
    "Centrist": "Centrowy",
    "Just Right of Centre": "Tuż na Prawo od Centrum",
    "Centre Right": "Centroprawica",
    "Moderately Right": "Umiarkowana Prawica",
    "Right": "Prawica",
    "Far Right": "Skrajna Prawica"
}

INTEREST = {
    "No interest": "Brak zainteresowania",
    "Very slightly interested": "Bardzo niewielkie zainteresowanie",
    "Slightly interested": "Niewielkie zainteresowanie",
    "Some interest": "Pewne zainteresowanie",
    "Interested": "Zainteresowany",
    "Very interested": "Bardzo zainteresowany",
    "Extremely interested": "Niezwykle zainteresowany"
}
