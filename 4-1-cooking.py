import asyncio
import time

class Coffee:
    pass
class Egg:
    pass
class Toast:
    pass

def PourCoffee():
    print('Pouring Coffee')
    return Coffee()

async def ApplyButter():
    print(f"{time.ctime()} - Spreading butter on toast")
    await asyncio.sleep(1)
  
async def FryEggsAsync(howMany):
    print(f'{time.ctime()} - Heat pan to fry eggs')
    await asyncio.sleep(3) 
    print(f'{time.ctime()} - Frying', howMany, 'eggs')
    await asyncio.sleep(3)
    print(f'{time.ctime()} - Eggs are ready')   
    return Egg()

async def ToastAsync(slices):
    for slice in range(slices):
        print(f'{time.ctime()} - Toasting bread {slice + 1}')
        await asyncio.sleep(3)
        print(f'{time.ctime()} - Bread {slice + 1} toasted')
        await ApplyButter()
        print(f'{time.ctime()} - Toast {slice + 1} ready')
    return Toast()

async def main():
    cup = PourCoffee()
    print(f"{time.ctime()} - Coffee is ready")
    await asyncio.gather(FryEggsAsync(10), ToastAsync(10))
    
if __name__ == "__main__":
    import time
    s = time.perf_counter()
    asyncio.run(main())
    elapsed = time.perf_counter() - s
    print(f"{time.ctime()} - Breakfast cooked in",elapsed,"seconds.")