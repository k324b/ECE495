import pyttsx3

class TextToSpeechService:
    def __init__(self):
        # We initialize inside the speak method to prevent the engine from hanging
        pass

    def long_form_synthesize(self, text: str):
        try:
            engine = pyttsx3.init()
            engine.setProperty('rate', 180) 
            
            # Clean text of special characters that crash the engine
            clean_text = text.replace('"', '').replace('\n', ' ').strip()
            
            engine.say(clean_text)
            engine.runAndWait()
            
            # Stop the engine completely after speaking
            engine.stop()
        except Exception as e:
            print(f"TTS Engine Error: {e}")
            
        return None, None