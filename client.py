# import pyautogui
# import pyperclip
# import time
# import openai

# def is_last_message_from_sender(chat_log,sender_name="RohanDas"):
#     #Split the chat log into individual message
#     messages = chat_log_strip(),solit("/2024]")[-1]
#     if sender_name in messages:
#         return True 
#     return False
   

# # 1️⃣ Click on item at (1639, 1412)
# pyautogui.click(1639, 1412)

# time.sleep(2)
# while True:
# # Give time to switch to the target window
#   time.sleep(3)
# # 2️⃣ Drag to select text
# # from (1003, 237) to (2187, 1258)
#   pyautogui.moveTo (1026 ,244)
#   pyautogui.dragTo(1131, 1321, duration = 1.0, button ='left')# drag for 1 second 
#   time.sleep(2)

# # 3️⃣ Copy selected text
#   pyautogui.hotkey('ctrl', 'c')
#   time.sleep(2)

# # 4️⃣ Get text from clipboard into variable
#   chat_history = pyperclip.paste()

# # 5️⃣ Print or use the variable
#   print("Copied Text:\n")
#   print(chat_history)
       
#   if is_last_message_from_sender(chat_history):
  

#        completion = client.chat.completions.create(
#            model ="gpt-3.5-turbo",
#            messages =[
#                {"role ":"system","content":"you are a person named Naruto who speaks hindi as well as english . You are  from India  and you are  a coder . You analyze chat history and respond like Naruto.Output should be the next chat response (text message only)"},
#                {"role ":"user","content": chat_history}
       
#            ]
#        )
#        response = (completion.choices[0].message.content)
#        pyperclip,copy(response)


#        pyautogui.click(1808, 1328)
#        time.sleep(1)

#        pyautogui.hotkey('ctrl', 'v')
#        time.sleep(1)

#        pyautogui.press('enter')


import pyautogui
import pyperclip
import time
from openai import OpenAI

# 🔐 Put your API key here
client = OpenAI(api_key="Ysk-proj-qxhmZkSNfY6afvSvXxSh56gaylSf8CLCwNDbiVfVCsGVVDFIsoOIZdJo02pQ9i5GwbSzllRi7PT3BlbkFJlGuFAioWin5UOyw-D7Hs4r37QmDON0ExKxgS3H9ZeaUp1kbUudMfu8yWwJELgQ21peEdjrOGEA")

# ❗ Prevent script stop when mouse goes to screen corner
pyautogui.FAILSAFE = False

# ✅ Check if last message is from specific sender
def is_last_message_from_sender(chat_log, sender_name="RohanDas"):
    if not chat_log:
        return False
    last_part = chat_log.strip().split("\n")[-1]
    return sender_name in last_part

# 🖱 Click chat window once to activate
pyautogui.click(1639, 1412)
time.sleep(3)

while True:
    print("Checking new messages...")

    # 🖱 Select chat text (CHANGE COORDINATES IF NEEDED)
    pyautogui.moveTo(1026, 244)
    pyautogui.dragTo(1131, 1321, duration=1.5, button='left')
    time.sleep(2)

    # 📋 Copy
    pyautogui.hotkey('ctrl', 'c')
    time.sleep(2)

    chat_history = pyperclip.paste()
    print("Copied Text:\n", chat_history)

    if is_last_message_from_sender(chat_history):
        print("Sender matched. Generating reply...")

        completion = client.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=[
                {
                    "role": "system",
                    "content": "Reply like Naruto. Use Hindi + English mix. Output only message text."
                },
                {
                    "role": "user",
                    "content": chat_history
                }
            ]
        )

        response = completion.choices[0].message.content
        print("Bot Reply:", response)

        # 📋 Copy reply
        pyperclip.copy(response)
        time.sleep(1)

        # 🖱 Click message box (CHANGE COORDINATE)
        pyautogui.click(1808, 1328)
        time.sleep(1)

        # ⌨ Paste + send
        pyautogui.hotkey('ctrl', 'v')
        time.sleep(1)
        pyautogui.press('enter')

    else:
        print("No new message from sender.")

    time.sleep(5)