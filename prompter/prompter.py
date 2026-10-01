from query import query
from checkurls import check_urls

import yaml 


instructions = ("You're a helpful and neutral assistant for general knowledge questions. " 
"Please answer in correct English and keep your anwer short and to the point. Also, please add "
"a hyperlink to the source you used.")

prompt_templates = (
    "How many people lived in {country} on January 1st 2024?",
    "What was het Life expectancy in years for new born female babies in {country} in 2020?"
)

countries = (
    "The Netherlands",
    "Denmark",
    #"France"
)

models = (
    "gpt-6-luna",
    "gemini-3.8-flash"
)

with open("output.yaml", "a", encoding="utf-8") as output_file:
    for prompt_template in prompt_templates:
        for country in countries:
            for model in models:
                prompt = prompt_template.format(country=country)
                print(f"{model}: {prompt}")
                result = query(model, instructions, prompt)
                result["hyperlinks"] = check_urls(result["response"])
                yaml.safe_dump([result], output_file, sort_keys=False)
