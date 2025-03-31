from prettytable import PrettyTable


def get_index(field, file, object):
    with open(file, 'r') as handle:
        try:
            data = eval(handle.read())
            index = data[0].index(field) - 1
            if object in data:
                for i in data:
                    if object == data[i][index]:
                        return i
            else:
                print(f'{object} is Not a entry of {file}')
        except:
            print('The File is Empty......')

def print_entry(id, file):
    x = PrettyTable()
    with open(file, 'r') as handle:
        try:
            h = eval(handle.read())
            sample = h[0]
            x.field_names = sample
            if len(id) > 0:
                for k in id:
                    row = [k] + h[k]
                    x.add_row(row)
            else:
                for i in h:
                    if i == 0: continue
                    row = [i] + h[i]
                    x.add_row(row)

            print(x)
        except:
            if len(id)>0:
                print('There are no such entries..........')
            else:
                print('The Table is Empty.........')


def new_entry(file):
    x = []
    with open(file, 'r') as handle:
        data = eval(handle.read())
        h = data[0]
        id = int(max(data)) + 1
        for i in range(1, len(h)):
            x.append(input(f'Kindly Enter New {data[0][i]} >> '))
        data[id] = x
    with open(file, 'w') as handle:
        handle.write(str(data))
        return data


def search_entry(id, file):
    with open(file, 'r') as handle:
        h = eval(handle.read())
        if id in h:
            dict = {id: h[id]}
            return dict
        else:print(f'{id} is not in {file}')


def modify_entry(id, file):
    x = []
    with open(file, 'r+') as handle:
        data = eval(handle.read())
        if id in data:
            h = data[id]
            for i in range(len(h)):
                x.append(input(f'Kindly Enter New {data[0][i + 1]} >> '))
            data[id] = x
            with open(file, 'w') as handle:
                handle.write(str(data))
        else:print('------------------------No such Entry Found------------------')


def modify_specentry(id, field, new, file):
    x = []
    with open(file, 'r') as handle:
        data = eval(handle.read())
        za = data[0]
        index = za.index(field) - 1
        if id in data:
            h = data[id]
            h[index] = new
            data[id] = h
            with open(file, 'w') as handle:
                handle.write(str(data))

        else:print('------------------------No such Entry Found------------------')


def delete_entry(id, file):
    with open(file, 'r+') as handle:
        data = eval(handle.read())
        if id in data:
            del data[id]
        else:
            print('No such Entry found')
        with open(file, 'w') as e:
            e.write(str(data))

print('=================================Library Book Management System=========================')
# defining some constants
l = ['Library_Book_Record.txt', 'Books_Purchase_Record.txt', 'Student_Lend_Record.txt']
idname = ['Book Number', 'Purchase ID', 'Lend ID']
while True:
    print('-' * 70)
    print('''
>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>Choose the Database <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<
                                
                                1]Library Books Record
                                2]Books Purchase Record
                                3]Student lend Record
                                4]Close the Database
                                                                ''')

    while True:
        try:
            o = int(input('Enter your choice >> '))
            break
        except:
            print('Please Enter one of the above options......')
    if o == 4: break
    file = l[o - 1]
    br = 0
    while True:
        print(f'''
---------------------------------------FILE:{file}------------------------------------------------
--------------------------------CHOOSE THE OPERATION THAT YOU WANT TO PERFORM -----------------------
                                        1]Display the entire database
                                        2]Display specific entries
                                        3]Modify an entry
                                        4]delete an entry
                                        5]Enter a new Entry
                                        6]Switch Database
                                        7]Close the Database''', end='')
        if o == 3:
            print('''
                                        8]Change Status''')
        else:
            print('')
        while True:
            try:
                ch = int(input('Enter your choice >>> '));break
            except:print('Please Enter on of the above choices')
        if ch == 1:
            print_entry([], file)
        if ch == 2:
            y = []
            while True:
                try:
                    no = int(input('Enter the number of entries that you want to display  >>> '));break
                except:print('Please Enter a Integral Value............')
            for i in range(no):
                while True:
                    try:
                        vfg = int(input(f'Enter the {idname[o - 1]} >> '));break
                    except:
                        print('Please Enter a Integral Value............')
                y.append(vfg)
            print_entry(y, file)
        if ch == 3:
            while True:
                try:
                    id = int(input(f'Enter the {idname[o - 1]} >>> '));break
                except: print('Please enter a integral Value......')
            modify_entry(id, file)
        if ch == 4:
            while True:
                try:
                    id = int(input(f'Enter the {idname[o - 1]} >>> '));break
                except:
                    print('Please enter a integral value...............')

            delete_entry(id, file)
        if ch == 5:
            data = new_entry(file)
            if o == 3:
                modify_specentry(get_index('Book Title', l[0], data[max(data)][0]), 'Last Student Lended',
                                 data[max(data)][1], l[0])
        if ch == 6: break
        if ch == 7:
            br = 1
            break
        if ch == 8:
            while True:
                try:
                    id = input('Enter the Lend ID >>> ');break
                except:print('Please enter a integral value...........')
            while True:
                try:
                    er = input('Enter the Status of the book >>> ');break
                except:
                    print('Please enter a integral value...........')
            modify_specentry(id, 'Status', er, file)
    if br == 1: break
