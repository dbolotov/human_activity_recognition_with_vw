#!/usr/bin/python
'''
Convert original dataset to Vowpal Wabbit or mRMR format.

Code modified from original: https://github.com/zygmuntz/phraug
'''

import sys,csv


def main(in_file, out_file, format):
    
    reader = csv.reader(open(in_file), delimiter=";")
    writer = open(out_file,'w')

    # namespaces = ['b1','b2','b3','b4','b5','b6','a7','a8','a9','a10','a11','a12','a13','a14','a15','a16','a17','a18'] #use all features
    namespaces = ['b1','b2','b3','b4','b5','a6','a7','a8','a9','a10','a11','a12','a13','a14','a15','a16','a17'] #omit 'gender'
    # namespaces = ['f1','f2','f3','f4','f5','f6','f7','f8','f9','f10','f11','f12','f13','f14','f15','f16'] #omit 'user' and 'gender'
    # namespaces = ['f1','f2','f3','f4','f5','f6','f7','f8','f9','f10','f11','f12'] #omit all but accel features

    label_map = {'sitting':1, 'sittingdown': 2, 'standing': 3, 'standingup': 4, 'walking': 5}


    if format == 'vw': #convert to vw format
        header = reader.next() #skip header

        counter = 1
        for line in reader: 
            line = line[1:]#use [2:] to omit the 'user' and 'gender' features
            new_line = []

            label = label_map[line[-1]]
            new_line.append("%s " % label)
            

            for n in namespaces:
                item = line.pop( 0 )
                new_item = "|%s %s" % ( n, item )
                
                ## Uncomment section to add example number
                # if n == 'b1':
                #     new_item = "example_%s|%s %s" % ( counter, n, item )
                # else:
                #     new_item = "|%s %s" % ( n, item )  

                new_line.append(new_item)

            new_line = " ".join(new_line)
            new_line += "\n"
            writer.write(new_line)
            counter += 1

    elif format == 'mrmr': #convert to mrmr format
        names = reader.next()

        header = [names[-1]] + names[:-1]
        header = ",".join(header)
        header += "\n"

        writer.write(header)
        for line in reader:
            new_line = []

            label = label_map[line[-1]]
            new_line.append("%s" % label)

            for n in line[:-1]:
                new_line.append(n)

            new_line = ",".join(new_line)
            new_line += "\n"
            writer.write(new_line)


if __name__=='__main__':
    sys.exit(main(sys.argv[1],sys.argv[2], sys.argv[3]))