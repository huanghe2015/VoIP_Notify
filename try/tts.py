#!/usr/bin/python
# coding=utf-8
# Standard library
import asyncio
import tempfile


# Third party library
import edge_tts
from playsound import playsound

# Class section


# Function section
async def main():
    """
    Main function
    """
    communicate = edge_tts.Communicate()
    ask = input("What do you want TTS to say? ")
    with tempfile.NamedTemporaryFile() as temporary_file:
        async for i in communicate.run(ask):
            if i[2] is not None:
                temporary_file.write(i[2])
        playsound(temporary_file.name)


async def get_voice(text):
    # 根据邮件主旨生成语音文件，返回语音文件名。

    pass

# Main section
if __name__ == "__main__":
    # Global Configs
    # Exec
    asyncio.get_event_loop().run_until_complete(main())
