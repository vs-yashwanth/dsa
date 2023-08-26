
def is_stack_possible(string):
    count = 0
    for i in string:
        if i == 'S':
            count += 1
        elif i == 'X':
            count -= 1
        if count < 0:
            return False
    return count == 0



if __name__ == '__main__':

    # Test cases
    print(is_stack_possible("SXSSXSXX"))  # Should print True
    print(is_stack_possible("SSX"))      # Should print False
    print(is_stack_possible("SXXSX"))    # Should print False