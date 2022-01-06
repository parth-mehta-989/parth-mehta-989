def anagram_check(str1,str2):
    casefold1=str1.casefold()
    casefold2=str2.casefold()
    list1=list(casefold1)
    list2=list(casefold2)
    list1.sort()
    list2.sort()
    if list1==list2:
        return 'The strings are anagram'
    return 'The given strings aren\'t an anagram' 
while True:
    str1=input('enter string 1\n')
    str2=input('enter string 2 \n')
    print(anagram_check(str1,str2))
    try:
        temp=int(input('if you want to continue, press 1, else press 0. \n'))
        if temp==1:
            continue
        elif temp==0:
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
    
