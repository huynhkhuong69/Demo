def multiply_list(input_list):
        output = 1
        for x in input_list:
            if type(x) == int or type(x) == float:
                output = output * x
            else:
                return False
        return output
