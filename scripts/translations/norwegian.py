from translations.article import Article

COUNTRIES = {
    'Austria': 'Østerrike',
    'France': 'Frankrike',
    'Germany': 'Tyskland',
    'Greece': 'Hellas',
    'Ireland': 'Irland',
    'Israel': 'Israel',
    'Italy': 'Italia',
    'the Netherlands': 'Nederland',
    'Norway': 'Norge',
    'Poland': 'Polen',
    'Romania': 'Romania',
    'Spain': 'Spania',
    'Sweden': 'Sverige',
    'Switzerland': 'Sveits',
    'the UK': 'Storbritannia'
}

AGREEMENT_INSTRUCTION = "## INSTRUKSJON - Vennligst vurder ditt standpunkt i følgende påstand fra skalaen – 1 helt uenig, 2 ganske uenig, 3 litt uenig, 4 nøytral, 5 litt enig, 6 ganske enig, 7 helt enig:"

WILLINGNESS_INSTRUCTION = "## INSTRUKSJON - Vennligst vurder ditt standpunkt ved å benytte skalaen under; til å ta følgende handling - 1 helt uvillig, 2 ganske uvillig, 3 litt uvillig, 4 nøytral, 5 litt villig, 6 ganske villig, 7 helt villig:"

PROBE_STATEMENTS = [
    "# Økonomien vil møte en nedgang i nær fremtid - ",
    "# Det må gjennomføres endringer i politikken for å forhindre en nedgang i kjøpekraften - ",
    "# Del nyhetsartikkelen på sosiale nettverkssider - ",
    "# Snakk med en venn om artikkelen - ",
    "# Signer en nettbasert underskriftskampanje for å støtte den ikke-statlige organisasjonen nevnt i artikkelen - "
]

INSERTS = {
    'Austria': ['østerriksk', 'Østerrike'],
    'France': ['fransk', 'Frankrike'],
    'Germany': ['tysk', 'Tyskland'],
    'Greece': ['gresk', 'Hellas'],
    'Ireland': ['irsk', 'Irland'],
    'Israel': ['israelsk', 'Israel'],
    'Italy': ['italiensk', 'Italia'],
    'the Netherlands': ['nederlandsk', 'Nederland'],
    'Norway': ['norsk', 'Norge'],
    'Poland': ['polsk', 'Polen'],
    'Romania': ['rumensk', 'Romania'],
    'Spain': ['spansk', 'Spania'],
    'Sweden': ['svensk', 'Sverige'],
    'Switzerland': ['sveitsisk', 'Sveits'],
    'the UK': ['britisk', 'Storbritannia']
}

