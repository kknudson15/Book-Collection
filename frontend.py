'''
Graphical User Interface for Book Collection App
Created by Kyle Knudson 2019
'''

from tkinter import *
import backend


def get_selected_row(event):
        '''
        If the user selects a row in the list view it populates the values into each entry box.  
        If the list is empty nothing happens.
        inputs: a special event parameter 
        outputs: none
        '''
        try:
                global selected_tuple
                index = list1.curselection()[0]
                selected_tuple = list1.get(index)
                e1.delete(0,END)
                e1.insert(END,selected_tuple[1])
                e2.delete(0,END)
                e2.insert(END,selected_tuple[2])
                e3.delete(0,END)
                e3.insert(END,selected_tuple[3])
                e4.delete(0,END)
                e4.insert(END,selected_tuple[4])
        except IndexError:
                pass


def view_command():
        '''
        When the user clicks the view all button, all of the rows in the 
        database are inserted into the list view. 
        inputs: none 
        outputs: none
        '''
        list1.delete(0,END)
        for row in backend.view():
                list1.insert(END,row)

def search_command():
        '''
        When the user searches using the search button, the rows that much the search
        parameters are inserted into the list view.
        inputs: none
        outputs: none
        '''
        list1.delete(0, END)
        for row in backend.search(title_text.get(),author_text.get(),year_text.get(),isbn_text.get()):
                list1.insert(END,row)

def add_command():
        '''
        This function adds a book to the collection.
        inputs: none
        outputs: none
        '''
        backend.insert(title_text.get(),author_text.get(),year_text.get(),isbn_text.get())
        list1.delete(0,END)
        list1.insert(END,(title_text.get(),author_text.get(),year_text.get(),isbn_text.get()))

def delete_command():
        '''
        This function deletes an entry from the database
        inputs: none
        outputs: none
        '''
        backend.delete(selected_tuple[0])

def update_command():
        '''
        This function updates an entry in the database 
        inputs: none
        outputs: none
        '''
        backend.update(selected_tuple[0],title_text.get(),author_text.get(),year_text.get(),isbn_text.get())


#Creates a base window for the widgets to go onto
window = Tk()

#Sets the title of the window
window.wm_title("Book Collector")

'''
Creates labels and places them on the window
'''
l1= Label(window, text = 'Title')
l1.grid(row=0, column = 0)

l2= Label(window, text = 'Author')
l2.grid(row=0, column = 2)

l3= Label(window, text = 'Year')
l3.grid(row=1, column = 0)

l4 = Label(window, text = 'ISBN')
l4.grid(row=1, column = 2)

'''
Creates entry boxes that get stored in a string object
'''
title_text = StringVar()
e1 = Entry(window, textvariable= title_text)
e1.grid(row=0, column = 1)

author_text = StringVar()
e2 = Entry(window, textvariable= author_text)
e2.grid(row=0, column = 3)

year_text = StringVar()
e3 = Entry(window, textvariable= year_text)
e3.grid(row=1, column = 1)

isbn_text = StringVar()
e4 = Entry(window, textvariable= isbn_text)
e4.grid(row=1, column = 3)

'''
Creates a list box for the books to apepar in
'''
list1 = Listbox(window, height= 6, width = 35)
list1.grid(row=2, column=0, rowspan =6, columnspan = 2)

'''
Adds the scroll bar to the window
'''
sb1 = Scrollbar(window)
sb1.grid(row=2, column = 2, rowspan =6)

'''
Configes the list bar to work with the scrolls bar
'''
list1.configure(yscrollcommand=sb1.set)
sb1.configure(command=list1.yview)

'''
Binds clicking of the items in the list to the function get_selected_row
'''
list1.bind('<<ListboxSelect>>', get_selected_row)

'''
Adds buttons to the screen that correspond to different backend functions
'''
b1 = Button(window, text = "View all", width = 12, command = view_command)
b1.grid(row=2, column=3)

b2 = Button(window, text = "Search Entry", width = 12, command = search_command)
b2.grid(row=3, column=3)

b3 = Button(window, text = "Add Entry", width = 12, command = add_command)
b3.grid(row=4, column=3)

b4 = Button(window, text = "Update Selected", width = 12,command = update_command)
b4.grid(row=5, column=3)

b5 = Button(window, text = "Delete Selected", width = 12, command = delete_command)
b5.grid(row=6, column=3)

b6 = Button(window, text = "Close", width = 12, command = window.destroy)
b6.grid(row=7, column=3)


#Creates the window and displays it
window.mainloop()