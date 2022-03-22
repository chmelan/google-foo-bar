from fractions import Fraction, gcd

def num_of_transients(m):
    if len(m) == 0:
        raise Exception("Can't get transient states of empty matrix")

    for r in range(len(m)):
        for c in range(len(m[r])):
            if m[r][c] != 0:
                # this is not an all-zero row, try next one
                break
        else:
            # has just finished looping over an empty row (i.e. w/o `break`)
            return r
    # reached end of table and didn't encounter all-zero row - no absorbing states
    raise Exception("Not a valid AMC matrix: no absorbing (terminal) states")

# decompose input matrix `m` on Q (t-by-t) and R (t-by-r) components
# `t` is the number of transient states
def decompose(m):
    t = num_of_transients(m)
    if t == 0:
        raise Exception("No transient states. At least initial state is needed.")

    Q = []
    for r in range(t):
        qRow = []
        for c in range(t):
            qRow.append(m[r][c])
        Q.append(qRow)
    if Q == []:
        raise Exception("Not a valid AMC matrix: no transient states")

    R = []
    for r in range(t):
        rRow = []
        for c in range(t, len(m[r])):
            rRow.append(m[r][c])
        R.append(rRow)
    if R == []:
        raise Exception("Not a valid AMC matrix: missing absorbing states")
    return Q, R

# return Identity matrix of size `t`
def identity(t):
    m = []
    for i in range(t):
        r = []
        for j in range(t):
            r.append(int(i == j))
        m.append(r)
    return m

# swap i,j rows/columns of a square matrix `m`
def swap(m, i, j):
    n = []
    s = len(m)

    if s != len(m[0]):
        raise Exception("Cannot swap non-square matrix")

    if i == j:
        # no need to swap
        return m

    for r in range(s):
        nRow = []
        tmpRow = m[r]
        if r == i:
            tmpRow = m[j]
        if r == j:
            tmpRow = m[i]
        for c in range(s):
            tmpEl = tmpRow[c]
            if c == i:
                tmpEl = tmpRow[j]
            if c == j:
                tmpEl = tmpRow[i]
            nRow.append(tmpEl)
        n.append(nRow)
    return n

# reorganize matrix so zero-rows go last (preserving zero rows order)
def sort(m):
    size = len(m)

    zero_row = -1
    for r in range(size):
        sum = 0
        for c in range(size):
            sum += m[r][c]
        if sum == 0:
            # we have found all-zero row, remember it
            zero_row = r
        if sum != 0 and zero_row > -1:
            # we have found non-zero row after all-zero row - swap these rows
            n = swap(m, r, zero_row)
            # and repeat from the begining
            return sort(n)
    #nothing to sort, return
    return m

# normalize matrix `m`
def normalize(m, use_fractions=False ):
    n = []
    for r in range(len(m)):
        sum = 0
        cols = len(m[r])
        for c in range(cols):
            sum += m[r][c]

        nRow = []

        if sum == 0:
            # all-zero row
            nRow = m[r]
        else:
            for c in range(cols):
                if use_fractions:
                    nRow.append(Fraction(m[r][c], sum))
                else:
                    nRow.append(float(m[r][c])/sum)
        n.append(nRow)
    return n

# subtract two matrices
def subtract(i, q):
    if len(i) != len(i[0]) or len(q) != len(q[0]):
        raise Exception("non-square matrices")

    if len(i) != len(q) or len(i[0]) != len(q[0]):
        raise Exception("Cannot subtract matrices of different sizes")

    s = []
    for r in range(len(i)):
        sRow = []
        for c in range(len(i[r])):
            sRow.append(i[r][c] - q[r][c])
        s.append(sRow)
    return s

# multiply two matrices
def multiply(a, b):
    if a == [] or b == []:
        raise Exception("Cannot multiply empty matrices")

    if len(a[0]) != len(b):
        raise Exception("Cannot multiply matrices of incompatible sizes")

    m = []
    rows = len(a)
    cols = len(b[0])
    iters = len(a[0])

    for r in range(rows):
        mRow = []
        for c in range(cols):
            sum = 0
            for i in range(iters):
                sum += a[r][i]*b[i][c]
            mRow.append(sum)
        m.append(mRow)
    return m

