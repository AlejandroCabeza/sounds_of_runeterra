# Python Imports
from io import BytesIO
# Third-Party Imports
from google.cloud import texttospeech as tts
# Project Imports
from text_to_speech.config import DEFAULT_LANGUAGE_CODE
from text_to_speech.utils import build_voice_request, VoiceRequestParams


class TextToSpeechClient:

    def __init__(self):
        self.client = tts.TextToSpeechClient()

    def _perform_voice_request(self, string: str, language_code: str):
        voice_request: VoiceRequestParams = build_voice_request(string, language_code)
        return self.client.synthesize_speech(
            voice_request.synthesis_input,
            voice_request.voice_config,
            voice_request.audio_config
        )

    def transform_text_to_audio(self, string: str, language_code: str = DEFAULT_LANGUAGE_CODE):
        response = self._perform_voice_request(string, language_code)
        return response.audio_content

    def transform_text_to_audio_as_bytes_io(self, string: str, language_code: str = DEFAULT_LANGUAGE_CODE) -> BytesIO:
        return BytesIO(self.transform_text_to_audio(string, language_code))
