# polyominos

Simple python tool to creat polyominos, the generalization of dominos or tetrominos, known from the famous game Tetris\tm.

# Installation

First, create a conda environment via

  conda create -f environment.yml

# Usage

Run e.g.

  python polyominos.py 4

Alternatively, you can the iterative version which runs faster and consumes less memory.

  python polyominos_iterative.py 4

Both will generate and print all tetrominos:

Number of unique polyominoes up to rotation: 7
Unique Polyomino 1:
■ 
■ 
■ 
■ 

Unique Polyomino 2:
■ ■ 
■   
■   

Unique Polyomino 3:
■   
■   
■ ■ 

Unique Polyomino 4:
■ ■ 
■ ■ 

Unique Polyomino 5:
■ ■   
  ■ ■ 

Unique Polyomino 6:
■   
■ ■ 
■   

Unique Polyomino 7:
■   
■ ■ 
  ■ 


Use another number that 4 accordingly.

  polyominos_batch.sh will generate all polyominos between 10 and 20, and will store them to text files polyominoXXX.txt.
  

