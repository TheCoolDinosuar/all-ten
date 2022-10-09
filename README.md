# All Ten
Art of Problem Solving has this game called All Ten. Each day, a new puzzle is
released. Using the 4 given digits and the operations
- addition,
- subtraction,
- multiplication,
- division, and
- concatentation,

the goal is to create each number from 1 to 10. The only caveat is that
concatenation cannot be used in intermediate calculations, you can only
concatenate the original digits together.

You can play the game [here](https://beastacademy.com/all-ten).

## All Ten Solver
If you don't want to think anymore, you can use this script to find all possible
answers for All Ten. To use, you can either run
```
python solve.py
```
and enter 4 digits, or you can pass them as arguments like so:
```
python solve.py 4 4 4 4
```
