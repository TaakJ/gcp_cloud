# Asynchronous I/O

import asyncio
import test1
import time

class Test_asyn:
    def __init__(self):
        pass
        # self.t1 = time.time()
        # self.t2 = time.time() - self.t1
    
    def run_start(self):
        loop = asyncio.get_event_loop()
        loop.run_until_complete(self.main())
    
    
    async def function_test(self):
        loop = asyncio.get_event_loop()
        loop.run_until_complete(self.main())
        
    
    async def func1(self):
        t1 = time.time()
        t2 = time.time() - t1
        a = "v1"
        t = 30
        b = test1.v1()
        
        print(f'start_function ({a}): time {t} seconds...')
        await asyncio.sleep(t)
        return f'{a} is completed in {t2:0.2f} seconds.'
    
    async def func2(self):
        t1 = time.time()
        t2 = time.time() - t1
        a = "v2"
        t = 5
        b = test1.v2()
        
        print(f'start_function ({a}): time {t} seconds...')
        await asyncio.sleep(t)
        return f'{a} is completed in {t2:0.2f} seconds.'
    
    async def func3(self):
        t1 = time.time()
        t2 = time.time() - t1
        a = "v3"
        t = 15
        b = test1.v2()
        
        print(f'start_function ({a}): time {t} seconds...')
        await asyncio.sleep(t)
        return f'{a} is completed in {t2:0.2f} seconds.'
    
    async def func4(self):
        t1 = time.time()
        t2 = time.time() - t1
        a = "v4"
        t = 6
        b = test1.v4()
        
        print(f'start_function ({a}): time {t} seconds...')
        await asyncio.sleep(t)
        return f'{a} is completed in {t2:0.2f} seconds.'
    
    async def func5(self):
        t1 = time.time()
        t2 = time.time() - t1
        a = "v5"
        t = 2
        b = test1.v5()
        
        print(f'start_function ({a}): time {t} seconds...')
        await asyncio.sleep(t)
        return f'{a} is completed in {t2:0.2f} seconds.'
    
    async def func6(self):
        t1 = time.time()
        t2 = time.time() - t1
        a = "v6"
        t = 3
        b = test1.v6()
        
        print(f'start_function ({a}): time {t} seconds...')
        await asyncio.sleep(t)
        return f'{a} is completed in {t2:0.2f} seconds.'
    
    async def main(self):
        
        coros = [
            asyncio.create_task(self.func1()), 
            asyncio.create_task(self.func2()),
            asyncio.create_task(self.func3()),
            asyncio.create_task(self.func4()),
            asyncio.create_task(self.func5()),
            asyncio.create_task(self.func6()),
            ]
        
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
    app = Test_asyn()
    app.run_start()
    
    t2 = time.time() - t1
    print(f'Executed in {t2:0.2f} seconds.')