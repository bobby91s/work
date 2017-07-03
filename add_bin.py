import marshal
from datetime import datetime

def add_bin(to_dos):
    # import pdb; pdb.set_trace()
    with open('todo.txt', 'ab+') as myFile:
        the_keys = to_dos.keys()
        for key in the_keys:
            for todo in to_dos.items():
                for k, v in to_dos.items():
                        if key in todo:
                            todo = marshal.dumps(todo)
                            size = len(str(todo))
                            size = ("%016d" % size)
                            now = datetime.now().strftime('%Y-%d-%m %H:%M')
                            header = (str(size), 'bits',str(now), '-')
                            header = ' '.join(header)
                            if str(the_keys) in myFile.readlines():
                                pass
                            else:
                                myFile.write(header + todo)
                                break
