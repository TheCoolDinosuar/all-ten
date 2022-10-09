from sys import argv
from time import time

from all_ten import all_ten



if __name__ == "__main__":
    if len(argv) == 1:
        nums = map(
            int,
            input("Please enter 4 space separated digits: ").split(' ')
        )
    elif len(argv) == 5:
        nums = map(int, argv[1:])
    else:
        print("Please give exactly 4 digits as arguments.")
        exit(-1)
        
    try:
        tstart = time()
        results = all_ten(*nums)
        tend = time()
    except Exception as e:
        print(e)
        exit(-1)
    
    for i in range(1, 11):
        print(f"SOLUTIONS FOR {i}")
        for e in results[i]:
            print(f"\t{e}")

    print(f"Calculation took {tend-tstart:.5g}s.")
