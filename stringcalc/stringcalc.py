#String Calculator

class StringCalculator:
    
    def add(self,input_string):
        if not input_string:
            return 0
        input_string = input_string.replace('\n',',')
        numbers = input_string.split(',')
        try:
            return sum(int(num) for num in numbers)
        except ValueError:
            raise ValueError("Input string contains non numeric data.")