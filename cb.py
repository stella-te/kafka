def process_data(callback):
    # some processing...
    result = 42
    callback(result)

def print_result(result):
    print("Result is", result)

process_data(print_result)
