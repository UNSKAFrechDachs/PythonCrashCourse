def send_messages(pending_messages, sent_messages):
    while pending_messages:
        message = pending_messages.pop(0)
        print(f"Message: {message}")
        sent_messages.append(message)


messages = ["Hello", "How are you?", "I'm fine.", "What are you doing?", "Programming"]
old_messages = []

send_messages(messages[:], old_messages)
print(messages)
print(old_messages)