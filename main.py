import openai

openai.api_key = "enter chatbot api"

def chat_with_gpt(prompt):
  respons = openai.ChatCompletion.create(
    model = "gpt-3.5-turbo",
    messages = [{"role": "user", "content": prompt}]
  )

  return response.choices[0].message.content.strip()

if __name__ == "__main__":
  while True:
    user_input = input("You: ")
    if user_input.lower() in ["quit", "exit", "bye"]:
      break
      
      response = chat_with_gpt(user_input);
      Print("Chatbot:", response);
