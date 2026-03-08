messages = ["A world basked in purest light. Beneath it, grew eternal night.", "If foutains freed, the roaring cries. And titans shape from darkened eyes.", "The light and dark both burning dire. A countdown to the earth's expire.", "But lo, on hopes and dreams they send. Three Heroes at the world's end."]

def show_messages():
    for message in messages:
        print(message)

sent_messages = []

def my_end_messages():
    while messages:
        to_send = messages.pop()

def send_messages():
    for text in messages:
        print(text)
        sent_messages.append(text)
    #my_end_messages()
    del messages[:]

    print()
    print(messages)
    print(sent_messages)

send_messages()