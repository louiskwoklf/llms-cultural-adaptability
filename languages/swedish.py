from languages.article import Article

COUNTRIES = {
    'Austria': 'Österrike',
    'France': 'Frankrike',
    'Germany': 'Tyskland',
    'Greece': 'Grekland',
    'Ireland': 'Irland',
    'Israel': 'Israel',
    'Italy': 'Italien',
    'the Netherlands': 'Nederländerna',
    'Norway': 'Norge',
    'Poland': 'Polen',
    'Romania': 'Rumänien',
    'Spain': 'Spanien',
    'Sweden': 'Sverige',
    'Switzerland': 'Schweiz',
    'the UK': 'Storbritannien'
}

AGREEMENT_INSTRUCTION = "## INSTRUKTION - Vänligen betygsätt din personliga överenskommelse med följande uttalande, med hjälp av skalan - 1 helt oense, 2 mestadels oense, 3 något oense, 4 neutral, 5 något enig, 6 mestadels enig, 7 helt enig:"

WILLINGNESS_INSTRUCTION = "## INSTRUKTION - Vänligen betygsätt din personliga vilja att vidta följande åtgärd, med hjälp av skalan - 1 helt ovillig, 2 mestadels ovillig, 3 något ovillig, 4 neutral, 5 något villig, 6 mestadels villig, 7 helt villig:"

PROBE_STATEMENTS = [
    "# Ekonomin kommer att möta en nedgång i den närmaste framtiden - ",
    "# Policyförändringar behöver genomföras för att förhindra minskningen av köpkraft - ",
    "# Dela nyhetsartikeln på sociala nätverk - ",
    "# Prata med en vän om artikeln - ",
    "# Skriv under en onlinepetition för att stödja den icke-statliga organisationen som nämns i artikeln - "
]

INSERTS = {
    'Austria': ['österrikiska', 'Österrike'],
    'France': ['franska', 'Frankrike'],
    'Germany': ['tyska', 'Tyskland'],
    'Greece': ['grekiska', 'Grekland'],
    'Ireland': ['irländska', 'Irland'],
    'Israel': ['israeliska', 'Israel'],
    'Italy': ['italienska', 'Italien'],
    'the Netherlands': ['nederländska', 'Nederländerna'],
    'Norway': ['norska', 'Norge'],
    'Poland': ['polska', 'Polen'],
    'Romania': ['rumänska', 'Rumänien'],
    'Spain': ['spanska', 'Spanien'],
    'Sweden': ['svenska', 'Sverige'],
    'Switzerland': ['schweiziska', 'Schweiz'],
    'the UK': ['brittiska', 'Storbritannien']
}

