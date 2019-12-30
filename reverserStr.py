st1="1"
st2="0"
def are_reverses(st1,st2):
    l=len(st2)-1
    print(l)
    for i in range(len(st1)):
        if(st1[i]==st2[l-i]):
            print(True)
        else:
            print(False)

def larger_than(a, b):
    if len(a) > len(b) :
        return True
    elif len(a) < len(b):
        return False
    for i in range(len(a)):
        if a[i] == b[i]:
            continue
            # return True
        elif a[i] > b[i]:
            return True
        else:
            return False
    return False #
print(larger_than(st1,st2))
