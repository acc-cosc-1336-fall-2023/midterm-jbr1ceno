#write functions here, don't add input('') statements here!

def get_person_category(age):
    
    ageGroup = ""

    if(age > 0 and age <= 1):
        ageGroup = "infant"

    elif(age > 1 and age < 13):
        ageGroup = "child"
    
    elif(age >= 13 and age < 20):
        ageGroup = "teenager"

    elif(age >= 20 and age <= 125):
        ageGroup = "adult"
    
    else:
        ageGroup = "Invalid number"

    return ageGroup