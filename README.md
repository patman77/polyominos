# polyominos

Simple python tool to creat polyominos, the generalization of dominos or tetrominos, known from the famous game Tetris\tm.

# Installation

First, create a conda environment via

  conda env create -f environment.yml

and activate it via

  conda activate polyominos

# Usage

Run e.g.

  python polyominos.py 4

Alternatively, you can run the iterative version which runs faster and consumes less memory.

  python polyominos_iterative.py 4

Both will generate and print all tetrominos.

Use another number than 4 accordingly.

polyominos_batch.sh will generate all polyominos between 10 and 20, and will store them to text files polyominoXXX.txt.
  

