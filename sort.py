def up_letter_sort(list):
    '''
    Sorts nested lists in alphabetical order.
    :param list[t][0]: str
    '''
    end = len(list)
    for n in range(0,end-1):
        for t in range(0,end-n-1):
            if list[t][0].lower() > list[t+1][0].lower():
                hold = list[t]
                list[t] = list[t+1]
                list[t+1] = hold
    return list

def down_letter_sort(list):
    '''
    Sorts nested lists in reversed alphabetical order
    :param list[t][0]: str
    '''
    end = len(list)
    for n in range(0, end - 1):
        for t in range(0, end - n - 1):
            if list[t][0].lower() < list[t + 1][0].lower():
                hold = list[t]
                list[t] = list[t + 1]
                list[t + 1] = hold
    return list

def up_number_sort(list):
    '''
    Sorts nested lists in increasing numerical order
    :param list[t][1]: float
    '''
    end = len(list)
    for n in range(0, end - 1):
        for t in range(0, end - n - 1):
            if list[t][1] > list[t + 1][1]:
                hold = list[t]
                list[t] = list[t + 1]
                list[t + 1] = hold
    return list

def down_number_sort(list):
    '''
    Sorts nested lists in decreasing numerical order
    :param list[t][1]: float
    '''
    end = len(list)
    for n in range(0, end - 1):
        for t in range(0, end - n - 1):
            if list[t][1] < list[t + 1][1]:
                hold = list[t]
                list[t] = list[t + 1]
                list[t + 1] = hold
    return list

def grade(score : float) -> str:
    '''
    Returns a letter grade
    :param score: the score of the student
    :return: the letter grade they recieved
    '''
    if score >= 97:
        grade = 'A+'
    elif score >= 93:
        grade = 'A'
    elif score >= 90:
        grade = 'A'
    elif score >= 87:
        grade = 'B+'
    elif score >= 83:
        grade = 'B'
    elif score >= 80:
        grade = 'B-'
    elif score >= 77:
        grade = 'C+'
    elif score >= 73:
        grade = 'C'
    elif score >= 70:
        grade = 'C-'
    elif score >= 67:
        grade = 'D+'
    elif score >= 63:
        grade = 'D'
    elif score >= 60:
        grade = 'D-'
    else:
        grade = 'F'
    return grade

def main():
    '''Used for testing the functions in this module'''
    listylist = [['Victor',87],['joseph',65],['jaime',77],['Cole',90],['aaron',43],
             ['kylie',66],['tyler',99]]
    up_number_sort(listylist)
    print(listylist)

if __name__ == '__main__':
    main()