#write functions here, don't add input('') statements here!
def test_config():
    return True

def reverse_string(string1):

    revString = ""

    string_length = len(string1) - 1

    while(string_length >= 0):
        revString = revString + str(string1[string_length]) #the final string that will return (reverse string in this case)
        string_length -= 1 #index aka location
    return revString
    #print(revString)
    