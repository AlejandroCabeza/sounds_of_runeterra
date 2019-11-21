# Python Imports
import time
import asyncio
from io import BytesIO
# Third-Party Imports
# Project Imports
from audio.audio import AudioPlayer
from tts.gtts import synthesize_text
from cards.wrapper_cards import create_cards
from api.data_structures.states import GameStates
from api.services import get_game_state, get_player_names, get_game_result


class App:

    def __init__(self):
        print("Initialising")
        import os
        os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = "../creds.json"

        self.cards = create_cards("../cards_field.json", "../cards_data.json")
        self.player = AudioPlayer()

    async def loop(self):
        print("Checking game state")
        state = await get_game_state()
        while state != GameStates.InProgress:
            state: GameStates = await get_game_state()
            print(str(state))
            await asyncio.sleep(1)
        print("Reading players names")
        players = await get_player_names()
        print("Reproducing sounds")

        player_1, player_2 = players.values()
        print(f"Handling {player_1} : {player_2}")
        player_name_audio = synthesize_text(f"{player_1} vs {player_2}", "en-us")
        await self.player.add_audio_buffer(time.time(), BytesIO(player_name_audio).getbuffer())
        await asyncio.sleep(3)

        while state == GameStates.InProgress:
            await asyncio.sleep(2)
            print("Checking for finished game")
            state: GameStates = await get_game_state()

        print("Game finished")

        game_result: dict = await get_game_result()
        if game_result.get("LocalPlayerWon"):
            end_game_text = "You won!"
        else:
            end_game_text = "You lost."

        end_game_audio = synthesize_text(end_game_text, "en-us")
        await self.player.add_audio_buffer(time.time(), BytesIO(end_game_audio).getbuffer())
        await asyncio.sleep(3)

        await self.player.stop()
        print("Finish")

    def run(self):
        print("Running...")
        asyncio.get_event_loop().run_until_complete(asyncio.gather(self.loop(), self.player.play()))


if __name__ == '__main__':
    app = App()
    app.run()
