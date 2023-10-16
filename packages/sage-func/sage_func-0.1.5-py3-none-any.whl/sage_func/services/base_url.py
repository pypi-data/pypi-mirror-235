import openai

openai.api_key = "sk-7SlrqKrr9asuPMxjA9B2757170D0410a8fC01d8d2066245a"
openai.api_base = "https://api.aikey.one/v1"

# create a chat completion
chat_completion = openai.ChatCompletion.create(
    model="gpt-3.5-turbo", messages=[{"role": "user", "content": "Hello world"}]
)

# print the completion
print(chat_completion.choices[0].message.content)
