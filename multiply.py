from os import error

def multiply_list(input_list):
    try:
        output = 1
        for number in input_list:
            output = int(output * number)
        return output
    except error:
        return False

if __name__ == "__main__":
    print(multiply_list([1,2,3,7]))