ARTICLES = [
    Article(
        "Kjøpekraften vil avta - stiftelsen FutureNow utgir ny rapport",
        "<beskrivelse - hender og åpen tom lommebok, eieren ser inni>",
        "Ifølge en ny rapport fra FutureNow vil kjøpekraften avta i de kommende årene. En talsperson for den uavhengige stiftelsen som har overvåket økonomiske utviklinger i mange år kommenterer rapporten: 'Vi må øke bevisstheten om hva dette perspektivet betyr. Det vil være mindre penger å bruke. Tiltak må tas nå for å takle denne utfordringen.'"
    ),
    Article(
        "Kjøpekraften vil avta for [] vanlige folk - stiftelsen FutureNow skylder på politikerne i ny rapport",
        "<beskrivelse - hender og åpen tom lommebok, eieren ser inni>",
        "Ifølge en ny rapport fra FutureNow vil kjøpekraften i [] avta i de kommende årene. En talsperson for den uavhengige stiftelsen som har overvåket økonomiske utviklinger i mange år kommenterer rapporten: 'Vanlige borgere i [] må gjøres oppmerksom på at de vil ha mindre penger å bruke. Mange mennesker i [] jobber hardt hver dag for å ha et godt liv. Det er noe grunnleggende galt når disse anstrengelsene ikke lønner seg. Det er åpenbart at politikerne har skylden. De har vært for kortsiktige, egeninteresserte og korrupte de siste årene. De bryr seg ikke om andre enn seg selv og er for fjernt fra folket. Tiltak må tas nå for å takle denne trusselen mot vårt folks velferd.'"
    ),
    Article(
        "Kjøpekraften vil avta for [] vanlige folk - stiftelsen FutureNow skylder på innvandrerne i ny rapport",
        "<beskrivelse - hender og åpen tom lommebok, eieren ser inni>",
        "Ifølge en ny rapport fra FutureNow vil kjøpekraften i [] avta i de kommende årene. En talsperson for den uavhengige stiftelsen som har overvåket økonomiske utviklinger i mange år kommenterer rapporten: 'Vanlige borgere i [] må gjøres oppmerksom på at de vil ha mindre penger å bruke. Mange mennesker i [] jobber hardt hver dag for å ha et godt liv. Det er noe grunnleggende galt når disse anstrengelsene ikke lønner seg. Det er åpenbart at innvandrerne har skylden. De er for krevende, de utnytter systemet vårt og er vanskelige å integrere. Tiltak må tas nå for å takle denne trusselen mot vårt folks velferd.'"
    ),
    Article(
        "Kjøpekraften vil avta for [] vanlige folk - stiftelsen FutureNow skylder på politikerne og innvandrerne i ny rapport",
        "<beskrivelse - hender og åpen tom lommebok, eieren ser inni>",
        "Ifølge en ny rapport fra FutureNow vil kjøpekraften i [] avta i de kommende årene. En talsperson for den uavhengige stiftelsen som har overvåket økonomiske utviklinger i mange år kommenterer rapporten: 'Vanlige borgere i [] må gjøres oppmerksom på at de vil ha mindre penger å bruke. Mange mennesker i [] jobber hardt hver dag for å ha et godt liv. Det er noe grunnleggende galt når disse anstrengelsene ikke lønner seg. Det er åpenbart at politikerne og innvandrerne har skylden. Politikerne har vært for kortsiktige, egeninteresserte og korrupte de siste årene. Innvandrere er for krevende, de utnytter systemet vårt og er vanskelige å integrere. Og likevel tar politikerne bare vare på innvandrerne i stedet for vårt eget folk. Tiltak må tas nå for å takle denne trusselen mot vårt folks velferd.'"
    )
]

DATE = "1/Feb/2017"

RATINGS = [
    "nan",
    "helt uenig",
    "ganske uenig",
    "litt uenig",
    "nøytral",
    "litt enig",
    "ganske enig",
    "helt enig"
]

SURVEY = """HOLDNINGSSPØRREUNDERSØKELSE

## INSTRUKSJON - Vennligst fyll ut dine personlige data
Kjønn - {gender}
Alder - {age}
Land du bor i - {country}
Utdanningsnivå - {educationLevel}
Interesse for politikk - {politicalInterest}
Politisk ideologi - {politicalIdeology}

Fullføringsdato - {DATE}

## INSTRUKSJON - Vennligst vurder ditt standpunkt i følgende påstander, ved å bruke en skala fra 1 (helt uenig) til 7 (helt enig):
# Hvis vi trenger noe fra regjeringen, må folk som meg alltid vente lenger enn andre - {firstDeprivationRating} - {firstRating}
# Jeg har aldri fått det jeg faktisk fortjente - {secondDeprivationRating} - {secondRating}
# Det er alltid andre mennesker som drar nytte av alle fordelene - {thirdDeprivationRating} - {thirdRating}

## INSTRUKSJON - Vennligst les følgende nettbaserte nyhetsartikkel nøye.

Tittel: {article.title}

Foto: {article.photo}

Tekst: {article.text}"""

GENDER = {
    "Male": "Mann",
    "Female": "Kvinne"
}

EDUCATION = {
    "Low": "Lav",
    "Medium": "Middels",
    "High": "Høy"
}

IDEOLOGY = {
    "Far Left": "Ytre venstre",
    "Left": "Venstresiden",
    "Moderately Left": "Moderat venstre",
    "Centre Left": "Sentrumsvenstre",
    "Just Left of Centre": "Litt til venstre for sentrum",
    "Centrist": "Sentrum",
    "Just Right of Centre": "Litt til høyre for sentrum",
    "Centre Right": "Sentrumhøyre",
    "Moderately Right": "Moderat høyre",
    "Right": "Høyre",
    "Far Right": "Ytre høyre"
}

INTEREST = {
    "No interest": "Ingen interesse",
    "Very slightly interested": "Svært lite interessert",
    "Slightly interested": "Litt interessert",
    "Some interest": "Noe interesse",
    "Interested": "Interessert",
    "Very interested": "Svært interessert",
    "Extremely interested": "Ekstremt interessert"
}
