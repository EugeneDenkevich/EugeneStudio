s = ['1','2','3','4',"5"]
print(s)
print(type(s))
r = map(print, s)
print(list(r))

print(list(map(lambda l: int(l)**2, s)))

string = ' and '.join(s)
print(string)

s.append(6)
print(s)