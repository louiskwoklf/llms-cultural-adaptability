import concurrent.futures
import copy
import datetime
import json
import os
import pandas as pd
import random
import time
import warnings

from modelInteraction import completePrompt, MODEL_TYPE

warnings.filterwarnings("ignore", category=UserWarning, message="Workbook contains no default style, apply openpyxl's default")

MODEL_TYPE = MODEL_TYPE.replace('/', '-')

class Article:
    def __init__(self, title, photo, text):
        self.title = title
        self.photo = photo
        self.text = text

MAX_THREADS = 10
TRANSLATED = False

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

LANGUAGE_CODES = {
    "german": "de",
    "french": "fr",
    "greek": "el",
    "english": "en",
    "hebrew": "iw",
    "italian": "it",
    "dutch": "nl",
    "norwegian": "no",
    "polish": "pl",
    "romanian": "ro",
    "spanish": "es",
    "swedish": "sv",
}


NATIONALITIES = {
    "Austria": "Austrian citizens",
    "France": "French citizens",
    "Germany": "German citizens",
    "Greece": "Greek citizens",
    "Ireland": "Irish citizens",
    "Israel": "Israeli citizens",
    "Italy": "Italian citizens",
    "the Netherlands": "Dutch citizens",
    "Norway": "Norwegian citizens",
    "Poland": "Polish citizens",
    "Romania": "Romanian citizens",
    "Spain": "Spanish citizens",
    "Sweden": "Swedish citizens",
    "Switzerland": "Swiss citizens",
    "the UK": "UK citizens"
}

P, M, E, I, D, C1, C2, C3, C4, C5, C6, C7, C8, C9, C10, C11, C12, C13, C14 = [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], []

def translateText(text, language, translator):
    while True:
        try:
            return translator.translate(text, src="en", dest=LANGUAGE_CODES[language]).text
        except:
            time.sleep(1)


def processPrompt(prompt):
    response = completePrompt(prompt)
    while response == None or len(response) < 1 or len(response) > 1 or not response[0].isdigit():
        response = completePrompt(prompt)
    return response

