import os
import openai

openai.api_key = os.getenv("OPENAI_API_KEY1")

while True:
 question = input("\033[30mType in your question. Reply with exit to close.\n\033[34m")
 if question.lower() == "exit":
   print("\033[31mGoodbye!See you soon.\033[34m")
   break
 completion = openai.ChatCompletion.create(
     model="gpt-3.5-turbo",
    messages=[
    {"role": "system", "content": "You are a helpful assistant. Answer the given question."},
    {"role": "user", "content": question}
  ]
)
 print("\033[0m"+ completion.choices[0].message.content + "\n")
