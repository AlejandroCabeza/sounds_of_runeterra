from src.cards.wrapper_cards import create_cards
from src.api.services import *
from src.tts.gtts import synthesize_text
from src.audio.audio import AudioPlayer
import asyncio
import time
from io import BytesIO




if __name__ == "__main__":
    import os
    os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = "../cred.json"
    cards = create_cards()

    player = AudioPlayer()

    async def main():
        print("Checking game state")
        state = await get_game_state()
        while state != GameStates.InProgress:
            state = await get_game_state()
            print(str(state))
            await asyncio.sleep(1)
        print("Reading players names")
        players = await get_player_names()
        print("Reproducing sounds")
        for player_type, player_name in players.items():
            print(f"Handling {player_type} : {player_name}")
            player_name_audio = synthesize_text(player_name, "en-us")
            print(len(player_name_audio))
            await player.add_audio_buffer(time.time(), BytesIO(player_name_audio).getbuffer())
            await asyncio.sleep(3)
        await player.stop()
        print("Finish")
    print("Running...")
    asyncio.get_event_loop().run_until_complete(asyncio.gather(main(), player.play()))