from itertools import product, permutations

# Wikipedia gives 5 ways to completely associate 3 applications of
# binary operators, which is counted by Catalan numbers.
# ((ab)c)d   (a(bc))d   (ab)(cd)   a((bc)d)   a(b(cd))
# I could probably write a script to generate these and generalize to
# more than 4 numbers, but it seems a little overkill for this purpose

def all_ten(a: int, b: int, c: int, d: int) -> dict[set[str]]:
    """All-ten solver, brute force"""
    for i in a, b, c, d:
        if not (isinstance(i, int) and 1 <= i <= 9):
            raise ValueError("Invalid input to all_ten.")
    expressions = (
            # These are the 5 ways to completely determine order of 3 binary
            # operations
            # Here, _ represents any operation including concatenation, while
            # ? represents only +-*/, per rules of all ten.
            "((a_b)?c)?d",
            "(a?(b_c))?d",
            "(a_b)?(c_d)",
            "a?((b_c)?d)",
            "a?(b?(c_d))"
    )
    results: dict[set[str]] = {i: set() for i in range(1, 11)} 
    for expr in expressions: # Choose an expression
        for per in permutations((a, b, c, d)): # Choose an order of the numbers
            for ops in product(('+', '-', '*', '/', ''), repeat=3): # Choose operators
                e, valid = list( # Fill in our numbers
                    expr.replace('a', str(per[0]))
                        .replace('b', str(per[1]))
                        .replace('c', str(per[2]))
                        .replace('d', str(per[3]))
                ), 1
                for i in range(3): # Fill in operators
                    if valid:
                        for idx in range(len(e)):
                            if e[idx] == '_':
                                e[idx] = ops[i]
                                break
                            elif e[idx] == '?' and ops[i] != '':
                                e[idx] = ops[i]
                                break
                            elif e[idx] == '?' and ops[i] == '':
                                # We cannot use concatenation on ? per all ten
                                # rules, so the operators are no longer valid
                                valid = 0
                                break
                if valid:
                    try:
                        val = eval(''.join(e)) # Where the magic happens
                    except ZeroDivisionError:
                        continue
                    if val // 1 == val and 1 <= val <= 10:
                        # If we get a number from 1 - 10
                        results[val].add(''.join(e))
    return results
                    
if __name__ == "__main__":
    from time import time
    tstart = time()
    results = all_ten(4, 4, 4, 4)
    tend = time()
    
    for i in range(1, 11):
        print(f"SOLUTIONS FOR {i}")
        for e in results[i]:
            print(f"\t{e}")

    print(f"Calculation took {tend-tstart:.5g}s.")
