import speech_recognition as sr
from pydub import AudioSegment

def speech_to_text(input_path, output_path):
    sound = AudioSegment.from_ogg(input_path)
    sound.export(output_path, format="wav")

    r = sr.Recognizer()
    audio_file = sr.AudioFile(output_path)
    with audio_file as source:
        audio = r.record(source)
    query = r.recognize_google(audio_data=audio, language='ko-KR')
    return query