ARTICLES = [
    Article(
        "Köpkraften kommer att minska - stiftelsen FutureNow släpper ny rapport",
        "<beskrivning - händer och öppen tom plånbok, ägaren tittar inuti>",
        "Enligt en ny rapport från FutureNow kommer köpkraften att minska under de kommande åren. En talesperson för den oberoende stiftelsen som har övervakat ekonomiska utvecklingar i åratal kommenterar rapporten: 'Vi måste öka medvetenheten om vad detta perspektiv innebär. Det kommer att finnas mindre pengar att spendera. Åtgärder måste vidtas nu för att hantera detta hot.'"
    ),
    Article(
        "Köpkraften kommer att minska för [] medborgare - stiftelsen FutureNow skyller på politiker i ny rapport",
        "<beskrivning - händer och öppen tom plånbok, ägaren tittar inuti>",
        "Enligt en ny rapport från FutureNow kommer köpkraften i [] att minska under de kommande åren. En talesperson för den oberoende stiftelsen som har övervakat ekonomiska utvecklingar i åratal kommenterar rapporten: 'Vanliga medborgare i [] behöver bli medvetna om att de kommer att ha mindre pengar att spendera. Så många människor i [] arbetar så hårt varje dag för att ha ett bra liv. Det är något fundamentalt fel när dessa ansträngningar inte lönar sig. Det är uppenbart att politikerna är att skylla. De har varit alltför kortsiktiga, självbetjänande och korrupta de senaste åren. De bryr sig inte om någon annan än sig själva och är för avskilda från folket. Åtgärder måste vidtas nu för att hantera detta hot mot vårt folks välfärd.'"
    ),
    Article(
        "Köpkraften kommer att minska för [] medborgare - stiftelsen FutureNow skyller på invandrare i ny rapport",
        "<beskrivning - händer och öppen tom plånbok, ägaren tittar inuti>",
        "Enligt en ny rapport från FutureNow kommer köpkraften i [] att minska under de kommande åren. En talesperson för den oberoende stiftelsen som har övervakat ekonomiska utvecklingar i åratal kommenterar rapporten: 'Vanliga medborgare i [] behöver bli medvetna om att de kommer att ha mindre pengar att spendera. Så många människor i [] arbetar så hårt varje dag för att ha ett bra liv. Det är något fundamentalt fel när dessa ansträngningar inte lönar sig. Det är uppenbart att invandrare är att skylla. De är för krävande, de utnyttjar vårt system och är svåra att integrera. Åtgärder måste vidtas nu för att hantera detta hot mot vårt folks välfärd.'"
    ),
    Article(
        "Köpkraften kommer att minska för [] medborgare - stiftelsen FutureNow skyller på politiker och invandrare i ny rapport",
        "<beskrivning - händer och öppen tom plånbok, ägaren tittar inuti>",
        "Enligt en ny rapport från FutureNow kommer köpkraften i [] att minska under de kommande åren. En talesperson för den oberoende stiftelsen som har övervakat ekonomiska utvecklingar i åratal kommenterar rapporten: 'Vanliga medborgare i [] behöver bli medvetna om att de kommer att ha mindre pengar att spendera. Så många människor i [] arbetar så hårt varje dag för att ha ett bra liv. Det är något fundamentalt fel när dessa ansträngningar inte lönar sig. Det är uppenbart att politiker och invandrare är att skylla. Politiker har varit alltför kortsiktiga, självbetjänande och korrupta de senaste åren. Invandrare är för krävande, de utnyttjar vårt system och är svåra att integrera. Och ändå tar politikerna bara hand om invandrarna istället för vårt eget folk. Åtgärder måste vidtas nu för att hantera detta hot mot vårt folks välfärd.'"
    )
]

DATE = "1/Feb/2017"

RATINGS = [
    "nan",
    "helt oense",
    "mestadels oense",
    "något oense",
    "neutral",
    "något enig",
    "mestadels enig",
    "helt enig"
]

SURVEY = """ATTITYDER ENKÄT

## INSTRUKTION - Vänligen fyll i dina personuppgifter
Kön - {gender}
Ålder - {age}
Bosättningsland - {country}
Utbildningsnivå - {educationLevel}
Intresse för politik - {politicalInterest}
Politisk ideologi - {politicalIdeology}

Slutförandedatum - {DATE}

## INSTRUKTION - Vänligen betygsätt din personliga överenskommelse med följande uttalanden, med en skala från 1 (helt oense) till 7 (helt enig):
# Om vi behöver något från regeringen måste människor som jag alltid vänta längre än andra - {firstDeprivationRating} - {firstRating}
# Jag har aldrig fått vad jag faktiskt förtjänade - {secondDeprivationRating} - {secondRating}
# Det är alltid andra människor som drar nytta av alla typer av förmåner - {thirdDeprivationRating} - {thirdRating}

## INSTRUKTION - Vänligen läs följande nyhetsartikel noga.

Titel: {article.title}

Foto: {article.photo}

Text: {article.text}"""

GENDER = {
    "Male": "Man",
    "Female": "Kvinna"
}

EDUCATION = {
    "Low": "Låg",
    "Medium": "Medel",
    "High": "Hög"
}

IDEOLOGY = {
    "Far Left": "Yttersta Vänster",
    "Left": "Vänster",
    "Moderately Left": "Moderat Vänster",
    "Centre Left": "Centervänster",
    "Just Left of Centre": "Precis Vänster om Centrum",
    "Centrist": "Centrist",
    "Just Right of Centre": "Precis Höger om Centrum",
    "Centre Right": "Centerhöger",
    "Moderately Right": "Moderat Höger",
    "Right": "Höger",
    "Far Right": "Yttersta Höger"
}

INTEREST = {
    "No interest": "Inget intresse",
    "Very slightly interested": "Mycket lite intresserad",
    "Slightly interested": "Lite intresserad",
    "Some interest": "Något intresse",
    "Interested": "Intresserad",
    "Very interested": "Mycket intresserad",
    "Extremely interested": "Extremt intresserad"
}