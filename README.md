# diagonals
Diagonals placement puzzle

## Sample Output
```
$ time python3 diagonals.py
Solution: [[-1, -1, -1, 0, 1], [0, 0, -1, 0, 1], [1, 1, 0, 1, 1], [1, 0, -1, 0, 0], [1, 0, -1, -1, -1]]

real	0m1.220s
user	0m1.212s
sys	0m0.008s
```

## Optimization
Changing the order of `diagonalType` in the search dramatically affects search
performance. When the following order is used: `[1, -1, 0]`:

```
$ time python3 diagonals.py
Solution: [[-1, -1, -1, 0, 1], [0, 0, -1, 0, 1], [1, 1, 0, 1, 1], [1, 0, -1, 0, 0], [1, 0, -1, -1, -1]]

real	0m25.529s
user	0m25.494s
sys	0m0.020s
```

## Resources
- http://oeis.org/A264041
- http://dm.compsciclub.ru/app/quiz-n-diagonals
