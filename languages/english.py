from languages.article import Article

COUNTRIES = {
    'Austria': 'Austria',
    'France': 'France',
    'Germany': 'Germany',
    'Greece': 'Greece',
    'Ireland': 'Ireland',
    'Israel': 'Israel',
    'Italy': 'Italy',
    'the Netherlands': 'the Netherlands',
    'Norway': 'Norway',
    'Poland': 'Poland',
    'Romania': 'Romania',
    'Spain': 'Spain',
    'Sweden': 'Sweden',
    'Switzerland': 'Switzerland',
    'the UK': 'the UK'
}

AGREEMENT_INSTRUCTION = "## INSTRUCTION - Please rate your personal agreement with the following statement, using the scale - 1 completely disagree, 2 mostly disagree, 3 slightly disagree, 4 neutral, 5 slightly agree, 6 mostly agree, 7 completely agree:"

WILLINGNESS_INSTRUCTION = "## INSTRUCTION - Please rate your personal willingness to take the following action, using the scale - 1 completely unwilling, 2 mostly unwilling, 3 slightly unwilling, 4 neutral, 5 slightly willing, 6 mostly willing, 7 completely willing:"

PROBE_STATEMENTS = [
    "# The economy will face a decline in the near future - ",
    "# Policy changes need to be implemented to prevent the decline of purchasing power - ",
    "# Share the news article on social network sites - ",
    "# Talk to a friend about the article - ",
    "# Sign an online petition to support the nongovernmental organization mentioned in the article - "
]

INSERTS = {
    'Austria': ['Austrian', 'Austria'],
    'France': ['French', 'France'],
    'Germany': ['German', 'Germany'],
    'Greece': ['Greek', 'Greece'],
    'Ireland': ['Irish', 'Ireland'],
    'Israel': ['Israeli', 'Israel'],
    'Italy': ['Italian', 'Italy'],
    'the Netherlands': ['Dutch', 'the Netherlands'],
    'Norway': ['Norwegian', 'Norway'],
    'Poland': ['Polish', 'Poland'],
    'Romania': ['Romanian', 'Romania'],
    'Spain': ['Spanish', 'Spain'],
    'Sweden': ['Swedish', 'Sweden'],
    'Switzerland': ['Swiss', 'Switzerland'],
    'the UK': ['UK', 'the UK']
}

ARTICLES = [
    Article(
        "Purchasing power will decline - foundation FutureNow releases new report",
        "<description - hands and open empty wallet, owner is looking within>",
        "According to a new report by FutureNow, purchasing power will decline in the coming years. A spokesperson for the independent foundation, which has been monitoring economic developments for years, commented on the report: 'We have to raise awareness about what this prospect means. There will be less money to spend. Action has to be taken now to address this threat.'"
    ),
    Article(
        "Purchasing power will decline for [] citizens - foundation FutureNow blames politicians in new report",
        "<description - hands and open empty wallet, owner is looking within>",
        "According to a new report by FutureNow, purchasing power in [] will decline in the coming years. A spokesperson for the independent foundation, which has been monitoring economic developments for years, commented on the report: 'The common citizens in [] need to be made aware of the fact that they will have less money to spend. So many people in [] are working hard every day to have a good life. There is something profoundly wrong when these efforts do not pay off. It is obvious that politicians are to blame. They have been too short-sighted, self-serving, and corrupt in recent years. They don't care about anyone but themselves and are too detached from the people. Action has to be taken now to address this threat to the well-being of our people.'"
    ),
    Article(
        "Purchasing power will decline for [] citizens - foundation FutureNow blames immigrants in new report",
        "<description - hands and open empty wallet, owner is looking within>",
        "According to a new report by FutureNow, purchasing power in [] will decline in the coming years. A spokesperson for the independent foundation, which has been monitoring economic developments for years, commented on the report: 'The common citizens in [] need to be made aware of the fact that they will have less money to spend. So many people in [] are working hard every day to have a good life. There is something profoundly wrong when these efforts do not pay off. It is obvious that immigrants are to blame. They are too demanding, they exploit our system, and are hard to integrate. Action has to be taken now to address this threat to the well-being of our people.'"
    ),
    Article(
        "Purchasing power will decline for [] citizens - foundation FutureNow blames politicians and immigrants in new report",
        "<description - hands and open empty wallet, owner is looking within>",
        "According to a new report by FutureNow, purchasing power in [] will decline in the coming years. A spokesperson for the independent foundation, which has been monitoring economic developments for years, commented on the report: 'The common citizens in [] need to be made aware of the fact that they will have less money to spend. So many people in [] are working hard every day to have a good life. There is something profoundly wrong when these efforts do not pay off. It is obvious that politicians and immigrants are to blame. Politicians have been too short-sighted, self-serving, and corrupt in recent years. Migrants are too demanding, they exploit our system, and are hard to integrate. And still, politicians only take care of the migrants instead of our own people. Action has to be taken now to address this threat to the well-being of our people.'"
    )
]

DATE = "1/Feb/2017"

RATINGS = [
    "nan",
    "completely disagree",
    "mostly disagree",
    "slightly disagree",
    "neutral",
    "slightly agree",
    "mostly agree",
    "completely agree"
]

SURVEY = """ATTITUDES SURVEY

## INSTRUCTION - Please complete your personal data
Gender - {gender}
Age - {age}
Country of Residence - {country}
Education Level - {educationLevel}
Interest in Politics - {politicalInterest}
Political Ideology - {politicalIdeology}

Completion date - {DATE}

## INSTRUCTION - Please rate your personal agreement with the following statements, using a scale from 1 (completely disagree) to 7 (completely agree):
# If we need anything from the government, people like me always have to wait longer than others - {firstDeprivationRating} - {firstRating}
# I never received what I in fact deserved - {secondDeprivationRating} - {secondRating}
# It's always the other people who profit from all kinds of benefits - {thirdDeprivationRating} - {thirdRating}

## INSTRUCTION - Please read the following online news article closely.

Title: {article.title}

Photo: {article.photo}

Text: {article.text}"""

GENDER = {
    "Male": "Male",
    "Female": "Female"
}

EDUCATION = {
    "Low": "Low",
    "Medium": "Medium",
    "High": "High"
}

IDEOLOGY = {
    "Far Left": "Far Left",
    "Left": "Left",
    "Moderately Left": "Moderately Left",
    "Centre Left": "Centre Left",
    "Just Left of Centre": "Just Left of Centre",
    "Centrist": "Centrist",
    "Just Right of Centre": "Just Right of Centre",
    "Centre Right": "Centre Right",
    "Moderately Right": "Moderately Right",
    "Right": "Right",
    "Far Right": "Far Right"
}

INTEREST = {
    "No interest": "No interest",
    "Very slightly interested": "Very slightly interested",
    "Slightly interested": "Slightly interested",
    "Some interest": "Some interest",
    "Interested": "Interested",
    "Very interested": "Very interested",
    "Extremely interested": "Extremely interested"
}