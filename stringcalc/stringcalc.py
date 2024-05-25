#String Calculator

class StringCalculator:

    def add(self,str):
        sum = 0
        if str == "":
            return 0
        else:
            sum += int(str)
            return sum