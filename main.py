# Author: Jevan Smith, and Juan
# Assignment: Project01
# Course: CS415


''' #Debug code, save for later
def gcd(m, n):
    """
    Euclid's algorithm for computing gcd
    Input: two non-negative numbers
    Output: Greatest common divisor of m and n
    """
    while n != 0:
        temp = m % n
        m = n
        n = temp
    return m


def ica(m, n):
    """
    Consecutive integer checking algorithm for computing gcd
    Input: two non-negative numbers
    Output: Greatest common divisor of m and n
    """
    temp = min(m, n)
    while True:
        m_temp = m % temp
        if m_temp == 0:
            n_temp = n % temp
            if n_temp == 0:
                return temp
        temp -= 1
'''


def gcd_count(m, n):
    """
    This function counts number of modulo operations
    within Euclid's algorithm
    Input: two non-negative numbers
    Output: returns number of modulo operations count
    """
    counter = 0
    while n != 0:
        temp = m % n
        m = n
        n = temp
        counter += 1
    return counter


def ica_count(m, n):
    """
    This function counts number of modulo operations
    within Consecutive integer checking algorithm
    Input: two non-negative numbers
    Output: returns number of modulo operations count
    """
    counter = 0
    temp = min(m, n)
    while True:
        m_temp = m % temp
        counter += 1
        if m_temp == 0:
            n_temp = n % temp
            counter += 1
            if n_temp == 0:
                return counter
        temp -= 1


def gcd_avg(n):
    """
    This function computes average number of
    modulo divisions within Euclid's algorithm
    Input: one non-negative number
    Output: returns average number of modulo operations
    """
    sum = 0
    for i in range(1, n+1):
        sum += gcd_count(n, i)
    return sum / n


def ica_avg(n):
    """
    This function computes average number of
    modulo divisions within Consecutive integer checking algorithm
    Input: one non-negative number
    Output: returns average number of modulo operations
    """
    sum = 0
    for i in range(1, n+1):
        sum += ica_count(n, i)
    return sum / n


print("Definition 1 Example:", gcd_avg(5))
print("Definition 2 Example:", ica_avg(5))
