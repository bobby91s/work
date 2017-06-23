import marshal

x = {'aYt':{'done':False, 'title':'wash car'}, 'yFH':{'done':True, 'title':'clean house'}, 'TbA': {'done':False, 'title': "walk the dog"}}
y = {}


f = open('dumptest.txt', 'r+b')
serialized_x = marshal.dump(x.items(), f)


g = open('dumptest.txt', 'r+b')
raw_data = marshal.load(g)
for k,v in raw_data:
        y[k]= v
print y
