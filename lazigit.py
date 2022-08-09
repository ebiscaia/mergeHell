# Define maxNumber function
def maxNumber(n1, n2):
    if n1 >= n2:
        return n1
    return n2


# Block of comments to separate a hunk from another
#
#
#
#
#
#

# Define a lMax function
def lMax(lNumber):
    a = 0
    lMaxN = []
    while 2 * a < lNumber:
        lMaxN.append(lNumber[2 * a], lNumber[2 * a + 1])
