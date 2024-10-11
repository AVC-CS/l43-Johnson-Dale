def main():
    total = 0
    iterator = 0

    while iterator < 5:
        number = int(input("Input a number: "))
        total = total + number
    
    print(total)

    ########################################
    # Do not delete the return statement
    ########################################
    return total


if __name__ == '__main__':
    main()
