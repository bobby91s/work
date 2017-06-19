import marshal
import sys
import datetime
import time

#

# x = {'asta':'este', 'la fel':'si aici'}
# data = marshal.dumps(x)
#
# f = open('dumptest.txt', 'r+')
# f.write(repr(data))
# print repr(data)
# marshal_data = marshal.loads(data)
# print marshal_data

x = {'aYt':{'done':False, 'title':'wash car'}, 'yFH':{'done':True, 'title':'clean house'}, 'TbA': {'done':False, 'title': "walk the dog"}}
y = {}



def timeStamped(fname, fmt='%Y-%m-%d-%H-%M-%S_{fname}'):
    return datetime.datetime.now().strftime(fmt).format(fname=fname)


with open('dumptest.txt', 'ab+') as myFile:
    for element in x.items():
        element = marshal.dumps(element)
        size = len(element)   # ------------BYTE SIZE
        now = datetime.datetime.now().strftime('%Y-%d-%m %H:%M')
        line_header = str(size) + ' bits' + ' ' +str(now) + ' '
        myFile.write(line_header + element + '\n') # + '   ' + str(size) + ' bits' + '\n' )


with open('dumptest.txt', 'r+b') as openFile:
    for x in openFile:
        print x
        marsh = marshal.loads(x)
        # print marsh

    # for x in openFile:
        # print line
        # smthing = smthing.split('-')
        # size = len(element)
        # now = datetime.datetime.now().strftime('%Y-%d-%m %H:%M')
        # line_header = str(size) + ' bits' + ' ' +str(now) + '-'
        # if line_header in x:
        #     no_header = x.replace(line_header, '')
        #     # dict_elements = marshal.loads(no_header)
        #     print no_header
        # # y = dict_elements
        # dict_elements = marshal.loads(x)
        # print dict_elements
        # # print y
        # print dict_elements


    # One possible solution, need to check with other methods to see if all strings are 24 bits
# size = sys.getsizeof(len(element))
# print size
