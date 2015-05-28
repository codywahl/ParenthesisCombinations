#A common recursive solution to the parenthesis combinations problem. 
def get_parentheses_combinations(string, count, left, right):
    
    #Left and Right count must be equal and when added together must be 2x the pair count. 
    if ((right + left == 2 * count) and (left == right)):
        print(string)
    else:
        #Left or Right parenthesis' can't outnumber the total count.
        #If there are more right braces than left, the parenthesis are unbalanced.
        if (right <= count and left <= count and left >= right):
            #Adds left parenthesis
            get_parentheses_combinations(string + "(", count, left + 1, right);
            #Adds right parenthesis
            get_parentheses_combinations(string + ")", count, left, right + 1);


if __name__ == '__main__':
    number_of_parenthesis = int(input("Number of parenthesis?: "))
    get_parentheses_combinations('', number_of_parenthesis, 0, 0)
