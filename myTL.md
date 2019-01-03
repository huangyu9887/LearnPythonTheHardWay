from datetime import datetime
	
prompt ='>'	
in1 = input()
print ("input %s" %in1)
if in1 == ',':
	a = datetime.now()
print ('(start,%s)' %a)
in2 = input()
print ("input %s" %in2)
if in2 == '.':
	b = datetime.now()
c = b - a
print ("done, %s s" %c)

# CHANGELOG
- 20190103