def process_survey(country, language):

    if language == "dutch":
        from languages.dutch import AGREEMENT_INSTRUCTION, WILLINGNESS_INSTRUCTION, PROBE_STATEMENTS, ARTICLES, RATINGS, SURVEY, GENDER, EDUCATION, INTEREST, IDEOLOGY, DATE, COUNTRIES, INSERTS
    elif language == "english":
        from languages.english import AGREEMENT_INSTRUCTION, WILLINGNESS_INSTRUCTION, PROBE_STATEMENTS, ARTICLES, RATINGS, SURVEY, GENDER, EDUCATION, INTEREST, IDEOLOGY, DATE, COUNTRIES, INSERTS
    elif language == "french":
        from languages.french import AGREEMENT_INSTRUCTION, WILLINGNESS_INSTRUCTION, PROBE_STATEMENTS, ARTICLES, RATINGS, SURVEY, GENDER, EDUCATION, INTEREST, IDEOLOGY, DATE, COUNTRIES, INSERTS
    elif language == "german":
        from languages.german import AGREEMENT_INSTRUCTION, WILLINGNESS_INSTRUCTION, PROBE_STATEMENTS, ARTICLES, RATINGS, SURVEY, GENDER, EDUCATION, INTEREST, IDEOLOGY, DATE, COUNTRIES, INSERTS
    elif language == "hebrew":
        from languages.hebrew import AGREEMENT_INSTRUCTION, WILLINGNESS_INSTRUCTION, PROBE_STATEMENTS, ARTICLES, RATINGS, SURVEY, GENDER, EDUCATION, INTEREST, IDEOLOGY, DATE, COUNTRIES, INSERTS
    elif language == "italian":
        from languages.italian import AGREEMENT_INSTRUCTION, WILLINGNESS_INSTRUCTION, PROBE_STATEMENTS, ARTICLES, RATINGS, SURVEY, GENDER, EDUCATION, INTEREST, IDEOLOGY, DATE, COUNTRIES, INSERTS
    elif language == "norwegian":
        from languages.norwegian import AGREEMENT_INSTRUCTION, WILLINGNESS_INSTRUCTION, PROBE_STATEMENTS, ARTICLES, RATINGS, SURVEY, GENDER, EDUCATION, INTEREST, IDEOLOGY, DATE, COUNTRIES, INSERTS
    elif language == "polish":
        from languages.polish import AGREEMENT_INSTRUCTION, WILLINGNESS_INSTRUCTION, PROBE_STATEMENTS, ARTICLES, RATINGS, SURVEY, GENDER, EDUCATION, INTEREST, IDEOLOGY, DATE, COUNTRIES, INSERTS
    elif language == "romanian":
        from languages.romanian import AGREEMENT_INSTRUCTION, WILLINGNESS_INSTRUCTION, PROBE_STATEMENTS, ARTICLES, RATINGS, SURVEY, GENDER, EDUCATION, INTEREST, IDEOLOGY, DATE, COUNTRIES, INSERTS
    elif language == "spanish":
        from languages.spanish import AGREEMENT_INSTRUCTION, WILLINGNESS_INSTRUCTION, PROBE_STATEMENTS, ARTICLES, RATINGS, SURVEY, GENDER, EDUCATION, INTEREST, IDEOLOGY, DATE, COUNTRIES, INSERTS
    elif language == "swedish":
        from languages.swedish import AGREEMENT_INSTRUCTION, WILLINGNESS_INSTRUCTION, PROBE_STATEMENTS, ARTICLES, RATINGS, SURVEY, GENDER, EDUCATION, INTEREST, IDEOLOGY, DATE, COUNTRIES, INSERTS
    elif language == "greek":
        from languages.greek import AGREEMENT_INSTRUCTION, WILLINGNESS_INSTRUCTION, PROBE_STATEMENTS, ARTICLES, RATINGS, SURVEY, GENDER, EDUCATION, INTEREST, IDEOLOGY, DATE, COUNTRIES, INSERTS
    else:
        raise Exception(f"Language {language} not supported")
    
    agreement_instruction = AGREEMENT_INSTRUCTION + "\n"
    probe_statements = PROBE_STATEMENTS
    willingness_instruction = WILLINGNESS_INSTRUCTION + "\n"

    data = pd.read_excel("../demographics/humanSubjects.xlsx", header=0)

    for index, row in data.iterrows():
        if row["Country_Code"] != country:
            continue

        if row["finalflag"] != "sufficient/high quality response":
            continue

        if isinstance(row["gender"], str) == True:
            gender = GENDER[row["gender"]]
        else:
            gender = "nan"
        age = str(row["age_1"]).split(".")[0]

        country_name = COUNTRIES[country]
        if isinstance(row["educ"], str) == True:
            educationLevel = EDUCATION[row["educ"]]
        else:
            educationLevel = "nan"
        if isinstance(row["polint"], str) == True:
            politicalInterest = INTEREST[row["polint"]]
        else:
            politicalInterest = "nan"
        if isinstance(row["ideo"], str) == True:
            politicalIdeology = IDEOLOGY[row["ideo"]]
        else:
            politicalIdeology = "nan"
        if isinstance(row["reldep1"], int) == True:
            firstDeprivationRating = row["reldep1"]
        else:
            firstDeprivationRating = 4
        if isinstance(row["reldep2"], int) == True:
            secondDeprivationRating = row["reldep2"]
        else:
            secondDeprivationRating = 4
        if isinstance(row["reldep3"], int) == True:
            thirdDeprivationRating = row["reldep3"]
        else:
            thirdDeprivationRating = 4

        if row["antielite"] == 0 and row["antiim"] == 0:
            articleIndex = 0
        elif row["antielite"] == 1 and row["antiim"] == 0:
            articleIndex = 1
        elif row["antielite"] == 0 and row["antiim"] == 1:
            articleIndex = 2
        elif row["antielite"] == 1 and row["antiim"] == 1:
            articleIndex = 3
            

        article = copy.deepcopy(ARTICLES[articleIndex])
        if articleIndex >= 1:
            article.title = article.title.replace("[]", INSERTS[country][0])
            article.text = article.text.replace("[]", INSERTS[country][1])
        
        survey = SURVEY.format(gender = gender, age = age, country = country_name, educationLevel = educationLevel, politicalInterest = politicalInterest, politicalIdeology = politicalIdeology, DATE = DATE, firstDeprivationRating = firstDeprivationRating, firstRating = RATINGS[firstDeprivationRating], secondDeprivationRating = secondDeprivationRating, secondRating = RATINGS[secondDeprivationRating], thirdDeprivationRating = thirdDeprivationRating, thirdRating = RATINGS[thirdDeprivationRating], article = article)
        
        survey += "\n\n"

        response1 = processPrompt(survey + agreement_instruction + probe_statements[0])

        response2 = processPrompt(survey + agreement_instruction + probe_statements[1])

        response3 = processPrompt(survey + willingness_instruction + probe_statements[2])

        response4 = processPrompt(survey + willingness_instruction + probe_statements[3])

        response5 = processPrompt(survey + willingness_instruction + probe_statements[4])

        e = int(articleIndex % 2 == 1)
        i = int(articleIndex > 1)
        d = (firstDeprivationRating + secondDeprivationRating + thirdDeprivationRating) / 3

        if TRANSLATED:
            filePath = f"../output/COLM/{MODEL_TYPE}/{language}/data/outputData_{country}.jsonl"
        else:
            filePath = f"../output/COLM/{MODEL_TYPE}/{language}/data/outputData_{country}.jsonl"

        data = {
            "P": (float(response1) + float(response2)) / 2,
            "M": (float(response3) + float(response4) + float(response5)) / 3,
            "E": e,
            "I": i,
            "D": d,
            "EI": e * i,
            "DE": d * e,
            "DI": d * i,
            "DEI": d * e * i,
            "C1": int(country == "Austria"),
            "C2": int(country == "France"),
            "C3": int(country == "Germany"),
            "C4": int(country == "Greece"),
            "C5": int(country == "Ireland"),
            "C6": int(country == "Israel"),
            "C7": int(country == "Italy"),
            "C8": int(country == "the Netherlands"),
            "C9": int(country == "Norway"),
            "C10": int(country == "Romania"),
            "C11": int(country == "Spain"),
            "C12": int(country == "Sweden"),
            "C13": int(country == "Switzerland"),
            "C14": int(country == "the UK")
        }

        with open(filePath, "a") as file:
            file.write(f"{json.dumps(data)}\n")
    
    print(f"{country} complete")


if __name__ == "__main__":
    for language in LANGUAGES:
        if language != "french":
            continue
        print(f"Experiment begins in {language}: " + str(datetime.datetime.now()))
        with concurrent.futures.ThreadPoolExecutor(max_workers=MAX_THREADS) as executor:
            future_to_country = {executor.submit(process_survey, country, language): country for country in NATIONALITIES.keys()}

            for future in concurrent.futures.as_completed(future_to_country):
                country = future_to_country[future]
                try:
                    data = future.result()
                except Exception as exc:
                    print('%r generated an exception: %s' % (country, exc))

            print(f"Experiment completed in {language}: " + str(datetime.datetime.now()))