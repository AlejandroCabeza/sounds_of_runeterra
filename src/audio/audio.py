# Python Imports
import asyncio
import time
from io import BytesIO
# Third-Party Imports
import simpleaudio
# Project Imports


class AudioPlayer(object):

    def __init__(self, num_channels=1, bytes_per_sample=2, sample_rate=24000):
        self.lock = asyncio.locks.Lock()
        self.current = None
        self.stop_play = False
        self.is_running = False
        self.queue = asyncio.Queue(1)
        self.config = (num_channels, bytes_per_sample, sample_rate)

    async def add_audio_buffer(self, new_audio_buffer, time_stamp=time.time()):
        if self.queue.full():
            current_waiting = (current_t, current_) = await self.queue.get()
            if current_t > time_stamp:
                await self.queue.put(current_waiting)
            else:
                await self.queue.put((time_stamp, new_audio_buffer))
        else:
            await self.queue.put((time_stamp, new_audio_buffer))

    async def stop(self):
        async with self.lock:
            self.stop_play = True

    async def play(self):
        async with self.lock:
            assert not self.is_running
            self.is_running = True
        while not self.stop_play:
            async with self.lock:
                if self.queue.full():
                    if self.current is not None:
                        self.current.stop()
                    _, buffer = await self.queue.get()
                    try:
                        self.current = simpleaudio.play_buffer(buffer, *self.config)
                    except Exception as e:
                        self.current = None
                        print(e)
            await asyncio.sleep(1)


if __name__ == "__main__":
    player = AudioPlayer(num_channels=1, bytes_per_sample=2, sample_rate=44100)
    with open("../test.wav", "rb") as f:
        audio = f.read()
    buff = BytesIO(audio).getbuffer()
    tasks = asyncio.gather(
        player.add_audio_buffer(3, buff),
        player.add_audio_buffer(1, buff),
        player.add_audio_buffer(2, buff),
    )
    asyncio.get_event_loop().run_until_complete(tasks)
    assert player.queue.full()
    audio_task = player.queue.get_nowait()
    assert audio_task[0] == 3
    assert player.queue.empty()
    player.queue.put_nowait(audio_task)

    async def test1():
        await asyncio.sleep(3)
        await player.stop()

    asyncio.get_event_loop().run_until_complete(asyncio.gather(test1(), player.play()))
