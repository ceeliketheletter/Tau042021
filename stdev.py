import numpy as np

print "Compute the standard deviation!"

points = [] 

point = raw_input("Add a point? ")
while point == 'y':

  x = np.float(raw_input("Data point: "))
  points.append(x)
  point = raw_input("Add a point? ")
  print " "

print " Points: " , points

avg  = sum(points) / len(points)

n = len(points)

squares = []

for i in points:
    square = (i - avg)**2
    squares.append(square)

sd = np.sqrt(  sum(squares) / n ) 

print " "
print "Standard Deviation: " , sd

stdev = np.std(points)
print "Check: " , stdev

print "avg:" , avg
