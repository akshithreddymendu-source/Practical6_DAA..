@@ -0,0 +1,36 @@
def matrix_chain_order(p):
    """
    Finds the minimum number of scalar multiplications needed 
    to multiply a chain of matrices.
    
    p: List of integers where matrix i has dimensions p[i-1] x p[i]
    """
    n = len(p) - 1  # Number of matrices
    
    # m[i][j] will store the minimum multiplication cost for matrices Ai...Aj
    # Allocating an extra row and column so indices match 1 to n
    m = [[0] * (n + 1) for _ in range(n + 1)]
    
    # L is the chain length (number of matrices being multiplied together)
    for L in range(2, n + 1):
        for i in range(1, n - L + 2):
            j = i + L - 1
            m[i][j] = float('inf')
            
            # Try every possible split point k between i and j
            for k in range(i, j):
                # Cost = cost of left subchain + cost of right subchain + cost of multiplying them
                cost = m[i][k] + m[k + 1][j] + p[i - 1] * p[k] * p[j]
                if cost < m[i][j]:
                    m[i][j] = cost
                    
    return m[1][n]

# Example Execution
if __name__ == "__main__":
    # Dimensions of 3 matrices:
    # A1: 10 x 30, A2: 30 x 5, A3: 5 x 60
    matrix_dimensions = [10, 30, 5, 60]
    
    min_ops = matrix_chain_order(matrix_dimensions)
    print(f"Minimum number of multiplications: {min_ops}")
