import sys
import random

from simple_term_menu import TerminalMenu
import pyfiglet

#Custom modules
sys.path.append('./sort')
import bubble
import selection
import insertion
import merge

options = {
    0: "Bubble Sort",
    1: "Selection Sort",
    2: "Insertion Sort",
    3: "Merge Sort",
    4: "Exit"
}

def sort_menu():
    values = options.values()
    terminal_menu = TerminalMenu(values, title="\nSelect a sorting algorithm...")
    menu_entry_index = terminal_menu.show()
    
    return menu_entry_index

def first_menu():
    range = ['30', '50', '75', '100', '120']
    colors = ['RED', 'BLUE', 'WHITE', 'GREEN']
    resolution = ['800x640', '1280x720', '1920x1080']

    terminal_menu_range = TerminalMenu(range, title="\nSelect a range...")
    range_index = terminal_menu_range.show()

    terminal_menu_resolution = TerminalMenu(resolution, title="\nSelect a resolution (RECOMMENDED 800x640)...")
    resolution_index = terminal_menu_resolution.show()



    filestring = range[range_index]+ " "+resolution[resolution_index]
    return filestring


if __name__ == '__main__':
    print(pyfiglet.figlet_format("Sort Visualizer"))
    N = 0
    try:
        with open('config.txt', 'r') as f:
            filestring = f.read()
            temp_arr = filestring.split(' ')
            N = temp_arr[0]
            RES = temp_arr[1].split('x')
            WIDTH = int(RES[0])
            HEIGHT = int(RES[1])

        change_option = TerminalMenu(["NO", "YES"], title="\nDo you want to change your saved configuration?")
        change_index = change_option.show()

        if(change_index==1):
            assert()

    except:
        filestring = first_menu()
        temp_arr = filestring.split(' ')
        N = temp_arr[0]
        with open('config.txt', 'w') as f:
            f.write(filestring)
    

    N=int(N)
    arr = []
    [arr.append(random.randint(100,500)) for _ in range(int(N))]

    while True:
        index=sort_menu()
        arr_copy = arr[:]
        if(index==0):
            bubble.sort(arr_copy, WIDTH, HEIGHT)
        elif(index==1):
            selection.sort(arr_copy, WIDTH, HEIGHT)
        elif(index==2):
            insertion.sort(arr_copy, WIDTH, HEIGHT)
        elif(index==3):
            merge.sort(arr_copy, WIDTH, HEIGHT)
        elif(index==4):
            break;
    
         
