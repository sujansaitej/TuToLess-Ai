import os
import openai
openai.api_key = "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"


def get_output_for_doubt(text):
    response = openai.ChatCompletion.create(
    model="gpt-3.5-turbo",
    messages=[
            {"role": "system", "content": text},
        ]
    )
    return response["choices"][0]["message"]['content']