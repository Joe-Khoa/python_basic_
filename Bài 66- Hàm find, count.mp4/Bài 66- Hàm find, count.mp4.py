s = 'http://google.com.vn/google_image?token=2gdfgdfgdf40oooooooFO3243432433/fsdfs'
pf = s.find('/')
print(pf)
pl = s.rfind('/')
print(pl)
c = s.count('o')
print('count: ',c)

print(s.count('o',35))
print(s.count('o',1,65))