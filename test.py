import os
import openai
from papago import Translator

openai.api_key = "your_key"

translator = Translator()
max_line = 9

while(True):
    prompt_file = open('./data1.txt', 'r+')
    prompt = ""
    count = 0
    while True:
        line = prompt_file.readline()
        if not line: break
        count += 1
        prompt = prompt + line
    prompt_file.close()
    if count > max_line or count <= 0:
        print('최대 대화 수 초과, 대화가 초기화됩니다.')
        prompt_file = open('./data1.txt', 'w')
        prompt_file.write("The following is a conversation with an AI assistant. The assistant is helpful, creative, clever, and very friendly.\n\nHuman: Hello, who are you?\nAI: I am an AI created by OpenAI. How can I help you today?\nHuman: ")
        prompt = "The following is a conversation with an AI assistant. The assistant is helpful, creative, clever, and very friendly.\n\nHuman: Hello, who are you?\nAI: I am an AI created by OpenAI. How can I help you today?\nHuman: "
        prompt_file.close()

    input_text = input()
    if input_text == "종료":
        break
    translated_input = translator.translate(input_text)
    prompt = prompt + translated_input + "\n" + "AI:"

    response = openai.Completion.create(
        engine="davinci",
        prompt=prompt,
        temperature=0.9,
        max_tokens=150,
        top_p=1,
        frequency_penalty=0.0,
        presence_penalty=0.6,
        stop=["\n", " Human:", " AI:"]
    )

    output = str(response['choices'][0]['text'])
    prompt = prompt + output + "\n" + "Human:"
    prompt_file = open('./data1.txt', 'w')
    prompt_file.write(prompt)
    prompt_file.close()

    translated_output = translator.translate(output, source='en', target='ko')
    print(translated_output)

os.system('pause')