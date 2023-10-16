class MyCalc:
    ans = 0

    '''
    UCID: sb2648
    Date: 10/15/23
    The function _is_float converts to float if the given number is not a float and returns false in case of any exceptions.
    '''
    def _is_float(self, val):
        try:
            val = float(val)
            return True
        except:
            return False

    '''
    UCID: sb2648
    Date: 10/15/23
    The function _is_int converts to float if the given number is not a int and returns false in case of any exceptions.
    '''
    def _is_int(self, val):
        try:
            val = int(val)
            return True
        except:
            return False
    '''
    UCID: sb2648
    Date: 10/15/23
    The function _as_number converts to integer if the given number is an integer then this function returns interger.
    If it is a float then it returns a value of type float 
    In either of the both cases then it returns "Not a number" Exception.
    '''
    def _as_number(self, val):
        if self._is_int(val):
            return int(val)
        elif self._is_float(val):
            return float(val)
        else:
            raise Exception("Not a number")

    '''
    UCID: sb2648
    Date: 10/15/23
    This function performs addition of two numbers for given inputs and returns the sum of two given numbers.
    If ans and a number is given as input to the function, then it returns the sum of a number and the value stored in ans variable.
    '''
    def add(self, num1, num2):
        if num1 == "ans":
            return self.add(self.ans, num2)
        else:
            num1 = self._as_number(num1)
            num2 = self._as_number(num2)
            self.ans = num1+num2
        return self.ans
    
    '''
    UCID: sb2648
    Date: 10/15/23
    This function performs subtraction of two numbers for given inputs and returns the difference of two given numbers.
    If "ans" and a number is given as input to the function, then it returns the difference of a number and the value stored in ans variable.
    '''
    def sub(self, num1, num2):
        if num1 == "ans":
            return self.sub(self.ans, num2)
        else:
            num1 = self._as_number(num1)
            num2 = self._as_number(num2)
            self.ans = num1-num2
        return self.ans

    '''
    UCID: sb2648
    Date: 10/15/23
    This function performs multipication of two numbers for given inputs and returns the multipication of two given numbers.
    If "ans" and a number is given as input to the function, then it returns the multipication of a number and the value stored in ans variable.
    '''
    def mult(self, num1, num2):
        if num1 == "ans":
            return self.mult(self.ans, num2)
        else:
            num1 = self._as_number(num1)
            num2 = self._as_number(num2)
            self.ans = num1*num2
        return self.ans

    '''
    UCID: sb2648
    Date: 10/15/23
    This function performs division of two numbers for given inputs and returns the division of two given numbers.
    If "ans" and a number is given as input to the function, then it returns the division of a number and the value stored in ans variable.
    '''
    def div(self, num1, num2):
        if num1 == "ans":
            return self.div(self.ans, num2)
        else:
            num1 = self._as_number(num1)
            num2 = self._as_number(num2)
            if num2 == 0:
                print("Can't divide by zero, sorry")
            else:
                self.ans = num1/num2
        return self.ans


if __name__ == '__main__':
    is_running = True
    iSTR = input("Are you ready?")
    calc = MyCalc()
    print(calc)
    if iSTR == "yes":
        while is_running:
            iSTR = input("What is your eq:")
            if iSTR == "quit" or iSTR == "q":
                is_running = False
            else:
                print("Your eq was " + str(iSTR))
                if "+" in iSTR:
                    nums = iSTR.split("+")
                    r = calc.add(nums[0].strip(), nums[1].strip())
                    print("R is " + str(r))
                # must be done before - check to hanlde negative values
                elif "/" in iSTR:
                    nums = iSTR.split("/")
                    r = calc.div(nums[0].strip(), nums[1].strip())
                    print("R is " + str(r))

                elif "*" in iSTR or "x" in iSTR:
                    nums = iSTR.split("*") if "*" in iSTR else iSTR.split("x")
                    r = calc.mult(nums[0].strip(), nums[1].strip())
                    print("R is " + str(r))
                # must be done last so negative numbers work
                elif "-" in iSTR:
                    nums = iSTR.split("-")
                    r = calc.sub(nums[0].strip(), nums[1].strip())
                    print("R is " + str(r))

    else:
        print("Good bye")
        is_running = False