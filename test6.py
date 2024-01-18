def gen(batch = None, limit = None):
    ret = []
    for i in range(1, 11): # put your data reading here and i counter (i += 1) under for
        if batch:
            ret.append(i)
            if limit and i == limit:
                if len(ret):            
                    yield ret
                return
            if len(ret) == batch:
                yield ret
                ret = []
        else:
            if limit and i > limit:
                break
            yield i
    if batch and len(ret): # yield the rest of the list
        yield ret
            
g = gen(batch=5, limit=8) # batches with limit
#g = gen(batch=5) # batches
#g = gen(limit=5) # step 1 with limit
#g = gen() # step 1 with limit
for i in g:
    print(i)