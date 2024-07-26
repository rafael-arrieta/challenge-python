def isBalanced(sequence):
    characterPairs = {'(': ')', '[': ']', '{': '}'}
    emptyArray = []

    for char in sequence:
        if char in characterPairs.keys():
            emptyArray.append(char)
        elif char in characterPairs.values():
            if not emptyArray or emptyArray[-1] != { v: k for k, v in characterPairs.items()}[char]:
                return False
            emptyArray.pop()
    return not emptyArray

    


print(isBalanced("{[()]}"))
print(isBalanced("(abc1234)"))  
print(isBalanced("{[)—(]}"))  