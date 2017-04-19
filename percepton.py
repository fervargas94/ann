import fileinput
from numpy import array, dot, random
from random import randint

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





