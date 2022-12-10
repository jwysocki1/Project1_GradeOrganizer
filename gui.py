from tkinter import *
from sort import *
import csv

class GUI:
    Book = []   #List of [student,score]

    def __init__(self, window):
        self.window = window

        self.inputframe = Frame(self.window)
        self.inputlabel = Label(self.inputframe, text='Student name:')
        self.inputentry = Entry(self.inputframe, width=20)
        self.inputentry.insert(0, 'Ex. Jamie Brown')
        self.gradelabel = Label(self.inputframe,text='Score:')  #Entry Frame
        self.gradeentry = Entry(self.inputframe, width=5)
        self.inputlabel.pack(padx=5, side='left')
        self.inputentry.pack(padx=5, side='left')
        self.gradelabel.pack(padx=5, side='left')
        self.gradeentry.pack(padx=5, side='left')
        self.inputframe.pack(anchor='w', pady=10)

        self.submitframe = Frame(self.window)
        self.submitbutton = Button(self.submitframe, text='Enter', command=self.addstudent)
        self.undobutton = Button(self.submitframe, text='Undo', command=self.undostudent)
        self.errorlabel = Label(self.submitframe,text='Press "Enter" to add student.', width=55)
        self.undobutton.pack(side='left',padx=10)
        self.submitbutton.pack(side='left',padx=20)             #Undo, Enter, and error label and buttons
        self.errorlabel.pack(side='left',padx=7)
        self.submitframe.pack(anchor='w', pady=15)

        self.methodframe = Frame(self.window)
        self.methodlabel = Label(self.methodframe, text='Method:')
        self.radio_1 = IntVar()
        self.radio_1.set(0)
        self.alphabetradio = Radiobutton(self.methodframe, text='Alphabetically', variable=self.radio_1, value=1)
        self.numberradio = Radiobutton(self.methodframe, text='Numerically', variable=self.radio_1, value=2)
        self.methodlabel.pack(side='left', padx=10)
        self.alphabetradio.pack(side='left', padx=15)          #first two radio buttons
        self.numberradio.pack(side='left')
        self.methodframe.pack(anchor='w', pady=10)

        self.wayframe = Frame(self.window)
        self.waylabel = Label(self.wayframe, text='Preference:')
        self.radio_2 = IntVar()
        self.radio_2.set(0)
        self.increaseradio = Radiobutton(self.wayframe,text='Ascending',variable=self.radio_2, value=1)
        self.decreaseradio = Radiobutton(self.wayframe,text='Descending',variable=self.radio_2,value=2)
        self.waylabel.pack(side='left',padx=10)
        self.increaseradio.pack(side='left', padx=1)         #last two radio buttons
        self.decreaseradio.pack(side='left', padx=33)
        self.wayframe.pack(anchor='w',pady=5)

        self.exportframe = Frame(self.window)     #Export button
        self.exportbutton = Button(self.exportframe,text='Export/Organize', command=self.organize)
        self.exportbutton.pack(pady=20,padx=100)
        self.exportframe.pack(anchor='w')

        self.window.bind("<Return>", self.addstudent) #Binds the <Enter> key to the same function the enter button calls


    def undostudent(self):
        '''Deletes the last entry entered unless the export/organize button
        was pressed since the last entry.'''
        if len(GUI.Book) >= 1:
            lost_student = GUI.Book.pop()
            self.errorlabel.config(text=f"Deleted student: {lost_student[0]}")
        else:
            self.errorlabel.config(text='No students to delete.')

    def addstudent(self, *args):
        '''Determines in user input is valid, creates a list to append,
        then clears the Entry box.'''
        info = self.inputentry.get().split()
        score = self.gradeentry.get()
        info.append(score)

        if len(info) == 3:
            try:
                name = info[0] + ' ' + info[1]
                grade = float(info[2])
                GUI.Book.append([name, grade])
                self.errorlabel.config(text='')
            except:
                self.errorlabel.config(text='Invalid Input')
        elif len(info) == 2:
            try:
                name = info[0]
                grade = float(info[1])
                GUI.Book.append([name, grade])
                self.errorlabel.config(text='')
            except:
                self.errorlabel.config(text='Invalid Input')
        else:
            self.errorlabel.config(text='Invalid Input')

        self.inputentry.delete(0,END)
        self.gradeentry.delete(0,END)

    def organize(self):
        '''Determines the way the user wants the data sorted, calls the sort function,
        then calls the export function'''
        method = self.radio_1.get()
        preference = self.radio_2.get()
        if method == 1:
            if preference == 0 or preference == 1:
                up_letter_sort(GUI.Book)
            elif preference == 2:
                down_letter_sort(GUI.Book)
        elif method == 2:
            if preference == 0 or preference == 1:
                up_number_sort(GUI.Book)
            elif preference == 2:
                down_number_sort(GUI.Book)
        self.export()

    def export(self):
        '''Gives a letter grade for each students score, then creates a csv file to put the data in.
        Exports the list
        :param: GUI.Book[1] : float'''
        if len(GUI.Book[1]) == 2:
            for x in GUI.Book:
                x.append(grade(x[1]))

        with open('CS2_OrganizedGradeBook.csv', 'w', newline='') as file:
            writer = csv.writer(file, delimiter=',')
            top = ['Student','Score','Grade']
            writer.writerow(top)
            for n in GUI.Book:
                writer.writerow(n)

        self.errorlabel.config(text='Spreadsheet created!')
