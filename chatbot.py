cmd_____________   pip3 install openai


import openai


openai.api_key = "______API_---------"


def chat_with_gpt(prompt):
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        message=[{"role": "user", "content": prompt}]
    )


return response.choices[0].message.content.strip()


if __name__ == "__main__":
    while True:
        user_input = input("you: ")
        if user_input.lower() in ["quit", "exit", "bye"]:
            break




response = chat_with_gpt(user_input)
        print("chatbot: ", response)




cmd______________________  python main.py