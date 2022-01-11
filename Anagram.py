def anagram_check(str1: str, str2: str) -> str:
    """
    This function takes two arguments, each a string. If two strings are anagram of each other i.e. just the rearrangements of each other, then returns a string saying so.
    Else, returns a string saying the opposite of the earlier string.
    example 1:
        str1 = "Listen"
        str2 = "Silent"
        return: "The strings are an anagram of each other"
    example 2:
        str1 = "Not"
        str2 = "sat"
        return: 'The given strings aren\'t an anagram of each other'  
    """
    #casefold both strings for comparison as a list
    casefold1 = str1.casefold()
    casefold2 = str2.casefold()
    list1 = list(casefold1)
    list2 = list(casefold2)
    #sorting before comparison
    list1.sort()
    list2.sort()
    if list1 == list2:
        return 'The strings are an anagram of each other'
    return 'The given strings aren\'t an anagram of each other'


#infinite loop till the user wants to cancel
while True:
    #taking input from the user
    str1 = input('enter string 1\n')
    str2 = input('enter string 2 \n')
    print(anagram_check(str1, str2))
    try:
        temp = int(input('if you want to continue, press 1, else press 0. \n'))
        if temp == 1:
            continue
        elif temp == 0:
            print("""
            you have exited the program. Thanks for using this.
            Made by Parth Mehta.
            contact: mparth989@gmail.com""")
            break
        else:
            print("""you did not enter a 0 or 1, program shall exit now.
Thanks for using this.
Made by Parth Mehta.
5contact: mparth989@gmail.com""")
            break
    except Exception as e:
        print("""Invalid input.""")
        print("""Thanks for using this.The program shall exit now
            Made by Parth Mehta.
            Contact: mparth989@gmail.com""")
        break
