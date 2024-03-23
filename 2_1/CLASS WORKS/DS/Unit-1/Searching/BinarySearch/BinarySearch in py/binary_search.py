pos = -1 
def search(list, n):
    l = 0
    u = len(list)-1
    while l <= u:
         mid = (l+u) // 2
         if list [mid] == n:
             globals()['pos'] = mid
             return True
         else:
                if list[mid] < n:
                    l = mid +1
                else:
                        u = mid -1
    return False

list = (4,7,8,12,13,14,19)
n = 13

if search (list, n):
    print("found at ", pos+1)
else:
    print ("not found")