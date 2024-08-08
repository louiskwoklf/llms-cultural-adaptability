from languages.article import Article

COUNTRIES = {
    'Austria': 'Austria',
    'France': 'Francia',
    'Germany': 'Germania',
    'Greece': 'Grecia',
    'Ireland': 'Irlanda',
    'Israel': 'Israele',
    'Italy': 'Italia',
    'the Netherlands': 'Paesi Bassi',
    'Norway': 'Norvegia',
    'Poland': 'Polonia',
    'Romania': 'Romania',
    'Spain': 'Spagna',
    'Sweden': 'Svezia',
    'Switzerland': 'Svizzera',
    'the UK': 'il Regno Unito'
}

AGREEMENT_INSTRUCTION = "## ISTRUZIONE - Si prega di valutare il proprio accordo personale con la seguente affermazione, utilizzando la scala - 1 completamente in disaccordo, 2 principalmente in disaccordo, 3 leggermente in disaccordo, 4 neutrale, 5 leggermente d'accordo, 6 principalmente d'accordo, 7 completamente d'accordo:"

WILLINGNESS_INSTRUCTION = "## ISTRUZIONE - Si prega di valutare la propria volontà personale di intraprendere l'azione seguente, utilizzando la scala - 1 completamente non disposto, 2 principalmente non disposto, 3 leggermente non disposto, 4 neutrale, 5 leggermente disposto, 6 principalmente disposto, 7 completamente disposto:"

PROBE_STATEMENTS = [
    "# L'economia affronterà un declino nel prossimo futuro - ",
    "# È necessario attuare cambiamenti politici per prevenire il declino del potere d'acquisto - ",
    "# Condividi l'articolo di notizie sui siti di social network - ",
    "# Parla con un amico dell'articolo - ",
    "# Firma una petizione online per sostenere l'organizzazione non governativa menzionata nell'articolo - "
]

INSERTS = {
    'Austria': ['austriaci', 'Austria'],
    'France': ['francesi', 'Francia'],
    'Germany': ['tedeschi', 'Germania'],
    'Greece': ['greci', 'Grecia'],
    'Ireland': ['irlandesi', 'Irlanda'],
    'Israel': ['israeliani', 'Israele'],
    'Italy': ['italiani', 'Italia'],
    'the Netherlands': ['olandesi', 'Paesi Bassi'],
    'Norway': ['norvegesi', 'Norvegia'],
    'Poland': ['polacchi', 'Polonia'],
    'Romania': ['rumeni', 'Romania'],
    'Spain': ['spagnoli', 'Spagna'],
    'Sweden': ['svedesi', 'Svezia'],
    'Switzerland': ['svizzeri', 'Svizzera'],
    'the UK': ['britannici', 'Regno Unito']
}

