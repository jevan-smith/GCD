# Author: Jevan Smith, and Juan
# Assignment: Project01
# Course: CS415

import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
import random
import time

#Debug code, save for later
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

''' 
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


def sieve(x):
    result = []
    prime = []
    p = 2
    for i in range(0, x+1):
        prime.append(True)

    while p*p <= x:
        if prime[p]:
            j = p*2
            while j <= x:
                prime[j] = False
                j += p
        p += 1

    p = 2  # reset the value of p back to 2

    while p <= x:
        if prime[p]:
            result.append(p)
        p += 1

    return result


def primefactors2(x):
    result = []
    array = sieve(x)
    value = x
    temp = x
    for i in range(len(array)):
        while value not in array:
            if value % array[i] == 0:
                value = temp // array[i]
                temp = value
                result.append(array[i])
            else:
                break
        if value in array:
            result.append(value)
            return result


def gcd_middle(m, n):
    pos1 = 0
    pos2 = 0
    result = []
    total = 1
    m_primefactors = primefactors2(m)
    n_primefactors = primefactors2(n)

    for i in range(max(len(m_primefactors), len(n_primefactors))):
        if pos2 == len(n_primefactors) or pos1 == len(m_primefactors):
            return result, total
        elif m_primefactors[pos1] == n_primefactors[pos2]:
            total *= n_primefactors[pos2]
            result.append(n_primefactors[pos2])
            pos1 += 1
            pos2 += 1
        elif m_primefactors[pos1] > n_primefactors[pos2]:
            pos2 += 1
        else:
            pos1 += 1
    return result, total


def fib_seq(k):
    """
    This function computes fibonacci sequence
    Input: one non-negative number
    Output: returns fibonacci sequence in an array
    """
    new_k = k - 1
    array = [1, 1]
    for i in range(0, new_k-1):
        total = array[i] + array[i+1]
        array.append(total)
    return array


""" 
Main program loop
"""
print("")
while True:

    print("[1] Enter 'User testing mode'")
    print("[2] Enter 'Scatter plot mode'")
    print("[3] Exit")

    option = int(input("Option: "))
    print("")

    if option == 1:
        while True:
            print("Mode: User testing")
            print("[1] Task 1")
            print("[2] Task 2")
            print("[3] Task 3")
            print("[4] Go Back")
            print("[5] Exit")

            option = int(input("Option: "))
            print("")

            if option == 1:
                print("Task 1: ")
                print("Mode: User testing")
                n = int(input("Enter positive value for 'n': "))
                print("Average number of Modulo Divisions GCD is:", gcd_avg(n))
                print("Average number of Divisions GCD is:", ica_avg(n))
                print("")

            elif option == 2:
                print("Task 2: ")
                print("Mode: User testing")
                k = int(input("Enter positive value for 'k': "))
                start = time.time()
                fib = fib_seq(k)
                print("Fibonacci Sequence:", fib)
                total_Mod = 0
                for i in range(0, k-2):
                    total_Mod += gcd_count(fib[i+1], fib[i])
                end = time.time()
                print("Total number of Modulo Divisions is:", total_Mod)
                print("Time Taken to Compute total # of modulo divisions:", end - start)
                print("")

            elif option == 3:
                print("Task 3: ")
                print("Mode: User testing")
                m = int(input("Enter positive value for 'm': "))
                n = int(input("Enter positive value for 'n': "))
                x = gcd_middle(m, n)[0]
                y = gcd_middle(m, n)[1]
                print("Prime factors for 'm':", primefactors2(m))
                print("Prime factors for 'n':", primefactors2(n))
                print("Middle-school GCD(", m, ",", n, ") = ", sep="", end="")
                if len(x) != 0:
                    for i in range(len(x)):
                        if i == len(x)-1:
                            print(x[i], end="")
                        else:
                            print(x[i], " * ", sep="", end="")
                else:
                    print("1", end="")
                print(" =", y)
                print("")

            elif option == 4:
                break

            elif option == 5:
                print("Goodbye!\n")
                exit()

            else:
                print("Invalid input, try again.\n")

    elif option == 2:
        while True:
            print("Mode: Scatter plot")
            print("[1] Task 1")
            print("[2] Task 2")
            print("[3] Task 3")
            print("[4] Go Back")
            print("[5] Exit")

            option = int(input("Option: "))
            print("")

            if option == 1:
                print("Task 1: ")
                print("Mode: Scatter plot")
                x = []
                y = []
                x1 = []
                y1 = []
                for i in range(50):
                    n = random.randint(1, 30)
                    n2 = random.randint(1, 30)
                    gcd = gcd_avg(n)
                    ica = ica_avg(n2)
                    x.append(n)
                    y.append(gcd)
                    x1.append(n2)
                    y1.append(ica)
                plt.plot(x, y, 'bs')
                plt.plot(x1, y1, 'ro')
                plt.axis([0, 30, 0, 10])
                blue_patch = mpatches.Patch(color='blue', label='Mod Division GCD')
                red_patch = mpatches.Patch(color='red', label='Division GCD')
                plt.legend(handles=[red_patch, blue_patch])
                plt.xlabel('n')
                plt.ylabel('Averages')
                plt.show()

            elif option == 2:
                print("Task 2: ")
                print("Mode: Scatter plot")
                x = []
                y = []
                k = random.randint(30, 50)
                fib = fib_seq(k)
                total_Mod = 0
                print("Fibonacci Sequence:", fib)
                for i in range(k):
                    total_Mod += gcd_count(fib[i+1], fib[i])
                    x.append(i)
                    y.append(total_Mod)
                plt.plot(x, y, 'bs')
                plt.axis([0, 30, 0, 100])
                plt.xlabel('k')
                plt.ylabel('Number of modulo divisions')
                plt.show()

            elif option == 3:
                print("Task 3: ")
                print("Mode: Scatter plot")
                print("")

            elif option == 4:
                break

            elif option == 5:
                print("Goodbye!\n")
                exit()

            else:
                print("Invalid input, try again.\n")

    elif option == 3:
        print("Goodbye!\n")
        exit()
    else:
        print("Invalid input, try again.\n")
