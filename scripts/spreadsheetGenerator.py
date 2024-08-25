import json
import pandas as pd

from modelInteraction import MODEL_TYPE

MODEL_TYPE = MODEL_TYPE.replace('/', '-')

LANGUAGES = [
    "dutch",
    "english",
    "french",
    "german",
    "greek",
    "hebrew",
    "italian",
    "norwegian",
    "polish",
    "romanian",
    "spanish",
    "swedish"
]

COUNTRIES = [
    "Austria",
    "France",
    "Germany",
    "Greece",
    "Ireland",
    "Israel",
    "Italy",
    "the Netherlands",
    "Norway",
    "Poland",
    "Romania",
    "Spain",
    "Sweden",
    "Switzerland",
    "the UK"
]

for language in LANGUAGES:
    for country in COUNTRIES:
        with open(f'../output/{MODEL_TYPE}/data/outputData_{country}.jsonl', 'r') as file:
            jsonlData = [json.loads(line) for line in file]

        df = pd.DataFrame(jsonlData)

        insertString = ""

        if country == "the Netherlands":
            insertString = "Netherlands"
        elif country == "the UK":
            insertString = "UK"
        else:
            insertString = country

        df.to_excel(f'../output/{MODEL_TYPE}/spreadsheets/outputData_{insertString}.xlsx', index=False)
