# Description: This script uses the SpeechRecognition module to record speech
# and trancribes it to a file

# Added an __init__ section so that this can be ran as an individual script OR be imported as a module.
# See the main() as an example of how to instantiate this module.

# Import the SpeechRecognition module
import speech_recognition as sr

# Playback text to speech
import pyttsx3

class recordSpeech:

    # Setup build the transcribed speech
    def transcribe(self):
        
        # Initialize the speech recognizer module.
        record = sr.Recognizer()
        
        # Begin recording speech
       # mic = sr.Microphone(device_index=0)
        mic = sr.Microphone(device_index = None, sample_rate = 48000, chunk_size = 1024)
        with mic as source_recording:
            # Put recording into audio variable
            audio = record.listen(source_recording)
        
        # Return the trancribed speech
        return record.recognize_google(audio)

    def export(self, transcription):

        # open file to write
        with open('transcription.txt', mode='w') as file:
            file.write("Transcribed Speech: ")
            file.write("\n")
            file.write(transcription)

        return

def main():

    # Build the object
    sp = recordSpeech()
    # Build text to be transcribed. Return it to the text variable
    text = sp.transcribe()
    # Perform the export of the speech to a file
    engine = pyttsx3.init()
    print("Spoken text: "+text)
    engine.say(text)
    engine.runAndWait()
    sp.export(text)
    
if __name__ == '__main__':
    	main()


