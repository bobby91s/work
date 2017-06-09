import sys
import os
import string
import random
from collections import defaultdict


to_dos = {}
search_index = {}
search_index = defaultdict(list)


def main_menu(menu_actions):
    # Prints out the main menu and let's you choose the submenu
    os.system('clear')

    print 'Welcome to the To-Do-List Main Menu \n'
    print 'Please choose the option that you want by typing the index'

    for x in range(1, 7):
        print x, menu_actions[str(x)]['title']
    print '\n'

    return


def view_todo():
    """ View Menu - shows all the tasks and can filter to
    see either the done or not done ones """

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

    # for x in range(0):
    print '\n0. Back'
    return


def add_todo():
    # Add Menu - adds the tasks to both to_dos and search_index
    the_key = "".join(random.sample(string.ascii_letters, 3))
    add = raw_input('Add a To Do to your list: ')
    to_dos[the_key] = {'done': False, 'title': add}

    split_title = to_dos[the_key]['title'].split()
    for word in split_title:
        search_index[word].append(the_key)

    print "You've added", add, "to your To Do List"
    print '\n0. Back or 2. Add another one'
    return


def edit_todo():
    """ Edit Menu edits the bool of the tasks so
    they can be set to done after completion """
    for i, (k, v) in enumerate(to_dos.iteritems()):
        print i+1, v['title']

    this_one = int(raw_input('Choose which To Do you want to edit: \n'))
    for change_this, values in to_dos.items():
        change_this = to_dos.keys()[this_one - 1]
        change_this_title = to_dos[change_this]['title']
        if not to_dos[change_this]['done']:
            to_dos[change_this]['done'] = True
            print change_this_title, 'is now done'
            break

        elif to_dos[change_this]['done']:
            to_dos[change_this]['done'] = False
            print change_this_title, 'is now not done'
            break

    print '\n0. Back or 3. Edit another one'
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

    for remove_this, values in to_dos.items():
        remove_this = to_dos.keys()[which - 1]
        remove_this_title = to_dos[remove_this]['title']
        # print remove_this, remove_this_title
        if remove_this in to_dos:
            del to_dos[remove_this]
            print remove_this_title, 'has been deleted from your To Do List'
            unindex(remove_this)
            break

    print '\n0. Back or 4. Delete another one'
    return


def search():
    """ Search menu - searches for all the tasks that
    have the same key-word in them and prints them out """
    search_this = raw_input('Type a key-word and we will show you '
                            + 'all To-Dos with that word in them: \n')
    print "Your search word is", "'", search_this, "'"
    + ", here are the results: "

    uids = search_index.get(search_this, [])
    for uid in uids:
        if uid in to_dos.keys():
            print to_dos[uid]['title']

    print '\n0. Back or 5. Search for another one'
    return


def back():
    # Back to main menu
    menu_actions['main_menu'](menu_actions)


def quit():
    # Closing the program
    sys.exit()


if __name__ == "__main__":
    menu_actions = {
        # Menu Definitions - each input coresponds to a different function
        'main_menu': main_menu,
        '1': {'title': "View To-Do", 'func': view_todo},
        '2': {'title': "Add To-Do", 'func': add_todo},
        '3': {'title': "Edit To-Do", 'func': edit_todo},
        '4': {'title': "Delete To-Do", 'func': del_todo},
        '5': {'title': "Search for To-Do", 'func': search},
        '6': {'title': "Exit", 'func': exit},
        '0': {'title': "Back", 'func': back}
        }

    main_menu(menu_actions)
    while True:
        choice = raw_input('Select your option: ')
        os.system('clear')
        menu_actions[choice]['func']()
