import fileinput
from numpy import array, random
import random 

'''
	/********************************
		Activation function treshold
		@params List inputs
		@return 0 or 1
	*********************************
'''
def tresholdFunction(inputs):
    tres = 0
    #print(inputs)
    for i in range(0, len(inputs)):
        tres += inputs[i] * w[i]
    return 1 if tres > treshold else 0

'''
	/********************************
		Update weights
		@params List inputs
		@return error
	*********************************
'''
def getWeight(train):
	output = train[1]
	calculated = tresholdFunction(train[0])
	#print("calculated", calculated, "outpu", output)
	error = output - calculated
	for index, val in enumerate(w):
		w[index] += error * train[0][index]
	return error

training = []
test = []
w = []

#Parser
count = 0
for line in fileinput.input():
	if count == 0:
		d = int(line)
	elif count == 1:
		m = int(line)
	elif count == 2:
		n = int(line)
	elif count >= 3 and count < 3 + m:
		line = (line.rstrip('\n').rstrip('\r')).replace(" ", "")
		line = line.split(",")
		arr = ([float(value) for value in line[0:-1]])
		data = ((arr), float(line[-1]))
		training.append(data)
	else:
		line = (line.rstrip('\n').rstrip('\r')).replace(" ", "")
		line = line.split(",")
		arr = ([float(value) for value in line])
		test.append(arr)
	count += 1

#Generate random weights
for i in range(d):
	w.append(random.randrange(0, 1))

rounds = 100
treshold = random.randrange(1, 10);

#Until 100 rounds or error = 0 
while (rounds >= 0):
    rounds -= 1
    error = 0
    for train in training:
    	#http://lcn.epfl.ch/tutorial/english/perceptron/html/learning.html
        error += pow(getWeight(train), 2)
    if (error == 0):
        break

if error >= 1:
	print("no solution found")
else: 
	for val in test:
		print(tresholdFunction(val))




