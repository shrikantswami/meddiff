
def check_is_palindrome(word):
    try:
        revered = (word[::-1]).lower()
        if revered == word.lower():
            return True
        return False
    except Exception as e:
        print(e)


word='svs'
flag = check_is_palindrome(word=word)
print(flag)