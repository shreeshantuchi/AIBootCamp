def reverseString(text):
    return text[::-1]


def checkPalindrome(text):
    if text==reverseString(text):
        return f"the text {text} is palindrome "
    else:
        return f"the text {text} is  not palindrome "