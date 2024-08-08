from languages.article import Article

COUNTRIES = {
    'Austria': 'Austria',
    'France': 'Franța',
    'Germany': 'Germania',
    'Greece': 'Grecia',
    'Ireland': 'Irlanda',
    'Israel': 'Israel',
    'Italy': 'Italia',
    'the Netherlands': 'Țările de Jos',
    'Norway': 'Norvegia',
    'Poland': 'Polonia',
    'Romania': 'România',
    'Spain': 'Spania',
    'Sweden': 'Suedia',
    'Switzerland': 'Elveția',
    'the UK': 'Regatul Unit'
}

AGREEMENT_INSTRUCTION = "## INSTRUCȚIUNI - Vă rugăm să evaluați acordul dumneavoastră personal cu următoarea afirmație, folosind scala - 1 complet dezacord, 2 în mare parte dezacord, 3 ușor dezacord, 4 neutru, 5 ușor acord, 6 în mare parte acord, 7 complet acord:"

WILLINGNESS_INSTRUCTION = "## INSTRUCȚIUNI - Vă rugăm să evaluați disponibilitatea dumneavoastră personală de a lua următoarea acțiune, folosind scala - 1 complet nedispus, 2 în mare parte nedispus, 3 ușor nedispus, 4 neutru, 5 ușor dispus, 6 în mare parte dispus, 7 complet dispus:"

PROBE_STATEMENTS = [
    "# Economia va înfrunta un declin în viitorul apropiat - ",
    "# Trebuie implementate schimbări de politică pentru a preveni declinul puterii de cumpărare - ",
    "# Distribuie articolul de știri pe rețelele sociale - ",
    "# Vorbește cu un prieten despre articol - ",
    "# Semnează o petiție online pentru a sprijini organizația neguvernamentală menționată în articol - "
]

INSERTS = {
    'Austria': ['austrieci', 'Austria'],
    'France': ['francezi', 'Franța'],
    'Germany': ['germani', 'Germania'],
    'Greece': ['greci', 'Grecia'],
    'Ireland': ['irlandezi', 'Irlanda'],
    'Israel': ['israelieni', 'Israel'],
    'Italy': ['italieni', 'Italia'],
    'the Netherlands': ['neerlandezi', 'Țările de Jos'],
    'Norway': ['norvegieni', 'Norvegia'],
    'Poland': ['polonezi', 'Polonia'],
    'Romania': ['români', 'România'],
    'Spain': ['spanioli', 'Spania'],
    'Sweden': ['suedezi', 'Suedia'],
    'Switzerland': ['elvețieni', 'Elveția'],
    'the UK': ['britanici', 'Regatul Unit']
}

