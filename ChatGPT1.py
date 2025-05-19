from openai import OpenAI

client = OpenAI()
completion = client.chat.completions.create(
    organization='org-zNwryVkuVZDXpTe45xjmY0vP',
    project='$PROJECT_ID',
    model="gpt-4o-mini",
    messages=[
        {"role": "system", "content": "You are a helpful assistant."},
        {
            "role": "user",
            "content": "Write a haiku about recursion in programming."
        }
    ]
)
print(completion.choices[0].message)

client = OpenAI()
response = client.images.generate(
    prompt="A cute baby sea otter",
    n=2,
    size="1024x1024"
)
print(response.data[0].url)

client = OpenAI()
response = client.embeddings.create(
    model="text-embedding-3-large",
    input="The food was delicious and the waiter..."
)
print(response)

