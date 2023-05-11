import openai
openai.api_key = "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"
model_engine = "gpt-3.5-turbo"

print ("hello word")

response = openai.ChatCompletion.create(
    model='gpt-3.5-turbo',
    messages=[
        {"role": "system", "content": "You are a helpful assistant."},
        {"role": "user", "content": "Hello, ChatGPT!"},
    ])

message = response.choices[0]['message']
print("{}: {}".format(message['role'], message['content']))
