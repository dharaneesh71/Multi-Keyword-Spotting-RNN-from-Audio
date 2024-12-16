import pyttsx3
import os
import random

keywords = ["Donut", "Apple", "Netflix", "Amazon", "Shower", "Soap", "Sandals", "Shark", "Bamboo", "Electricity"]
num_voices = 10
volumes = [0.0, 0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]
for keyword in keywords :
    if not os.path.exists(keyword) :
        os.makedirs(keyword)
    
for keyword in keywords :
    for voice_num in range(num_voices) :
        text = keyword
        engine = pyttsx3.init()
        rate = random.randint(0, 200)
        engine.setProperty('rate', rate)
        print(rate)
        volume = random.choice(volumes)
        engine.setProperty('volume', volume)
        engine.say(keyword)
        audio_path = os.path.join(keyword, f"{keyword}_{voice_num+1}.mp3")
        engine.save_to_file(text, audio_path)
        print("Check")
        engine.runAndWait()
