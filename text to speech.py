from gtts import gTTS
import os
text_enter = input("Enter the text ")

def text_to_audio(text, language='en', output_file='output.mp3'):
    output_file=input("Enter the name for the output file") +".mp3"
    # Create a gTTS object
    tts = gTTS(text=text, lang=language, slow=False)

    # Save the audio file
    tts.save(output_file)

    # Play the audio file
    os.system(f"start {output_file}")

# Example usage
text_to_audio(text_enter)
