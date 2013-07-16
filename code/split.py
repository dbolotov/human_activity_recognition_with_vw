'''
split a file into two randomly, line by line. 
Usage: split.py <input file> <output file 1> <output file 2> [<probability of writing to the first file>] [<random seed>]'

https://github.com/zygmuntz/nonlinear-vowpal-wabbit/blob/master/split.py

'''

import csv
import sys
import random

def main(input_file, output_file1, output_file2, P = 0.7, seed = 'randy'):
    random.seed(seed)
    
    i = open( input_file )
    o1 = open( output_file1, 'wb' )
    o2 = open( output_file2, 'wb' )
    
    reader = csv.reader( i )
    writer1 = csv.writer( o1 )
    writer2 = csv.writer( o2 )
    
    #headers = reader.next()
    #writer1.writerow( headers )
    #writer2.writerow( headers )
    
    counter = 0
    
    for line in reader:
    	r = random.random()
    	if r > P:
    		writer2.writerow( line )
    	else:
    		writer1.writerow( line )
    	
    	counter += 1
    	if counter % 100000 == 0:
    		print counter
    

if __name__=='__main__':
    sys.exit(main(sys.argv[1],sys.argv[2],sys.argv[3],sys.argv[4],sys.argv[5]))
