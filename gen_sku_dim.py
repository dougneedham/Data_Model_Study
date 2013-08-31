#~/bin/python
# Example 4 of SKU definition from : 
# http://en.wikipedia.org/wiki/Stock_keeping_unit
v = 1
c = 1
d = 1
r = 1
s = 1
total = 7

def print_sku(v,c,d,r,s):
	print "Vendor%i Collection%i Design%i Color%i Size%i V%iC%iD%iC%iZ%i" % (v,c,d,r,s,v,c,d,r,s)

for i in range(1,total):
  for j in range(1,total):
    for k in range(1,total):
      for l in range(1,total):
        for m in range(1,total):
	  print_sku(i,j,k,l,m)
