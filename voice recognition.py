import speech_recognition as sr

recognizer = sr.Recognizer()


def speech_recognize():
    with sr.Microphone() as source:
        print("Clearing Loud..")
        recognizer.adjust_for_ambient_noise(source)
        print("Now,You can speak..")
        audio_data = recognizer.listen(source)

        try:
            text = recognizer.recognize_google(audio_data)
            return text

        except sr.UnknownValueError:
            print("sorry, I don't know what I can do about it")

        except sr.RequestError as e:
            print("Error...")


def conversation():
    not_end = True
    while not_end:
        user_input = speech_recognize()
        if user_input is not None:
            print(f"You Said: {user_input}")
            if "hello" == user_input.lower() or "hi" == user_input.lower():
                print("Hello, How can I help you?")

            elif "how are you" == user_input.lower():
                print("I'm fine and I'm here to help you.")


            elif "what can you do" == user_input.lower():
                print(
                    "I can answer your questions, help you with your daily tasks , or talk with you about anything you want")

            elif user_input.lower() == "exit":
                print("I am happy to help you today. Have a nice time !")
                not_end = False

            else:
                print("I'm not sure how to respond to that.")

conversation()

