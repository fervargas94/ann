import fileinput
from numpy import array, dot, random
from random import randint

def tresholdFunction(input):
    dot = 0
    for index, val in enumerate(input):
        dot += val * w[index]
    return 1 if dot > treshold else 0

def getWeight(train):
	output = train[1]
	calculated = tresholdFunction(train[0])
	error = output - calculated
	for index, val in enumerate(w):
		val += error * train[index]
	return error

training = []
training_result = []
test = []

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
		data = (array([float(value)for value in line[0:d]]), float(line[-1]))
		training.append(data)
	else:
		line = (line.rstrip('\n').rstrip('\r')).replace(" ", "")
		line = line.split(",")
		test.append(array([float(value)for value in line]))
	count += 1

print(training)
print(training_result)
print(test)

w = random.rand(d)
rounds = 100
treshold = randint(0, 5);

while (rounds > 0):
    rounds -= 1
    error = 0
    for train in training:
        error += pow(getWeight(train), 2)
    if (error == 0):
        break

if error >= 1:
	print("no solution found")
else: 
	for val in test:
		print(tresholdFunction(val))




