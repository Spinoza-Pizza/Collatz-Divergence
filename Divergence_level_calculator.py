def compute_D_k(A_n, k):
    """
    Compute D_1(A_n) through D_k(A_n) for a given A_n and k.
    Returns a list of sets, where result[i] is D_{i+1}(A_n)
    """
    results = []
    current_set = {A_n}

    for step in range(1, k+1):
        next_set = set()
        for x in current_set:
            # always double
            next_set.add(2*x)
            # inverse branch if integer
            if (x - 1) % 3 == 0:
                next_set.add((x - 1) // 3)
        results.append(next_set)
        current_set = next_set  # prepare for next iteration

    return results

# Example usage:
if __name__ == "__main__":
    n = 7  # example: A_n = (4^7 - 1)/3 = 5461
    k = 5  # compute D_1 to D_5
    A_n = (4**n - 1)//3

    D_list = compute_D_k(A_n, k)
    for i, D in enumerate(D_list, start=1):
        print(f"D_{i}(A_{n}) = {sorted(D)}")
