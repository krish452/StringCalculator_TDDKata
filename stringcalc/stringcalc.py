#String Calculator

class StringCalculator:

    def add(self,str):
        sum = 0
        if str == "":
            return 0
        else:
            for i in str:
                if i != ',':
                    sum += int(i)
            return sum