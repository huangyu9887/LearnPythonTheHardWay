	
	from datetime import datetime  


	print ("Now let's record the time cost you spend on py.101.camp")


	prompt ='计时？（，| . | /) -->:'	
	du = []
	sum = 0.0
	n = 2
	for i in range(n):

	in1= input(prompt)
	#print (in1)
	if in1 == ',':
	nowst = datetime.now()
	nowst_stamp = nowst.timestamp()
	print ((start) ,nowst_stamp)
	in2 = input(prompt)
	#print (in2)
	if in2 == '.':
	nowed = datetime.now()
	nowed_stamp = nowed.timestamp()
	du[i]= nowed_stamp - nowst_stamp
	print ("done," ,du[i],"s")


	in3 = input(prompt)

	if in3 == "/":

	sum += du[i]

	print ("总计："，sum ,"s")
	

# CHANGELOG
- 20190108 add new feature
- 20190103 init
