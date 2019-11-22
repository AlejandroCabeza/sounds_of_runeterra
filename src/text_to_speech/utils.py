# Python Imports
from collections import namedtuple
# Third-Party Imports
from google.cloud import texttospeech as tts
# Project Imports


VoiceRequestParams = namedtuple("VoiceRequest", ("synthesis_input", "voice_config", "audio_config"))


def build_voice_request(string: str, language_code: str) -> VoiceRequestParams:
    synthesis_input = tts.types.SynthesisInput(text=string)
    voice_config = tts.types.VoiceSelectionParams(
        language_code=language_code,
        ssml_gender=tts.enums.SsmlVoiceGender.FEMALE
    )
    audio_config = tts.types.AudioConfig(audio_encoding=tts.enums.AudioEncoding.LINEAR16)
    return VoiceRequestParams(synthesis_input, voice_config, audio_config)
