def chop(t):
    del t[0]
    del t[-1:]
    return None

def middle(t):
    return t[1:-1]

a = [1, 2, 3, 4, 5, 6]
b = [1, 2, 3, 4, 5, 6]

print("This is the 'a' list:", a)
print('Chop chop chop')
chop(a)
print("This is the 'a' list:", a)

print("This is the 'b' list:", b)
print("This is the middle of the 'b' list:", middle(b))
print("This is the 'b' list:", b)
