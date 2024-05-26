#String Calculator

class StringCalculator:
    
    def add(self,input_string):
        delimiter = ','
        if not input_string:
            return 0
        if input_string.startswith('//'):
            newline_string = input_string.split('\n',1)
            delimiter = newline_string[0][2:]
            input_string = newline_string[1]
        input_string = input_string.replace('\n',delimiter)
        numbers = input_string.split(delimiter)
        try:
            return sum(int(num) for num in numbers)
        except ValueError:
            raise ValueError("Input string contains non numeric data.")