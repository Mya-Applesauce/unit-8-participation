messages = ["A world basked in purest light. Beneath it, grew eternal night.", "If foutains freed, the roaring cries. And titans shape from darkened eyes.", "The light and dark both burning dire. A countdown to the earth's expire.", "But lo, on hopes and dreams they send. Three Heroes at the world's end."]

def show_messages():
    for message in messages:
        print(message)

sent_messages = []

def send_messages(messages, sent_messages):
    for text in messages:
        print(text)
        sent_messages.append(text)
    del messages[:]

send_messages(messages[:], sent_messages)
print()
print(messages)
print(sent_messages)
