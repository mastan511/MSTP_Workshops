import re
def validatePhoneNumber(mobileno):
    if re.match("^[6-9][0-9]{9}",mobileno):
        return True
    else:
        return False
        
def emailValidator(email):
    emailPattern = "^[a-z|A-Z|0-9|._]{8,25}[@][a-z]{3,6}[.][a-z]{2,5}"
    if re.match(emailPattern,email):
        return True
    else:
        return False 
        