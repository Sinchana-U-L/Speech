import pyttsx3

txt_speech = pyttsx3.init()

ans = input("type the txt")
txt_speech.say(ans)
txt_speech.runAndWait()