# transpose matrix
def transposeMatrix(m):
    t = []
    for r in range(len(m)):
        tRow = []
        for c in range(len(m[r])):
            if c == r:
                tRow.append(m[r][c])
            else:
                tRow.append(m[c][r])
        t.append(tRow)
    return t

def getMatrixMinor(m,i,j):
    return [row[:j] + row[j+1:] for row in (m[:i]+m[i+1:])]

# matrix determinant
def getMatrixDeternminant(m):
    #base case for 1x1 matrix
    if len(m) == 1:
        return m[0][0]
    #base case for 2x2 matrix
    if len(m) == 2:
        return m[0][0]*m[1][1]-m[0][1]*m[1][0]

    d = 0
    for c in range(len(m)):
        d += ((-1)**c)*m[0][c]*getMatrixDeternminant(getMatrixMinor(m,0,c))

    return d

# matrix inversion
def getMatrixInverse(m):
    d = getMatrixDeternminant(m)

    if d == 0:
        raise Exception("Cannot get inverse of matrix with zero determinant")

    #special case for 2x2 matrix:
    if len(m) == 2:
        return [[m[1][1]/d, -1*m[0][1]/d],
                [-1*m[1][0]/d, m[0][0]/d]]

    #find matrix of cofactors
    cofactors = []
    for r in range(len(m)):
        cofactorRow = []
        for c in range(len(m)):
            minor = getMatrixMinor(m,r,c)
            cofactorRow.append(((-1)**(r+c)) * getMatrixDeternminant(minor))
        cofactors.append(cofactorRow)
    cofactors = transposeMatrix(cofactors)
    for r in range(len(cofactors)):
        for c in range(len(cofactors)):
            cofactors[r][c] = cofactors[r][c]/d
    return cofactors

def solution(m):
    """Find the probabilty of reaching a set of terminal states, given an absorbing markov matrix
    
    Arguments:
        m (list:list:int): A transition matrix containing non-negative ints. 
         e.g.   [
                [0,1,0,0,0,1], 
                [4,0,0,3,2,0],  
                [0,0,0,0,0,0],  
                [0,0,0,0,0,0],  
                [0,0,0,0,0,0],  
                [0,0,0,0,0,0],  
                ]
    
    Returns:
        probabilities (list: int): The list of numerators of probabilities for
            each terminal state, with the last int being the common denominator

            e.g. [1,3,5,7] == 1/7, 3/7, 5/7

    Credits:
        Most of the matrix implementation is based off of mkutny's absorbing markov chain library on github https://github.com/mkutny/absorbing-markov-chains
    
        Mathematical concepts are pulled from legolord208's article on dev.to https://dev.to/legolord208/absorbing-markov-chains-how-do-they-work-46
    """
    # check for a 1x1 matrix edge case
    if len(m) < 2:
        return [1,1]
        
    # <-------find the probability of reaching each terminal state------->
    

    # normalize and sort matrix with transient states preceding terminal states 
    m_normalized = normalize(sort(m))

    # decompose the matrix -> get q and R
    Q, R = decompose(m_normalized)

    # create an identity matrix of Q
    Q_identity = identity(len(Q))

    # create fundamental matrix
    N = getMatrixInverse((subtract(Q_identity, Q)))

    # find the average number of steps to reach each terminal state
    B = multiply(N, R)

    # <-------convert the output to the desired format------->

    # convert probabilities to fractions
    fractional_probabilities = [Fraction(i).limit_denominator() for i in B[0]]
    lcd = 1
    probabilities = []

    # find the lcd of all terminal states
    for prob in fractional_probabilities [1:]:
        lcd = lcd // gcd(lcd, prob.denominator) * prob.denominator
    
    # multiply each terminal state by the factor needed to convert it to the LCD 
    # then append it to the probability list
    for i in range(len(B[0])):
        probabilities.append( int((float(lcd) / fractional_probabilities [i].denominator) * fractional_probabilities [i].numerator))

    # append the LCD to the end of the probability list    
    probabilities.append(lcd)

    
    return probabilities