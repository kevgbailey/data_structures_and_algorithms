from random import seed, sample




def make_data(data_size):#DO NOT REMOVE OR MODIFY THIS FUNCTION
    '''A generator for producing data_size random values
    '''
    seed(0)
    data = sample(range(data_size * 3), k=data_size)
    data.sort()
    while True:
        yield data

def linear_search(lyst, target):

    comparisons = 0
    for i in lyst:
        comparisons = comparisons + 1
        if i == target:
            return True, comparisons
    return False
            

def binary_search(lyst, target):
    low = 0
    high = len(lyst)
    comparisons = 0
    while low <= high:
         comparisons = comparisons + 1
         mid = low+(high - low)//2
         print(lyst[mid])
         if lyst[mid] == target:
            return True, comparisons
         elif lyst[mid] > target:
            high = mid - 1
         elif lyst[mid] < target:
            low = mid + 1
    return False
            
def jump_search(lyst, target):
    step = int((len(lyst)**.5))
    print("step size: " + str(step))
    check = 0
    comparisons = 0
    border = len(lyst) - step 
    print("border: " + str(lyst[border]))
    if len(lyst) <= 4:
        for i in lyst:
            comparisons = comparisons + 1
            if i == target:
                return True, comparisons
    while check < border:
        if lyst[check] == target:
            print(lyst[check])
            comparisons = comparisons + 1
            return True, comparisons
        elif lyst[check] < target:
            print(lyst[check])
            comparisons = comparisons + 1
            check = check + step
        elif lyst[check] > target:
            print(lyst[check])
            comparisons = comparisons + 1
            check_endpoint = check
            check = check - step
            while check <= check_endpoint:
                check = check + 1
                comparisons = comparisons + 1
                print(lyst[check])
                if lyst[check] == target:
                    return True, comparisons
    while check < len(lyst):
        check = check + 1
        print(lyst[check])
        comparisons = comparisons + 1
        if lyst[check] == target:
            return True, comparisons
    return False





def main():
    pass

if __name__ == "__main__":
    main()

#length of list: 25

test_array = [0,1,2,3,5,6,10,15,23,24,27,28,30,33,34,40,45,47,50,51,52,53,54,55]
test_array_null = [0,1,2,3,4]
print(jump_search(test_array, 4))
