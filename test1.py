import datetime
from re import sub

def v1(): # list comprehension
    [print(i, i * 0.621371192) for i in range(1, 11)]

def v2(): # lambda
    m = list(
        map(
            (lambda i: i * 0.621371192), range(1, 11)
            )
        )
    print(m)
    
def v3():
    medals = [
        ["th", 1, 2, 3],
        ["kr", 4, 5, 6],
        ["jr", 7, 8, 9]
    ]
    a = [[m[0], m[1], m[2], m[3], sum(m[1:])] for m in medals]
    b = [m[0] for m in medals ]
    c = list(map((lambda m: m * m), range(1,4)))
    
    z = zip(b, c)
    y = {k:v for k,v in z}
    print(y)

    
def v4():
    t = [
        ("sun", "red"), 
        ("mon", "yellow"),
        ("tue", "pink"),
        ("wed", "green"),
        ("thu", "orange"),
        ("fri", "blue"),
        ("sat", "purple"),
        ]   
    d = {k.capitalize():v for k,v in t}
    print(d)

    today = datetime.datetime.now()
    weekday =  today.strftime('%a')
    weekcolour = d[weekday]
    print(weekday, weekcolour)
    
def v5():
    
    t1 = ["sun",
        "mon",
        "tue",
        "wed",
        "thu",
        "fri",
        "sat"]
    
    t2 = [ "red", 
        "yellow",
        "pink",
        "green",
        "orange",
        "blue",
        "purple"]
    
    z = zip(t1, t2)
    d = {k.capitalize():v for k,v in z}
    
    today = datetime.datetime.now()
    weekday =  today.strftime('%a')
    weekcolour = d[weekday]
    print(weekday, weekcolour)


def v6():
    
    _s = [1, 2, 3, 4]
    _r = [5, 6, 7, 8]
    
    # d = [(r , s) for s in _s for r in _r] 
    _z = zip(_s, _r)
    d = {k:v for k, v in _z}
    print(d)
    # _d = [r + s for s in _s for r in _r] 
    # print(_d)
    
####################
### map function ###
####################

# def addition(n):
#     return n + n

# num1 = [1,2,3,4,5,6,7]
# num2 = [8,9,10,11,12, 13, 14]

# results = list(map(addition, num))
# results = list(map(lambda x, y: x + y, num1, num2))
# print(results)

##############################################################################
# ex1 #

def add_more_two_dec(call_func): # เอา output ของ  call_func() มาใช้ คือ 1 
    def add_two () :
        return call_func() + 2
    return add_two

def add_more_dec(call_func): # เอา output ของ  call_func() มาใช้ คือ 1 
    def add_one () :
        return call_func() + 1
    return add_one
    
@add_more_two_dec
@add_more_dec
def init_one():  # เอาไปใช้กับ function อะไรบ้างให้ เพิ่ม @ชื่อ function ที่ต้องการ output ไปใช้
    return 1

# print(init_one())

# ex2 #
def time_three_dec (call_func): # เอา ouput จาก step ที่ 1 มาคำนวณ
    def mul_one (number) :
        return call_func(number) * 9999
    return mul_one

def time_two_dec (call_func):  # ทำงาน step ที่ 1 
    def time_two (number) :
        return call_func(number) + number
    return time_two

@time_three_dec # ทำงาน step ที่ 2
@time_two_dec # ทำงาน step ที่ 1 
def init_number (number) :
    print(number)
    return number


# print(init_number(9))


# ex3 #

# def greet_two(dec_arg1, dec_arg2):
#     def decorator (call_func) : 
#         def get_greeting_msg (func_arg1, func_arg2):
#             print(f"call function step 1 =>, {func_arg1}, {func_arg2} from inside wrapper")   
#             return f'call function step 2 => {call_func(dec_arg1, dec_arg2)}'
#         return get_greeting_msg
#     return decorator


def greet_one (dec_arg1, dec_arg2) : # args -> poy, toon
    def decorator (call_func) :  # call_func = greet_two_people
        def get_greeting_msg (func_arg1, func_arg2) : # func_arg1 -> tak, func_arg2 -> tok
            print("working on step => 2", func_arg1, func_arg2, dec_arg1, dec_arg2, " from inside wrapper")
            return call_func(func_arg1, func_arg2)
        return get_greeting_msg   
    return decorator

# @greet_two("poy", "toon")
@greet_one("poy", "toon")
def greet_two_people (name1, name2) :
    print(f'working on step => 1, {name1}, {name2}, From Normal Function')
    return name1, name2

print(greet_two_people("tak", "tok"))