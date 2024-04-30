import speech_recognition as sr

r = sr.Recognizer()
m = sr.Microphone()

try:
    print("A moment of silence, please...")
    with m as source: r.adjust_for_ambient_noise(source)
    print("Set minimum energy threshold to {}".format(r.energy_threshold))
    while True:
        print("Say something!")
        with m as source: audio = r.listen(source)
        print("Got it! Now to recognize it...")
        try:
            spoken_text = r.recognize_sphinx(audio)
            print("Tadbot thinks you said: " + spoken_text)
        except sr.UnknownValueError:
            print("Tadbot could not understand audio")
        except sr.RequestError as e:
            print(f"Could not request results from Sphinx; {e}")
except KeyboardInterrupt:
    pass
 