import asyncio
import time

async def example(message):
    print(f'{time.ctime()} - start of: {message}')
    await asyncio.sleep(1)
    print(f'{time.ctime()} - end of: {message}')


async def main():
    # Start coroutine twice
    first_awaitable = example('First call')
    second_awaitable = example('Second call')
    # Wait for coroutine for finish
    await first_awaitable
    await second_awaitable

asyncio.run(main())

# Running result 
# Wed Aug  9 15:15:09 2023 - start of: First call
# Wed Aug  9 15:15:10 2023 - end of: First call
# Wed Aug  9 15:15:10 2023 - start of: Second call
# Wed Aug  9 15:15:11 2023 - end of: Second call