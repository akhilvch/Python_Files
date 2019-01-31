
print('hello world')
myfile = open('/Users/akhil/Downloads/Python_Files/TextFile.txt')
list1 = myfile.readlines()
print(list1);
def summer_69(arr):
    total = 0
    isbetween = False;
    for num in arr:
        if num == 6:
            isbetween = True
        if not (isbetween):
            total+=num
        else:
            pass
        if num == 9:
           isbetween = False
    return total

def spy_game(nums):
    count = 3
    for i in nums:
        if i == 0 and count > 1:
            count-=1
        if i == 7 and count == 1:
            count-=1
        if count == 0:
            return True
    return False



# Check
print(summer_69([1, 3, 5]))
print(summer_69([4, 5, 6, 7, 8, 9]))
print(summer_69([2, 1, 6, 9, 11]))
              
print(spy_game([1,2,4,0,0,7,5]))
print(spy_game([1,0,2,4,0,5,7]))
print(spy_game([1,7,2,0,4,5,0]))




