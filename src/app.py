# Python Imports
import asyncio
# Third-Party Imports
# Project Imports
from audio.audio import AudioPlayer
from cards.wrapper_cards import create_cards
from data_structures import services as data_structure_services
from api.services import get_game_state, get_player_names, get_game_result
from data_structures.states import GameState
from input.managers import InputManager
from text_to_speech.client import TextToSpeechClient


class App:

    def __init__(self):
        print("Loading Credentials")
        import os
        os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = "../creds.json"

        print("Initialising required data")
        self.cards = create_cards("../cards_field.json", "../cards_data.json")
        self.audio_player = AudioPlayer()
        self.input_manager = InputManager(asyncio.get_event_loop())
        self.text_to_speech_client = TextToSpeechClient()
        self.flag_stop: bool = False

    def run(self):
        print("Running...")
        asyncio.get_event_loop().run_until_complete(asyncio.gather(self.loop(), self.audio_player.play()))

    async def loop(self):
        while not self.flag_stop:
            game_state: GameState = await get_game_state()
            await self.parse_game_state(game_state)
            await asyncio.sleep(1)
        await self._stop()

    async def parse_game_state(self, game_state: GameState):
        print(f"Parsing Game State: {game_state}")
        if data_structure_services.is_game_state_in_progress(game_state):
            await self.game_state_in_progress_loop()

        elif data_structure_services.is_game_state_in_menus(game_state):
            pass

        elif data_structure_services.is_game_state_in_transition(game_state):
            pass

        else:
            # raise AttributeError
            print(f"Unexpected state encountered: {game_state}")

    async def game_state_in_progress_loop(self):
        print("Begin game")
        await self.play_player_names()

        while True:
            game_state: GameState = await get_game_state()
            if not data_structure_services.is_game_state_in_progress(game_state):
                break

        await self.play_scores()

    async def play_player_names(self):
        print("Playing player names")
        audio = self.text_to_speech_client.transform_text_to_audio_as_bytes_io(await self.get_player_names_as_text())
        await self.audio_player.add_audio_buffer(audio.getbuffer())

    async def get_player_names_as_text(self):
        players = await get_player_names()
        player_1, player_2 = players.values()
        return f"{player_1} vs {player_2}"

    async def play_scores(self):
        print("Playing scores")
        text: str = f"Game result: {await self.get_game_result_as_text()}"
        audio = self.text_to_speech_client.transform_text_to_audio_as_bytes_io(text)
        await self.audio_player.add_audio_buffer(audio.getbuffer())

    async def get_game_result_as_text(self) -> str:
        game_result: dict = await get_game_result()
        return (
            "You won!"
            if game_result.get("LocalPlayerWon") else
            "You lost."
        )

    async def _stop(self):
        print("Closing")
        await self.audio_player.stop()
        await self.input_manager.stop()
        audio = self.text_to_speech_client.transform_text_to_audio_as_bytes_io("Exiting application.")
        await self.audio_player.add_audio_buffer(audio.getbuffer())
        print("Exiting...")
        await asyncio.sleep(2)


if __name__ == '__main__':
    app = App()
    app.run()
