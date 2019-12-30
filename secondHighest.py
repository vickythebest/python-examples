items = [20, 6,100, 8, 53, 56, 23, 87, 41, 49, 19]
counter=0
number=1
def secondHighest(list,count,number):
    
    size=len(list)
    if size > number and count <=number:
        for j in range(len(list)-1):
            if list[j]>=list[j+1]:
                temp=list[j]
                list[j]=list[j+1]
                list[j+1]=temp
        count+=1
        secondHighest(list,count,number)
#     if count ==number:    
        print(temp)

def second_larget(given_list):
        largest=None
        second_larget=None
        for current_number in given_list:
                if largest == None:
                        largest = current_number
                        print ("-",largest)
                elif current_number > largest:
                        second_larget=largest
                        print("-- second_larget --",second_larget)
                        largest=current_number
                        print("-- largest --",largest)
                elif second_larget == None:
                        second_larget=current_number
                        print("--- second_larget ---",second_larget)
                elif current_number > second_larget:
                        second_larget = current_number
                        print("---- second_larget ----",second_larget)
        return second_larget

#print(items)
# secondHighest(items,counter,number)
#print(second_larget(items))



def findsecondBig(list):
        largest=None
        second_larget=None
        
        for current in list:
                if largest == None:
                        largest=current
                elif current > largest:
                        second_larget=largest
                        largest=current
                elif second_larget==None:
                        second_larget=current
                elif current > second_larget :
                        second_larget=current
                        
        return second_larget
print(findsecondBig(items))