#
#The Basic 13 Algorithm Challenges
#

#Demo Examples:
a = [6, 5, 3, 1]
b = [-5, 6, -9, 0]
c = [9 , 3, 1, 2, 5, 8]
value = 2



#Print 1-255
print '----Print 1-255----'
def print1to255():
	for i in range(1,256):
		print i

print1to255()


#print Odds 1-255
print '----print Odds 1-255----'
def printodd1to255():
	for i in range(1,256):
		if(i%2==1):
			print i

printodd1to255()


#print Ints and Sum 0-255
print '----print Ints and Sum 0-255----'
def printsum0to255():
	sum = 0
	for i in range(0,256):
		sum +=i
		print '{} : {}'.format(i, sum)

printsum0to255()


#print Iterate and Print Array
print '----print Iterate and Print Array----'
def printarray(arg):
	for i in arg:
		print i

printarray(a)


#Find and Print Max
print '----Find and Print Max----'
def findmax(arg):
	max = arg[0]
	for i in range(1,len(arg)):
		if(arg[i] > arg[0]):
			max = arg[i]
	return max

print 'The max of array, {} is: {}'.format(a,findmax(a))


#Get Average
print '----Get Average----'
def getavg(arg):
	sum = 0
	for i in arg:
		sum += i
	return sum / float(len(arg))

print 'Average of array, {} is: {}'.format(a,getavg(a))



#Create array of odds 1 to 255
print '----ArrayofOdds1to255----'
def array1to255odd():
	a = []
	for i in range(1,255):
		if(i%2==1):
			a.append(i)
	print a

array1to255odd()


#Square the values of an array
print '----Squaring Values of Array----'
def squarevalues(arg):
	result = []
	for i in range(0,len(arg)):
		result.append(arg[i] * arg[i])
	print result

squarevalues(a)



#Compare array values to value
print '----Compare array values to defined value----'
def greaterthany(arg,val):
	count = 0
	for i in arg:
		if(i > val):
			count +=1
			print '{} is greater than {}. Count: {}'.format(i,val,count)

greaterthany(a,value)



#ZeroOutNegativeNumbers
print '----Zero Out Negative Numbers----'
def zerooutnegnum(arg):
	result = 1*arg				
	for i in range(0, len(result)):
		if(result[i] < 0):
			result[i] = 0
	return result

print 'Zero out array, {}'.format(zerooutnegnum(b))


# Finding max min and avg
print '----Finding Max Min and Avg----'
def maxminavg(arg):
	max = arg[0]
	min = arg[0]
	sum = 0
	for i in range(1,len(arg)):
		if(arg[i] > max):
			max = arg[i]
		elif(arg[i] < min):
			min = arg[i]
		sum +=arg[i]
	return max, min, sum/float(len(arg))

print 'The max: {}, min: {}, avg: {}'.format(maxminavg(a)[0], maxminavg(a)[1], maxminavg(a)[2])



#Shift Array values
print '----Shift Array Values----'
def shiftvalues(arg):
	result = [i*0 for i in range(0,len(arg))]
	for i in range(0,len(arg)):
		try:
			result[i+1] = arg[i]
		except IndexError:
			continue
	return result

print shiftvalues(c)


#Swap String for Array Negative Values
print '----Swap Negative Array Values with String----'
def swapnegvalues(arg):
	result = 1*arg
	for i in range(0,len(result)):
		if(result[i] < 0):
			result[i] = 'Dojo'
	return result

print swapnegvalues(b)