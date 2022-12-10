from gui import *
'''This program gets a list of students and their scores via user input,
then organizes and grades the scores to be exported to a csv file'''
def main():
    window = Tk()
    window.title('Grade Organizer')
    window.geometry('325x250')
    window.resizable(False, False)

    widgets = GUI(window)
    window.mainloop()

if __name__ == '__main__':
    main()
    print('yeah okay idek give me an error')