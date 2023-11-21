import openai
from web_scrapping import parsed_json

api_key = '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'

openai.api_key = api_key

swagger_content = parsed_json

response = openai.ChatCompletion.create(
    model="gpt-3.5-turbo",
    messages=[
        {"role": "system", "content": "You are a helpful assistant."},
        {"role": "user", "content": f"Generate a Python class to handle API calls based on the"
                                    f" Swagger JSON:\n{{swagger_content}}\n\n"
                                    f"Our class should have methods like 'health_check()',"
                                    f" 'post_whisper_task(audio_url, whisper_model, language)', "
                                    f"and 'get_whisper_output(transaction_id)'."
                                    f"\n\n_base_url = 'custom url'\n\nalso in __init__ function we must have headers\n"
                                    f"/gw1/whisper/v1/health before all endpoints must be added /gw1\n"
                                    f"self.headers = {{'x-app-authorization': api_key}} header must be like this\n"},
    ],
    temperature=0.0,
    max_tokens=3000
)

# print(response['choices'][0]['message']['content'])

# Write the response to a file
with open('generated_client_code.txt', 'w') as file:
    file.write(response['choices'][0]['message']['content'])

print("Code has been written to 'generated_client_code.txt'")