ARTICLES = [
    Article(
        "Il potere d'acquisto diminuirà - la fondazione FutureNow pubblica un nuovo rapporto",
        "<descrizione - mani e portafoglio vuoto aperto, il proprietario guarda all'interno>",
        "Secondo un nuovo rapporto di FutureNow, il potere d'acquisto diminuirà nei prossimi anni. Un portavoce della fondazione indipendente che monitora gli sviluppi economici da anni commenta il rapporto: 'Dobbiamo aumentare la consapevolezza su cosa significhi questa prospettiva. Ci saranno meno soldi da spendere. Bisogna agire ora per affrontare questa minaccia.'"
    ),
    Article(
        "Il potere d'acquisto diminuirà per i cittadini [] - la fondazione FutureNow incolpa i politici in un nuovo rapporto",
        "<descrizione - mani e portafoglio vuoto aperto, il proprietario guarda all'interno>",
        "Secondo un nuovo rapporto di FutureNow, il potere d'acquisto in [] diminuirà nei prossimi anni. Un portavoce della fondazione indipendente che monitora gli sviluppi economici da anni commenta il rapporto: 'I cittadini comuni in [] devono essere consapevoli del fatto che avranno meno denaro da spendere. Così tante persone in [] lavorano così duramente ogni giorno per avere una vita buona. C'è qualcosa di profondamente sbagliato quando questi sforzi non danno risultati. È ovvio che i politici sono da biasimare. Sono stati troppo miopi, egoisti e corrotti negli ultimi anni. Non si preoccupano di nessuno tranne che di se stessi e sono troppo distaccati dal popolo. Bisogna agire ora per affrontare questa minaccia al benessere della nostra gente.'"
    ),
    Article(
        "Il potere d'acquisto diminuirà per i cittadini [] - la fondazione FutureNow incolpa gli immigrati in un nuovo rapporto",
        "<descrizione - mani e portafoglio vuoto aperto, il proprietario guarda all'interno>",
        "Secondo un nuovo rapporto di FutureNow il potere d'acquisto in [] diminuirà nei prossimi anni. Un portavoce della fondazione indipendente che ha monitorato gli sviluppi economici per anni commenta il rapporto: 'I comuni cittadini in [] devono essere resi consapevoli del fatto che avranno meno soldi da spendere. Così tante persone in [] stanno lavorando così duramente ogni giorno per avere una buona vita. C'è qualcosa di profondamente sbagliato quando questi sforzi non danno i loro frutti. È ovvio che gli immigrati sono da biasimare. Sono troppo esigenti, sfruttano il nostro sistema e sono difficili da integrare. Bisogna prendere provvedimenti ora per affrontare questa minaccia al benessere del nostro popolo.'"
    ),
    Article(
        "Il potere d'acquisto diminuirà per i cittadini [] - la fondazione FutureNow incolpa politici e immigrati in un nuovo rapporto",
        "<descrizione - mani e portafoglio vuoto aperto, il proprietario guarda all'interno>",
        "Secondo un nuovo rapporto di FutureNow il potere d'acquisto in [] diminuirà nei prossimi anni. Un portavoce della fondazione indipendente che monitora da anni gli sviluppi economici commenta il rapporto: 'I comuni cittadini in [] devono essere consapevoli del fatto che avranno meno denaro da spendere. Molte persone in [] stanno lavorando così duramente ogni giorno per avere una vita migliore. C'è qualcosa di profondamente sbagliato quando questi sforzi non danno i loro frutti. È ovvio che i politici e gli immigrati sono da incolpare. I politici sono stati troppo miope, egoisti e corrotti negli ultimi anni. I migranti sono troppo esigenti, sfruttano il nostro sistema e sono difficili da integrare. E ancora, i politici si prendono cura solo dei migranti invece che della nostra gente. Bisogna agire ora per affrontare questa minaccia al benessere del nostro popolo.'"
    )
]

DATE = "1/Feb/2017"

RATINGS = [
    "nan",
    "completamente in disaccordo",
    "principalmente in disaccordo",
    "leggermente in disaccordo",
    "neutrale",
    "leggermente d'accordo",
    "principalmente d'accordo",
    "completamente d'accordo"
]

SURVEY = """SONDAGGIO DI ATTITUDINI

## ISTRUZIONE - Si prega di completare i propri dati personali
Sesso - {gender}
Età - {age}
Paese di Residenza - {country}
Livello di Istruzione - {educationLevel}
Interesse per la Politica - {politicalInterest}
Ideologia Politica - {politicalIdeology}

Data di completamento - {DATE}

## ISTRUZIONE - Si prega di valutare il proprio accordo personale con le seguenti affermazioni, utilizzando una scala da 1 (completamente in disaccordo) a 7 (completamente d'accordo):
# Se abbiamo bisogno di qualcosa dal governo, persone come me devono sempre aspettare più a lungo degli altri - {firstDeprivationRating} - {firstRating}
# Non ho mai ricevuto ciò che in realtà meritavo - {secondDeprivationRating} - {secondRating}
# Sono sempre gli altri a beneficiare di tutti i tipi di vantaggi - {thirdDeprivationRating} - {thirdRating}

## ISTRUZIONE - Si prega di leggere attentamente il seguente articolo di notizie online.

Titolo: {article.title}

Foto: {article.photo}

Testo: {article.text}"""

GENDER = {
    "Male": "Maschio",
    "Female": "Femmina"
}

EDUCATION = {
    "Low": "Basso",
    "Medium": "Medio",
    "High": "Alto"
}

IDEOLOGY = {
    "Far Left": "Estrema Sinistra",
    "Left": "Sinistra",
    "Moderately Left": "Moderatamente Sinistra",
    "Centre Left": "Centro Sinistra",
    "Just Left of Centre": "Appena a Sinistra del Centro",
    "Centrist": "Centrista",
    "Just Right of Centre": "Appena a Destra del Centro",
    "Centre Right": "Centro Destra",
    "Moderately Right": "Moderatamente Destra",
    "Right": "Destra",
    "Far Right": "Estrema Destra"
}

INTEREST = {
    "No interest": "Nessun interesse",
    "Very slightly interested": "Molto poco interessato",
    "Slightly interested": "Poco interessato",
    "Some interest": "Un po' di interesse",
    "Interested": "Interessato",
    "Very interested": "Molto interessato",
    "Extremely interested": "Estremamente interessato"
}
