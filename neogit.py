# This is a simple program made to create a merge conflict

# Function to provide the maximum value of two numbers
def maxNum(n1, n2):
    if n1 >= n2:
        return n1
    return n2


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
def lMax(lNumber):
    a = 0
    lNumber = []
    while 2 * a > len(lNumber):
        maxNum(lNumber[2 * a], lNumber[2 * a + 1])
