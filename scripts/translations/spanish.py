from translations.article import Article

COUNTRIES = {
    'Austria': 'Austria',
    'France': 'Francia',
    'Germany': 'Alemania',
    'Greece': 'Grecia',
    'Ireland': 'Irlanda',
    'Israel': 'Israel',
    'Italy': 'Italia',
    'the Netherlands': 'los Países Bajos',
    'Norway': 'Noruega',
    'Poland': 'Polonia',
    'Romania': 'Rumanía',
    'Spain': 'España',
    'Sweden': 'Suecia',
    'Switzerland': 'Suiza',
    'the UK': 'el Reino Unido'
}

AGREEMENT_INSTRUCTION = "## INSTRUCCIÓN - Indique en qué medida está de acuerdo con la siguiente afirmación, usando la escala - 1 totalmente en desacuerdo, 2 mayormente en desacuerdo, 3 ligeramente en desacuerdo, 4 neutral, 5 ligeramente de acuerdo, 6 mayormente de acuerdo, 7 totalmente de acuerdo:"

WILLINGNESS_INSTRUCTION = "## INSTRUCCIÓN - Por favor, califique su disposición personal a tomar la siguiente acción, usando la escala - 1 completamente no dispuesto, 2 mayormente no dispuesto, 3 ligeramente no dispuesto, 4 neutral, 5 ligeramente dispuesto, 6 mayormente dispuesto, 7 completamente dispuesto:"

PROBE_STATEMENTS = [
    "# La economía enfrentará una caída en el futuro cercano - ",
    "# Se necesitan implementar cambios en las políticas para prevenir la caída del poder adquisitivo - ",
    "# Comparte el artículo en las redes sociales - ",
    "# Habla con un amigo sobre el artículo - ",
    "# Firma la petición en línea para apoyar a la ONG mencionada en el artículo - "
]

INSERTS = {
    'Austria': ['austriacos', 'Austria'],
    'France': ['franceses', 'Francia'],
    'Germany': ['alemanes', 'Alemania'],
    'Greece': ['griegos', 'Grecia'],
    'Ireland': ['irlandeses', 'Irlanda'],
    'Israel': ['israelíes', 'Israel'],
    'Italy': ['italianos', 'Italia'],
    'the Netherlands': ['neerlandeses', 'los Países Bajos'],
    'Norway': ['noruegos', 'Noruega'],
    'Poland': ['polacos', 'Polonia'],
    'Romania': ['rumanos', 'Rumanía'],
    'Spain': ['españoles', 'España'],
    'Sweden': ['suecos', 'Suecia'],
    'Switzerland': ['suizos', 'Suiza'],
    'the UK': ['británicos', 'el Reino Unido']
}

