a, b, c = int(input()), int(input()), int(input())
t = [a,b,c]
mx = t.pop(t.index(max(a,b,c)))
mn = t.pop(t.index(min(a,b,c)))
print (mx,'\n',mn,'\n',t[0])
