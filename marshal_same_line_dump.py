import marshal
import sys
from datetime import datetime
import time
import os


x = {'aYt':{'done':False, 'title':'wash car'}, 'yFH':{'done':True, 'title':'clean house'}, 'TbA': {'done':False, 'title': "walk the dog"}}
y = {}
loaded = []

with open('dumptest.txt', 'r+b') as f:
    for todo in x.items():
        data = marshal.dumps(todo)
        size = len(str(data)) ##### this here represents the bit size of the original todo, NOT THE SERIALIZED ONE!!! FIX!!!!
        now = datetime.now().strftime('%Y-%d-%m %H:%M') # use unix timestamp
        s = ' '
        header = (str(size), 'bits',str(now), '-')
        header = s.join(header)
        # print header
        data = marshal.dumps(todo)
        # data = header + data
        f.write(header + data)
    # print bit_size


with open('dumptest.txt', 'r+b') as f:
    # import pdb; pdb.set_trace()
    header = f.read(26)
    bits = int(header[:2])
    f.seek(26)
    data = f.read(bits)
    loaded_data = marshal.loads(data)
    loaded.append(loaded_data)
    while True:
        try:
            bit = f.read(2)
            bit = int(bit)
            f.read(24)
            data = f.read(bit)
            loaded_data = marshal.loads(data)
            loaded.append(loaded_data)
        except ValueError:
            break
    for x in loaded:
        print x
        key = x[0]
        value = x[1]
        y[key] = value
    print y
    # IT WORKS!




# >>> f = open('dumptest.txt', 'r+b')
# >>> h = f.read(26)
# >>> bits =int(h[:2])
# >>> bits
# 52
# >>> data = f.read(bits)
# >>> data
# '(\x02\x00\x00\x00t\x03\x00\x00\x00TbA{t\x04\x00\x00\x00doneFt\x05\x00\x00\x00titles\x0c\x00\x00\x00walk the dog0'
# >>> f.tell()
# 78
# >>> f.read(2)
# '48'
# >>> f.seek(78)
# >>> bb = f.read(2)
# >>> bb
# '48'
# >>> bb = int(bb)
# >>> f.read(24)
# ' bits 2017-29-06 16:55 -'
# >>> data2 = f.read(bb)
# >>> data2
# '(\x02\x00\x00\x00t\x03\x00\x00\x00aYt{t\x04\x00\x00\x00doneFt\x05\x00\x00\x00titles\x08\x00\x00\x00wash car0'
# >>>
