from typing import List

def solution(list_in: List[int], expected: int) -> bool:
    #Return tru or false if the sum of any two numbers 
    #in the list_in variable result in the expected variables value.
    
    #>>> solution([10,15,3,7])
    #True

    for number1 in list_in:
        for number2 in list_in:
            potential_k=number1 + number2
            if potential_k == expected:
                return True
    return False

if __name__=='__main__':
    from doctest import testmod
    testmod()