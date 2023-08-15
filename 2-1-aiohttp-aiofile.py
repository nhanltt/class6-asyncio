# pip install aiofiles==0.7.0
# pip install aiohttp==3.7.4.post0

import sys
import asyncio
import time

import aiohttp
import aiofiles


async def write_genre(file_name):
    """
    Uses genrenator from binaryjazz.us to write a random genre to the
    name of the given file
    """
    async with aiohttp.ClientSession() as session:
        async with session.get("https://binaryjazz.us/wp-json/genrenator/v1/genre") as response:
            genre = await response.json()

    async with aiofiles.open(file_name, "w") as new_file:
        print(f"{time.ctime()} - Writing '{genre}' to '{file_name}'...")
        await new_file.write(genre)

async def main():
    tasks = []

    print(f"{time.ctime()} - Starting ...")
    start = time.time()
    for i in range(5):
        tasks.append(write_genre(f"./asyncout/new_file{i}.txt"))

    await asyncio.gather(*tasks)

    end = time.time()
    print(f"Time to complete asyncio read/writes: {round(end - start, 2)} seconds")


if __name__ == '__main__':
    if sys.version_info[0] == 3 and \
    sys.version_info[1] >= 8 and \
    sys.platform.startswith('win'):
        asyncio.set_event_loop_policy(asyncio.WindowsSelectorEventLoopPolicy())

    asyncio.run(main())
    
    

if __name__ == "__main__":
    # On Windows, this finishes successfully, but throws 'RuntimeError: Event loop is closed'
    # The following lines fix this
    # Source: https://github.com/encode/httpx/issues/914#issuecomment-622586610
    if sys.version_info[0] == 3 and sys.version_info[1] >= 8 and sys.platform.startswith('win'):
        asyncio.set_event_loop_policy(asyncio.WindowsSelectorEventLoopPolicy())

    asyncio.run(main())

# Running result
# Tue Aug 15 15:47:04 2023 - Starting ...
# Tue Aug 15 15:47:05 2023 - Writing 'dance-samba road' to './asyncout/new_file3.txt'...
# Tue Aug 15 15:47:05 2023 - Writing 'country rockabilly' to './asyncout/new_file2.txt'...      
# Tue Aug 15 15:47:05 2023 - Writing 'protoEDMgaze' to './asyncout/new_file4.txt'...
# Tue Aug 15 15:47:05 2023 - Writing 'tribute gong' to './asyncout/new_file1.txt'...
# Tue Aug 15 15:47:05 2023 - Writing 'neuroceltic/folk star' to './asyncout/new_file0.txt'...   
# Time to complete asyncio read/writes: 1.19 seconds
# Tue Aug 15 15:47:05 2023 - Starting ...
# Tue Aug 15 15:47:06 2023 - Writing 'deathnapoletana' to './asyncout/new_file4.txt'...
# Tue Aug 15 15:47:06 2023 - Writing 'tuvan flute storm' to './asyncout/new_file1.txt'...
# Tue Aug 15 15:47:06 2023 - Writing 'brazilian clarinet' to './asyncout/new_file2.txt'...      
# Tue Aug 15 15:47:06 2023 - Writing 'panpipe gypsy invasion' to './asyncout/new_file3.txt'...
# Tue Aug 15 15:47:06 2023 - Writing 'dance orchestral' to './asyncout/new_file0.txt'...        
# Time to complete asyncio read/writes: 1.13 seconds
