import sys
import os
import string
import random
import marshal
import add_binary
from collections import defaultdict


to_dos = {}
search_index = {}
search_index = defaultdict(list)
loaded = []


def main_menu():
    # Prints out the main menu and let's you choose the submenu
    os.system('clear')

    print 'Welcome to the To-Do-List Main Menu \n'
    print 'Please choose the option that you want by typing the index'

    for i, menu in enumerate(menu_actions):
        print i+1, menu['title']
    print '\n'
    return


def file_to_dict():
    with open('todo.txt', 'r+b') as f:
        header = f.read(40)
        bits = int(header[:16])
        f.seek(40)
        data = f.read(bits)
        loaded_data = marshal.loads(data)
        loaded.append(loaded_data)
        while True:
            try:
                bit = int(f.read(16))
                bit = int(bit)
                f.read(24)
                data = f.read(bit)
                loaded_data = marshal.loads(data)
                loaded.append(loaded_data)
            except ValueError:
                break
        for x in loaded:
            key = x[0]
            value = x[1]
            to_dos[key] = value


def view_todo():
    """ View Menu - shows all the tasks and can filter to
    see either the done or not done ones """

    file_to_dict()

    if len(to_dos) == 0:
        print 'Nothing To Do yet'
    else:
        both = raw_input('Would you like to see both '
                         + 'done and not done To Do-s? y/n --- ')
        if both == 'y':
            """ this is how you add an index nr to
            each added element that is printed """
            for i, (k, v) in enumerate(to_dos.iteritems()):
                print i+1, v['title']

        else:
            which = raw_input('View the -done- ones or the -not done- one? \n')
            if which == 'done':
                for i, (key, todo) in enumerate(to_dos.iteritems()):
                    if todo['done']:
                        print i+1, todo['title']

            elif which == 'not done':
                for i, (key, todo) in enumerate(to_dos.iteritems()):
                    if not todo['done']:
                        print i+1, todo['title']

    print '\n6. Back'
    return


def add_todo():
    # Add Menu - adds the tasks to both to_dos and search_index
    the_key = "".join(random.sample(string.ascii_letters, 3))
    add = raw_input('Add a To Do to your list: ')
    to_dos[the_key] = {'done': False, 'title': add}

    split_title = to_dos[the_key]['title'].split()
    for word in split_title:
        search_index[word].append(the_key)

    add_binary.add_bin(to_dos)

    print "You've added", add, "to your To Do List"
    print '\n6. Back or 2. Add another one'

    return


def edit_todo():
    """ Edit Menu edits the bool of the tasks so
    they can be set to done after completion """
    for i, (k, v) in enumerate(to_dos.iteritems()):
        print i+1, v['title']

    which = int(raw_input('Choose which To Do you want to edit: \n'))

    index = to_dos.keys()[which-1]
    todo = to_dos[index]
    title = todo['title']

    if not to_dos[index]['done']:
        todo['done'] = True
        print title, 'is now done'

    elif to_dos[index]['done']:
        todo['done'] = False
        print title, 'is now not done'

    print '\n6. Back or 3. Edit another one'
    return


def unindex(to_dos_id):
    """ This function removes all the deleted uids
    from search_index if they are removed from to_dos """
    for word, uids in search_index.items():
        search_index[word] = [x for x in uids if x != to_dos_id]


def del_todo():
    """ Delete Menu - deletes the task you choose
    and calls unindex to clean up everything """
    for i, (k, v) in enumerate(to_dos.iteritems()):
        print i+1, v['title']

    which = int(raw_input('Which To Do would you like to delete? \n'))

    index = to_dos.keys()[which - 1]
    todo = to_dos[index]
    title = todo['title']

    if index in to_dos:
        del to_dos[index]
        print title, 'has been deleted from your To Do List'
        unindex(index)

    print '\n6. Back or 4. Delete another one'
    return


def search():
    """ Search menu - searches for all the tasks that
    have the same key-word in them and prints them out """
    search_this = raw_input('Type a key-word and we will show you '
                            + 'all To-Dos with that word in them: \n')
    print "Your search word is", "'", search_this, "'" \
        ", here are the results: "

    uids = search_index.get(search_this, [])
    for uid in uids:
        if uid in to_dos.keys():
            print to_dos[uid]['title']

    print '\n6. Back or 5. Search for another one'
    return


def back():
    # Back to main menu
    main_menu()


def quit():
    # Closing the program
    sys.exit()


if __name__ == "__main__":
    menu_actions = [
        # Menu Definitions - each input coresponds to a different function
        {'title': "View To-Do", 'func': view_todo},
        {'title': "Add To-Do", 'func': add_todo},
        {'title': "Edit To-Do", 'func': edit_todo},
        {'title': "Delete To-Do", 'func': del_todo},
        {'title': "Search for To-Do", 'func': search},
        {'title': "Back", 'func': back},
        {'title': "Exit", 'func': exit}
        ]

    main_menu()
    while True:
        while True:
            choice = raw_input('Select your option: ')
            try:
                choice = int(choice)-1
                break
            except:
                pass

        os.system('clear')
        menu_actions[choice]['func']()
