#!/bin/bash

# commands to change an existing .vw-format dataset
#
#
#

#weight 'sittingdown' and 'standingup' classes with weight 5
sed -e 's/2  /2 5  /g' -e 's/4  /4 5  /g' ../data/working/dataset.vw > ../data/working/dataset_weight_5.vw
