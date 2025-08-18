arr = [1, 3, 2]
print(sorted(arr))
print(arr)

if len(arr) == 0:
    raise RuntimeError('Error - array is empty')
if len(arr) % 2 == 0:
    # even
    print( sorted(arr)[len(arr)//2 - 1] )
else:
    print ( sorted(arr)[len(arr)//2] )