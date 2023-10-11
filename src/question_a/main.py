#add import
import question_a

string1 = ""
quitProgram = "QUITPROGRAM"

while(string1 != quitProgram):
    string1 = input("Enter a sentence or words. \nOr write QUITPROGRAM to quit the program. ")
    if(string1 != quitProgram):
        result = question_a.reverse_string(string1)
        print("The reverse string of ", string1, " is: ", result)
    else:
        print("Program has stopped. ")
        break
