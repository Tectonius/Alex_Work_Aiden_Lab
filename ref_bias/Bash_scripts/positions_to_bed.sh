#!/bin/bash

awk '{print $1 "\t" $2-500 "\t" $2+500}' positions.txt > positions_1000_range.bed