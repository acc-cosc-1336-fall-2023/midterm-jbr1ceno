#add import
import question_d

string1 = ""
quitProgram = "QUITPROGRAM"

while(string1 != quitProgram):
    string1 = input("Enter an age number. \nOr write QUITPROGRAM to quit the program. ")
    if(string1 != quitProgram):
        result = question_d.get_person_category(int(string1))
        print("The age group of the person is: " + result)
    else:
        print("Program has stopped. ")
        break