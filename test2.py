# Asynchronous I/O

import asyncio
from asyncore import loop
import time


class Test_asyncio:
    def __init__(self):
        pass
    
    def run_start(self):
        loop = asyncio.get_event_loop()
        loop.run_until_complete(self.main())
        
    async def cook(self, food, t):
        print(f'Microwave ({food}): Cooking {t} seconds...')
        await asyncio.sleep(t)
        print(f'Microwave ({food}): Finished cooking')
        return f'{food} is completed'
    
    async def main(self):
        coros = [self.cook('Rice', 3), self.cook('Eggs', 10), self.cook('Milk', 1)]
        results = await asyncio.wait(coros)
        print(f'Completed task: {len(results[0])}')
        [print(f"- {completed_task.result()}") for completed_task in results[0]]    
        print(f'Uncompleted task: {len(results[1])}')

# async def wash(basket):
#     print(f'Washing Machine ({basket}): Put the coin')ud 0]
#     print(f'Washing Machine ({basket}): Start washing...')
#     await asyncio.sleep(5)
#     print(f'Washing Machine ({basket}): Finished washing')
#     return f'{basket} is completed'

# async def main_test():
#     # await asyncio.gather(wash('Basket A'), wash('Basket B'))
#     coro = wash('Basket A')
#     print(coro)
#     print(type(coro))
#     task = asyncio.create_task(coro)
#     print(f"start tasks with {task}")
#     print(task)
#     print(type(task))
#     result = await task
#     print(result)
    
# async def main():
#     coro = [wash(f'backet:{i}') for i in range(1, 100001)]
#     results = await asyncio.wait(coro)
#     print(f'Completed task: {len(results[0])}')
#     print(f'Uncompleted task: {len(results[1])}')
    
# async def app():
#     test  = Test_asyncio()
#     await test.main()
        
if __name__ == '__main__':
    t1 = time.time()
    # asyncio.run(app())
    app = Test_asyncio()
    app.run_start()
    
    t2 = time.time() - t1
    print(f'Executed in {t2:0.2f} seconds.')