def rec_a(a: list, i: int, b: list):
    if i >= len(a):
        return []
    else:
        # Put result of rb in a list in order to extend it
        rb = [rec_b(a[i], b, 0)]
        # Get rest of the result
        ra = rec_a(a, i+1, b)
        # Merge the rest of the result with the current one
        rb.extend(ra)
        return rb

def rec_b(elem: float, b: list, k: int):
    if k >= len(b):
        return None
    elif b[k][0] <= elem <= b[k][1]:
        return [b[k][0], elem, b[k][1]]
    else:
        return rec_b(elem, b, k+1)

def rec(a, b):
    """
    PRECONDITION:
        For all k, k < len(b):
        b[k][0] <= b[k][1]
        
        and for all k, k < len(b) - 1:
        b[k][1] <= b[k+1][0]

        and for any i, k that i < len(a) and k < len(b):
        exists such i, k that:
        b[k][0] <= a[i] <= b[k][1] 
    """
    return rec_a(a, 0, b)

A = [1,2,3,7,2,6,4]
B = [[0.7, 1.5],[1.6, 2.9],[3, 4.7],[4.8, 8]]

print(rec(A, B))