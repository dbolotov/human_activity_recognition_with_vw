#!/usr/bin/python
'''
Convert original dataset to Vowpal Wabbit format

code modified from original: https://github.com/zygmuntz/phraug
'''

import sys,csv


def main(in_file, out_file, format):
    
    reader = csv.reader(open(in_file), delimiter=";")
    writer = open(out_file,'w')

    # namespaces = ['f1','f2','f3','f4','f5','f6','f7','f8','f9','f10','f11','f12','f13','f14','f15','f16','f17']
    namespaces = ['f1','f2','f3','f4','f5','f6','f7','f8','f9','f10','f11','f12','f13']

    label_map = {'sitting':1, 'sittingdown': 2, 'standing': 3, 'standingup': 4, 'walking': 5}


    if format == 'vw': #convert to vw format
        header = reader.next() #skip header

        for line in reader: 
            line = line[5:] #skip the 'user', 'gender', 'how_tall', 'weight', 'body_mass_index' features
            new_line = []

            label = label_map[line[-1]]
            new_line.append("%s " % label)

            for n in namespaces:
                item = line.pop( 0 )
                new_item = "|%s %s" % ( n, item )
                new_line.append(new_item)

            new_line = " ".join(new_line)
            new_line += "\n"
            # print new_line
            writer.write(new_line)

    elif format == 'mrmr': #convert to mrmr format
        names = reader.next()

        header = [names[-1]] + names[:-1]
        # print header
        # print type(header)
        header = ",".join(header)
        header += "\n"

        writer.write(header)

        # sys.exit()
        for line in reader:
            new_line = []
            # print line

            label = label_map[line[-1]]
            new_line.append("%s" % label)

            for n in line[:-1]:
                new_line.append(n)

            new_line = ",".join(new_line)
            new_line += "\n"
            # print new_line
            writer.write(new_line)


if __name__=='__main__':
    sys.exit(main(sys.argv[1],sys.argv[2], sys.argv[3]))