ARTICLES = [
    Article(
        "El poder adquisitivo disminuirá - la fundación FutureNow publica un nuevo informe",
        "<descripción - manos y una cartera abierta y vacía, con el proprietario mirando dentro>",
        "Según un nuevo informe de FutureNow, el poder adquisitivo disminuirá en los próximos años. Un portavoz de la fundación independiente que ha estado monitorizado el desarrollo económico durante años comenta sobre el informe: 'Tenemos que crear conciencia sobre lo que significa esta perspectiva. Habrá menos dinero para gastar. Se deben tomar medidas ahora para abordar esta amenaza.'"
    ),
    Article(
        "El poder adquisitivo disminuirá para los ciudadanos [] - la fundación FutureNow culpa a los políticos en un nuevo informe",
        "<descripción - manos y una cartera abierta y vacía, con el proprietario mirando dentro",
        "Según un nuevo informe de FutureNow, el poder adquisitivo en [] disminuirá en los próximos años. Un portavoz de la fundación independiente que ha estado monitorizado el desarrollo económico durante años comenta sobre el informe: 'Los ciudadanos corrientes de [] deben ser conscientes de que tendrán menos dinero para gastar. Tantas personas en [] están trabajando tan duro todos los días para tener una buena vida. Hay algo profundamente erróneo cuando estos esfuerzos no rinden frutos. Es obvio que los políticos tienen la culpa. Han sido demasiado cortos de miras, egoístas y corruptos en los últimos años. No les importa nadie más que ellos mismos y están demasiado alejados de la gente. Se deben tomar medidas ahora para abordar esta amenaza al bienestar de nuestro pueblo.'"
    ),
    Article(
        "El poder adquisitivo disminuirá para los ciudadanos [] - la fundación FutureNow culpa a los inmigrantes en un nuevo informe",
        "<descripción - manos y una cartera abierta y vacía, con el proprietario mirando dentro>",
        "Según un nuevo informe de FutureNow, el poder adquisitivo en [] disminuirá en los próximos años. Un portavoz de la fundación independiente que ha estado monitorizado el desarrollo económico durante años comenta sobre el informe: 'Los ciudadanos corrientes de [] deben ser conscientes de que tendrán menos dinero para gastar. Tantas personas en [] están trabajando tan duro todos los días para tener una buena vida. Hay algo profundamente erróneo cuando estos esfuerzos no rinden frutos. Es obvio que los inmigrantes tienen la culpa. Son demasiado exigentes, explotan nuestro sistema y son difíciles de integrar. Se deben tomar medidas ahora para abordar esta amenaza al bienestar de nuestro pueblo.'"
    ),
    Article(
        "El poder adquisitivo disminuirá para los ciudadanos [] - la fundación FutureNow culpa a los políticos e inmigrantes en un nuevo informe",
        "<descripción - manos y una cartera abierta y vacía, con el proprietario mirando dentro>",
        "Según un nuevo informe de FutureNow, el poder adquisitivo en [] disminuirá en los próximos años. Un portavoz de la fundación independiente que ha estado monitorizado el desarrollo económico durante años comenta sobre el informe: 'Los ciudadanos corrientes de [] deben ser conscientes de que tendrán menos dinero para gastar. Tantas personas en [] están trabajando tan duro todos los días para tener una buena vida. Hay algo profundamente erróneo cuando estos esfuerzos no rinden frutos. Es obvio que los políticos e inmigrantes tienen la culpa. Los políticos han sido demasiado cortos de miras, egoístas y corruptos en los últimos años. Los inmigrantes son demasiado exigentes, explotan nuestro sistema y son difíciles de integrar. Y aun así, los políticos solo se preocupan por los inmigrantes en lugar de nuestra propia gente. Se deben tomar medidas ahora para abordar esta amenaza al bienestar de nuestro pueblo.'"
    )
]

DATE = "1/Feb/2017"

RATINGS = [
    "nan",
    "completamente en desacuerdo",
    "mayormente en desacuerdo",
    "ligeramente en desacuerdo",
    "neutral",
    "ligeramente de acuerdo",
    "mayormente de acuerdo",
    "completamente de acuerdo"
]

SURVEY = """ENCUESTA DE ACTITUDES

## INSTRUCCIÓN - Por favor, complete sus datos personales
Género - {gender}
Edad - {age}
País de Residencia - {country}
Nivel Educativo - {educationLevel}
Interés en la Política - {politicalInterest}
Ideología Política - {politicalIdeology}

Fecha de compleción - {DATE}

## INSTRUCCIÓN - Indique en qué medida está de acuerdo con la siguente afirmación, usando una escala del 1 (completamente en desacuerdo) al 7 (completamente de acuerdo):
# Si necesitamos algo del gobierno, personas como yo siempre tienen que esperar más que otros - {firstDeprivationRating} - {firstRating}
# Nunca recibí lo que realmente merecía - {secondDeprivationRating} - {secondRating}
# Siempre son las otras personas las que se benefician de todo tipo de ayudas - {thirdDeprivationRating} - {thirdRating}

## INSTRUCCIÓN - Por favor, lea detenidamente el siguiente artículo de noticias en línea.

Título: {article.title}

Foto: {article.photo}

Texto: {article.text}"""

GENDER = {
    "Male": "Hombre",
    "Female": "Mujer"
}

EDUCATION = {
    "Low": "Bajo",
    "Medium": "Medio",
    "High": "Alto"
}

IDEOLOGY = {
    "Far Left": "Extrema Izquierda",
    "Left": "Izquierda",
    "Moderately Left": "Izquerda Moderada",
    "Centre Left": "Centro-Izquierda",
    "Just Left of Centre": "Justo a la Izquierda del Centro",
    "Centrist": "Centrista",
    "Just Right of Centre": "Justo a la Derecha del Centro",
    "Centre Right": "Centro-Derecha",
    "Moderately Right": "Derecha Moderada",
    "Right": "Derecha",
    "Far Right": "Extrema Derecha"
}

INTEREST = {
    "No interest": "Sin interés",
    "Very slightly interested": "Muy poco interesado",
    "Slightly interested": "Ligeramente interesado",
    "Some interest": "Algo interesado",
    "Interested": "Interesado",
    "Very interested": "Muy interesado",
    "Extremely interested": "Extremadamente interesado"
}
