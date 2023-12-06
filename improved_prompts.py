from openai import OpenAI

client = OpenAI(
    # api_key defaults to os.environ.get("OPENAI_API_KEY")
    api_key = 'YOUR_OPENAI_API_KEY'
)

added_prompt = 'give me a in detail input prompt containing related keywords for an ai text to image generation model to create an image of '
message = added_prompt + 'a lion painting his food on a canvas plced on a ezel in an art studio'

def improved_prompts(prompt):
  messages = [ {"role": "system", "content": "You are a intelligent assistant."} ]

  # message = input("User : ")
  messages.append(
    {"role": "user", "content": prompt},
  )
  chat = client.chat.completions.create(
        model = 'gpt-3.5-turbo',
        messages = messages,
        temperature = 0.5
  )
  reply = chat.choices[0].message.content

  partitions = reply.partition("\"")
  result = partitions[1] + partitions[2]
  # print(result)
  return result

IP = improved_prompts(message)
print(IP)