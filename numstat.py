#This program is to provide experience working with numerical data in a file and determines and displays the following:
#Chule Hou
#14327214
#chcnd
import os
path = '/Users/chulehou/Desktop/numbers.txt'
print('File name: ' + os.path.basename(path))
try:
    #Open file
    infile = open(path, 'r')
    data = [int(line) for line in infile]
    sum = sum(data)
    count = len(data)
    average = sum/count
    max = max(data)
    min = min(data)
    range = max-min
    print('Sum: ', sum)
    print('Count: ', count)
    print('Average: ', "%.1f" % average)
    print('Maximum: ', max)
    print('Minimum: ', min)
    print('Range: ', range)
    #Close file
    infile.close
except:
    print('An error occurred.')
