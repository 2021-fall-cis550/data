#! /bin/sh

# Get the following columns from parkcode data.
#  [(1, PARKID), (2, NAME), (4, CITY), (5, STATE)] 
cat "$1" | cut -d, -f1,2,4,5 | tee "$2" | column -s, -t