#String Calculator

class StringCalculator:

    def extract_delimiter(self,input_string):
        delimiters = []
        i = 0
        while i < len(input_string):
            if input_string[i] == '[':
                j = i + 1
                while j < len(input_string) and input_string[j] != ']':
                    j += 1
                if j < len(input_string):  # Make sure we found a closing bracket
                    delimiters.append(input_string[i+1:j])
                    i = j
            i += 1
        return delimiters
    
    def add(self,input_string):
        if not input_string:
            return 0
        
        delimiters = [',']  # Default delimiter
    
        if input_string.startswith('//'):
            newline_index = input_string.index('\n')
            delimiter_part = input_string[2:newline_index]
            if delimiter_part.startswith('[') and delimiter_part.endswith(']'):
                delimiters = self.extract_delimiter(delimiter_part)
            else:
                delimiters = [delimiter_part]
            input_string = input_string[newline_index+1:]
        
        # Replace all delimiters with commas
        for delimiter in delimiters:
            input_string = input_string.replace(delimiter, ',')
        input_string = input_string.replace('\n', ',')
        
        numbers = input_string.split(',')
        negatives = [num for num in numbers if num.startswith('-')] 

        if len(negatives) > 0:
            raise ValueError (f"Negative numbers not allowed.{','.join(negatives)}")

        try:
            return sum(int(num) for num in numbers if int(num)<1000)
        except ValueError:
            raise ValueError("Input string contains non-numeric data.")