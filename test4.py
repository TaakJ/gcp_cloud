import asyncio


class Test_asyncio:
    def __init__(self):
        pass
        self.ans = ""
    
    def run_start(self, x, y):
        loop = asyncio.get_event_loop()
        loop.run_until_complete(self.test_connection_function())
    
    async def sum(self, x, y, t):
        print(f'ตัวแปร ({x}) + ตัวแปร ({y}) ใช้เวลาในการคำนวณ {t} seconds...')
        await asyncio.sleep(t)
        self.ans = x + y
        print(f'ได้ผลลัพทธ์ sum: {x + y}: ตามที่ต้องการ')
        return self.ans
    
    async def sub(self, x, y, t):
        print(f'ตัวแปร ({x}) - ตัวแปร ({y}) ใช้เวลาในการคำนวณ {t} seconds...')
        await asyncio.sleep(t)
        self.ans = x - y
        print(f'ได้ผลลัพทธ์ sub : {x - y}: ตามที่ต้องการ')
        return self.ans
    
    async def mul(self, x, y, t):
        print(f'ตัวแปร ({x}) * ตัวแปร ({y}) ใช้เวลาในการคำนวณ {t} seconds...')
        await asyncio.sleep(t)   
        self.ans = x * y
        print(f'ได้ผลลัพทธ์ mul : {x * y}: ตามที่ต้องการ')
        return self.ans
    
    async def test_connection_function(self):
        coros = [
            self.sum(100, 500, 1), 
            self.sub(500, 100, 2), 
            self.mul(100, 600, 3)
        ]
        results = await asyncio.wait(coros)
        print(f'Completed task: {len(results[0])}')
        [print(f"- {completed_task.result()}") for completed_task in results[0]]    
        print(f'Uncompleted task: {len(results[1])}')