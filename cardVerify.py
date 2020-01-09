"""
Python script to check the validity of credit card numbers
Author : PythonCircle.Com
Read more : https://www.pythoncircle.com/post/485/python-script-8-validating-credit-card-number-luhns-algorithm/
"""

import sys
import re
from datetime import date


def usage():
    msg = """

        usage:
        python3 cardVerify credit_card_numbe

        example:
        python3 credit_card_validator 34678253793

    """
    print(msg)
'''

def get_cc_number():
    if len(sys.argv) < 4:
        usage()
        sys.exit(1)

    return sys.argv[1]

def get_cc_name():
    if len(sys.argv) < 4:
        usage()
        sys.exit(1)


    return sys.argv[2]

def get_cc_cvv():
    if len(sys.argv) < 4:
        usage()
        sys.exit(1)


    return sys.argv[3]

'''

def validateName(name):
    exp = r'^[a-zA-Z ]+$'
    if re.search(exp,name):
        return True
    else:
        return False


def sum_digits(digit):
    if digit < 10:
        return digit
    else:
        sum = (digit % 10) + (digit // 10)
        return sum


def validateNumber(cc_num):
    # reverse the credit card number
    cc_num = cc_num[::-1]
    # convert to integer list
    cc_num = [int(x) for x in cc_num]
    # double every second digit
    doubled_second_digit_list = list()
    digits = list(enumerate(cc_num, start=1))
    for index, digit in digits:
        if index % 2 == 0:
            doubled_second_digit_list.append(digit * 2)
        else:
            doubled_second_digit_list.append(digit)

    # add the digits if any number is more than 9
    doubled_second_digit_list = [sum_digits(x) for x in doubled_second_digit_list]
    # sum all digits
    sum_of_digits = sum(doubled_second_digit_list)
    # return True or False
    return sum_of_digits % 10 == 0

def validateCvv(cvv):
    exp = r'\d{3}'
    if re.search(exp,cvv):
        return True
    else:
        return False

def validateExpiry(expiryDate):
    today = date.today()
    todayString = str(today)
    todayMM = todayString[5:7]
    todayYY = todayString[2:4]

    expiryMM = expiryDate[0:2]
    expiryYY = expiryDate[3:]

    expiryYYInt = int(expiryYY)
    expiryMMInt = int(expiryMM)
    todayMMInt = int(todayMM)
    todayYYInt = int(todayYY)

    '''
    print("Today ints", todayMMInt," ", todayYYInt)
    print("Expiry ints", expiryMMInt," ", expiryYYInt)
    '''
    if(expiryYYInt<todayYYInt):
        return False
    elif(expiryYY == todayYY):
        if(expiryMMInt< todayMMInt):
            return False
        else:
            return True
    else:
        return True




def checkCardValidity(cardName, cardNumber, cardCvv,cardExpiry):
    cardNumValid = validateNumber(cardNumber)
    cardNameValid = validateName(cardName)
    cardCvvValid = validateCvv(cardCvv)
    cardExpiryValid = validateExpiry(cardExpiry)
    return(cardNameValid and cardNameValid and cardCvvValid and cardExpiryValid)



if __name__ == "__main__":

    cardName = "Akash Parvatikar"
    cardNumber = "79927398713"
    cardCvv = "388"
    cardExpiry = "07/20"

    
    print("Card valid?", checkCardValidity(cardName, cardNumber, cardCvv,cardExpiry))



