#!/bin/bash

# Loop from 3 to 20
for i in {10..20}; do
    echo "Processing $i..."
    # Construct the filename with leading zeros
    filename=$(printf "polyomino%03d.txt" $i)
    # Call the Python script and redirect the output to the filename
    python polyominos_iterative.py $i > "$filename"
done

