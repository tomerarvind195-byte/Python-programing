import OpenAI

#pip istall openai 
#if you saved the key under a different environment variable name , you can do something like:
client = OpenAI (
    api_key ="sk-proj-Wxs17ehGK2PnwmzCHcDwT3BlbkFJFMjGlbqZaFTcj"
)
command ='''PS C:\Users\tomer\OneDrive\Desktop\Python> python -m pip insatll openai

Python was not found; run without arguments to install from the Microsoft Store, or disable this shortcut from Settings > Apps > Advanced app settings > App execution aliases.'''

completion = client.chat.completions.create(
    model ="gpt-3.5-turbo",
    messages =[
        {"role ":"system","content":"you are a person named harry who speaks hindi as well as english . He is from India  and is a coder . You analyze chat history and respond like Harry"},
        {"role ":"user","content": comman}

    ]
)
print(completion.choices[0].message.content)