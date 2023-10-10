#write functions here, don't add input('') statements here!
def test_config():
    return True

def reverse_string(string1):

    string_length = len(string1) - 1

    while(string_length >= 0):
        #print(str(string1[string_length]))
        string_length -= 1
        return string_length
    