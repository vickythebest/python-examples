# [3, 4, 1, 2, 9]
# Returns:
#  Nothing. However, this function will print out
#  a pair of numbers that adds up to 10. For example,
#  1, 9.  If no such pair is found, it should print
#  "There is no pair that adds up to 10.".
def pair10(given_list):
    number_seen = {}
    for item in given_list:
        if (10 - item) in number_seen:
            print(str(10 -item) +',' + str(item))
            return
        else:
            number_seen[item] = 1
    print("There is no pair that adds up to 10.")