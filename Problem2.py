
def check_is_palindrome(word):
    try:
        revered = (word[::-1]).lower()
        if revered == word.lower():
            return True
        return False
    except Exception as e:
        print(e)


word='svs'
print('input : svs')
Output = check_is_palindrome(word=word)

with open('Problem2_output.txt','w') as x :
    x.writelines(str(Output))
    print('output it is palindrome:'+str(Output))