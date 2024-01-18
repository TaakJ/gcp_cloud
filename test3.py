from threading import Thread
from test4 import Test_asyncio
import time
import json

# instances method ต้องกำหนดตัวแปรให้หมดทั้ง 4 ตัว เวลาเรียกใช้งาน
class students:
    
    def __init__(self, method_args):
    #    Thread.__init__(self)
        
        self.x = method_args.get("x")
        self.y = method_args.get("y") 
    
    def bmi(self): 
        return self.x / self.y
    
    @staticmethod
    def kg_pound(kg):
        return kg * 2.20462
    
    @staticmethod
    def foo():
        return students.num_users
    
    def run(self):
        t1 = time.time()
        app = Test_asyncio()
        app.run_start(self.x, self.y)
    
        t2 = time.time() - t1
        print(f'Executed in {t2:0.2f} seconds.')

if __name__ == '__main__':
    # s1 = students({'x':2,'y':100})
    # s1.run()
    
    null_test = {'object1': None,
                'object2': None
                }
    test = json.dumps({k: v if v is not None else '' for k, v in null_test.items()})
    print(test)