#the next palindrome

#pali = int(input("enter your string"))
def next_palindrome(n):
    n = n+1
    while not is_palindrome(n):
        n += 1
    return n
def is_palindrome(n):
    return str(n)==str(n)[::-1]
if __name__ == '__main__':


    n = int(input("enter no. of test cases"))
    numbers =[]
    for i in range(n):
        number = int(input("enter the no.\n"))
        numbers.append(number)
    #print(numbers)

    for i in range(n):
        print(f"next palindrome for {numbers[i]} is {next_palindrome(numbers[i])}")