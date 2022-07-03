import datetime
from re import sub

def v2(): # list comprehension
    [print(i, i * 0.621371192) for i in range(1, 11)]

def v3(): # lambda
    m = list(
        map(
            (lambda i: i * 0.621371192), range(1, 11)
            )
        )
    print(m)
    
def multidim_list():
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
    
    
    
def dict_demo():
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
    
def dict_demo1():
    
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


def dict_demo2():
    
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


multidim_list()
