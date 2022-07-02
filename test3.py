from threading import Thread
from test4 import Test_asyncio
import time

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
    
    args = {'x':50,'y':50}
    
    S = students(args)
    a = S.run()
    
    
    # print(students.kg_pound(50)) # เรียกผ่านตัว staticmethod 
