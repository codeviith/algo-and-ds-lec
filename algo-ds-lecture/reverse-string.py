
# time == O(n) or O(n^2), respectively.
# space == O(n)


### cleaner
#t O(n)
#s O(1)
def in_place_rev(l):
    mid = len(l) // 2
    
    for i in range(0, mid):
        tmp = l[ i]
        l[i] = l[len(l) - 1 - i]
        l[len(l) - 1 - i] = tmp

    return l



### not clean
def rev(s):
    end_idx = len(s) - 1   #t O(1)  #s O(1)
    new_str = ""   #t O(1)  #s O(1)

    #t O(n) or O(n^2), respectively.
    #s O(n)
    for i in range(end_idx, -1, -1):
        curr_char = s[i]  #t O(1)  #s O(1)
        new_str += curr_char  #t O(1) or O(n), respectively.  #s O(n)
    
    return new_str  #t O(1)  #s O(1)


print(rev('racecar'))
print()

print(rev(['a', 'b', 'c', 'd', 'e', 'f', 'g']))
print(in_place_rev(['a', 'b', 'c', 'd', 'e', 'f', 'g']))
