import requests

def send_message_to_flask():
    url = "http://127.0.0.1:5000/send_message"
    while True:
        message = input("Enter a message to send (or 'exit' to quit): ")
        if message.lower() == "exit":
            print("Exiting...")
            break

        data = {"message": message}
        try:
            response = requests.post(url, json=data)
            if response.status_code == 200:
                print("Message sent successfully:", response.json()["message"])
            else:
                print("Failed to send message:", response.json().get("message", "Unknown error"))
        except Exception as e:
            print("Error sending message:", e)

if __name__ == "__main__":
    send_message_to_flask()
