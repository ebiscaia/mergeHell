# This is a simple program made to create a merge conflict

# Function to provide the maximum value of two numbers
<<<<<<< HEAD
def maxNumber(num1, num2):
    if num2 >= num1:
        return num2
    return num1
=======
def maxNum(n1, n2):
    if n1 >= n2:
        return n1
    return n2
>>>>>>> a6080b8218d8bd8a52f19a6047878d25d07c6aed


# Since its inception Docker has been revolutionising the way software
# is deployed in companies. Developers are taking advantage of the little
# to no time needed to configure libraries and dependencies [1], the fact
# that containers are lightweight since they only contain the essential
# packages to run the application and multiple containers in the same host,
# which is making Docker the ideal tool for development in all stages of the
# development cycle. However, to achieve that, simplifications were made
# and due to that some security concerns were raised. Because Docker
# containers do not provide kernel isolation [2], a compromised container
# can also make vulnerable the host OS or the other containers that are being
# run alongside. Virtual Machines (VMs), on the other hand, where each
# application is run in its OS and therefore has its own kernel, prevents
# this type of malware spreading to other applications even when the VMs
# are sharing the same hardware.


# list of maxNumbers
<<<<<<< HEAD
=======
def lMax(lNum):
    b = 0
    lRet = []
    while b * 2 < len(lNum):
        lRet.append(maxNum(lNum[2 * b], lNum[2 * b + 1]))
>>>>>>> a6080b8218d8bd8a52f19a6047878d25d07c6aed