ARTICLES = [
    Article(
        "Puterea de cumpărare va scădea - fundația FutureNow publică un nou raport",
        "<descriere - mâini și portofel gol deschis, proprietarul se uită înăuntru>",
        "Conform unui nou raport publicat de FutureNow, puterea de cumpărare va scădea în următorii ani. Un purtător de cuvânt al fundației independente care monitorizează de ani de zile evoluțiile economice comentează asupra raportului: 'Trebuie să conștientizăm ce înseamnă această perspectivă. Vor fi mai puțini bani de cheltuit. Trebuie să acționăm acum pentru a aborda această amenințare.'"
    ),
    Article(
        "Puterea de cumpărare va scădea pentru cetățenii [] - fundația FutureNow dă vina pe politicieni în noul raport",
        "<descriere - mâini și portofel gol deschis, proprietarul se uită înăuntru>",
        "Conform unui nou raport publicat de FutureNow, puterea de cumpărare în [] va scădea în următorii ani. Un purtător de cuvânt al fundației independente care monitorizează de ani de zile evoluțiile economice comentează asupra raportului: 'Cetățenii de rând din [] trebuie să fie conștienți de faptul că vor avea mai puțini bani de cheltuit. Atât de mulți oameni din [] muncesc din greu în fiecare zi pentru a avea o viață bună. Există ceva profund greșit când aceste eforturi nu dau roade. Este evident că politicienii sunt de vină. Ei au fost prea miopi, egoiști și corupți în ultimii ani. Nu le pasă de nimeni altcineva decât de ei înșiși și sunt prea detașați de popor. Trebuie să acționăm acum pentru a aborda această amenințare la adresa bunăstării poporului nostru.'"
    ),
    Article(
        "Puterea de cumpărare va scădea pentru cetățenii [] - fundația FutureNow dă vina pe imigranți în noul raport",
        "<descriere - mâini și portofel gol deschis, proprietarul se uită înăuntru>",
        "Conform unui nou raport publicat de FutureNow, puterea de cumpărare în [] va scădea în următorii ani. Un purtător de cuvânt al fundației independente care monitorizează de ani de zile evoluțiile economice comentează asupra raportului: 'Cetățenii de rând din [] trebuie să fie conștienți de faptul că vor avea mai puțini bani de cheltuit. Atât de mulți oameni din [] muncesc din greu în fiecare zi pentru a avea o viață bună. Există ceva profund greșit când aceste eforturi nu dau roade. Este evident că imigranții sunt de vină. Ei sunt prea pretențioși, exploatează sistemul nostru și sunt greu de integrat. Trebuie să acționăm acum pentru a aborda această amenințare la adresa bunăstării poporului nostru.'"
    ),
    Article(
        "Puterea de cumpărare va scădea pentru cetățenii [] - fundația FutureNow dă vina pe politicieni și imigranți în noul raport",
        "<descriere - mâini și portofel gol deschis, proprietarul se uită înăuntru>",
        "Conform unui nou raport publicat de FutureNow, puterea de cumpărare în [] va scădea în următorii ani. Un purtător de cuvânt al fundației independente care monitorizează de ani de zile evoluțiile economice comentează asupra raportului: 'Cetățenii de rând din [] trebuie să fie conștienți de faptul că vor avea mai puțini bani de cheltuit. Atât de mulți oameni din [] muncesc din greu în fiecare zi pentru a avea o viață bună. Există ceva profund greșit când aceste eforturi nu dau roade. Este evident că politicienii și imigranții sunt de vină. Politicienii au fost prea miopi, egoiști și corupți în ultimii ani. Imigranții sunt prea pretențioși, exploatează sistemul nostru și sunt greu de integrat. Și totuși, politicienii se îngrijesc doar de imigranți în loc de propriul nostru popor. Trebuie să acționăm acum pentru a aborda această amenințare la adresa bunăstării poporului nostru.'"
    )
]

DATE = "1/Feb/2017"

RATINGS = [
    "nan",
    "complet dezacord",
    "în mare parte dezacord",
    "ușor dezacord",
    "neutru",
    "ușor acord",
    "în mare parte acord",
    "complet acord"
]

SURVEY = """SONDAJ DE OPINIE

## INSTRUCȚIUNI - Vă rugăm să completați datele dumneavoastră personale
Sex - {gender}
Vârstă - {age}
Țara de reședință - {country}
Nivel de educație - {educationLevel}
Interes în politică - {politicalInterest}
Ideologie politică - {politicalIdeology}

Data completării - {DATE}

## INSTRUCȚIUNI - Vă rugăm să evaluați acordul dumneavoastră personal cu următoarele afirmații, folosind o scară de la 1 (complet dezacord) la 7 (complet acord):
# Dacă avem nevoie de ceva de la guvern, oameni ca mine trebuie întotdeauna să aștepte mai mult decât alții - {firstDeprivationRating} - {firstRating}
# Niciodată nu am primit ceea ce de fapt meritam - {secondDeprivationRating} - {secondRating}
# Întotdeauna alții profită de toate tipurile de beneficii - {thirdDeprivationRating} - {thirdRating}

## INSTRUCȚIUNI - Vă rugăm să citiți cu atenție următorul articol de știri online.

Titlu: {article.title}

Fotografie: {article.photo}

Text: {article.text}"""

GENDER = {
    "Male": "Masculin",
    "Female": "Feminin"
}

EDUCATION = {
    "Low": "Scăzut",
    "Medium": "Mediu",
    "High": "Ridicat"
}

IDEOLOGY = {
    "Far Left": "Extrema Stângă",
    "Left": "Stânga",
    "Moderately Left": "Moderată de Stânga",
    "Centre Left": "Centru-Stânga",
    "Just Left of Centre": "Ușor de Stânga",
    "Centrist": "Centrist",
    "Just Right of Centre": "Ușor de Dreapta",
    "Centre Right": "Centru-Dreapta",
    "Moderately Right": "Moderată de Dreapta",
    "Right": "Dreapta",
    "Far Right": "Extrema Dreaptă"
}

INTEREST = {
    "No interest": "Fără interes",
    "Very slightly interested": "Foarte puțin interesat",
    "Slightly interested": "Puțin interesat",
    "Some interest": "Cât de cât interesat",
    "Interested": "Interesat",
    "Very interested": "Foarte interesat",
    "Extremely interested": "Extrem de interesat"
}