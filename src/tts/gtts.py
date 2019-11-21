# Python Imports
# Third-Party Imports
from google.cloud import texttospeech as tts
# Project Imports


def synthesize_text(text, lang):
    # Instantiates a client
    client = tts.TextToSpeechClient()
    # Set the text input to be synthesized
    synthesis_input = tts.types.SynthesisInput(text=text)
    # Build the voice request, select the language code ("en-US") and the ssml
    # voice gender ("neutral")
    voice = tts.types.VoiceSelectionParams(
        language_code=lang,
        ssml_gender=tts.enums.SsmlVoiceGender.FEMALE)
    # Select the type of audio file you want returned
    audio_config = tts.types.AudioConfig(
        audio_encoding=tts.enums.AudioEncoding.LINEAR16
    )
    # Perform the text-to-speech request on the text input with the selected
    # voice parameters and audio file type
    response = client.synthesize_speech(synthesis_input, voice, audio_config)
    # Note: the voice can also be specified by name.
    # Names of voices can be retrieved with client.list_voices().
    voice = tts.types.VoiceSelectionParams(
        language_code=lang,
        ssml_gender=tts.enums.SsmlVoiceGender.FEMALE
    )
    audio_config = tts.types.AudioConfig(
        audio_encoding=tts.enums.AudioEncoding.LINEAR16)
    response = client.synthesize_speech(synthesis_input, voice, audio_config)
    return response.audio_content
