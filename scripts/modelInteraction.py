from openai import OpenAI

API_KEY = ""
MODEL_TYPE = "gpt-3.5-turbo-1106"

def completePrompt(prompt): 
    client = OpenAI(api_key=API_KEY)

    response = client.chat.completions.create(
        model = MODEL_TYPE,
        messages = [{"role": "user", "content": prompt}],
        top_p = 1,
        temperature = 1,
        max_tokens = 1
    )

    return response.choices[0].message.content.strip()
