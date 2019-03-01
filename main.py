# Author: Jevan Smith, and Juan
# Assignment: Project01
# Course: CS415

import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
import random
import time


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
    """
    This function computes prime numbers using sieve's
    algorithm
    Input: one non-negative number
    Output: returns array of prime numbers up to the value
    of x
    """
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


def primefactors(x):
    """
    This function computes prime factors
    Input: one non-negative number
    Output: returns array of prime factors, based on
    the value of x
    """
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
    """
    This function computes gcd using the
    Middle-school procedure
    Input: Integer values of m, and n (non-negative number only)
    Output: result returns Array, total returns gcd value, counter
    returns total comparisons, and max_value
    returns max(len(m), len(n))
    """
    pos1 = 0
    pos2 = 0
    result = []
    total = 1
    counter = 0
    m_primefactors = primefactors(m)
    n_primefactors = primefactors(n)

    try:
        max_value = max(len(m_primefactors), len(n_primefactors))
        #  max_value = len(m_primefactors) + len(n_primefactors)
    except:
        return result, total, counter, 0

    for i in range(max(len(m_primefactors), len(n_primefactors))):
        if pos2 == len(n_primefactors) or pos1 == len(m_primefactors):
            counter += 1
            return result, total, counter, max_value
        elif m_primefactors[pos1] == n_primefactors[pos2]:
            counter += 2  # Count the previous comparison
            total *= n_primefactors[pos2]
            result.append(n_primefactors[pos2])
            pos1 += 1
            pos2 += 1
        elif m_primefactors[pos1] > n_primefactors[pos2]:
            counter += 3  # Count the previous comparisons
            pos2 += 1
        else:
            counter += 3  # Count the previous comparisons
            pos1 += 1
    return result, total, counter, max_value


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
                n = int(input("Enter positive value for 'n': "))
                print("Average number of Modulo Divisions GCD is:", gcd_avg(n))
                print("Average number of Divisions GCD is:", ica_avg(n))
                print("")

            elif option == 2:
                print("Task 2: ")
                k = int(input("Enter positive value for 'k': "))
                start = time.time()
                fib = fib_seq(k)
                print("Fibonacci Sequence:", fib)
                total_Mod = 0
                for i in range(0, k-2):
                    total_Mod += gcd_count(fib[i+1], fib[i])
                end = time.time()
                print("Total number of Modulo Divisions is:", total_Mod)
                print("Fibonacci value of k:", fib[k-1])
                print("Number of Modulo Divisions for the value of k:", gcd_count(fib[k-1], fib[k-2]))
                print("Time Taken to output result:", end - start)
                print("")

            elif option == 3:
                print("Task 3: ")
                m = int(input("Enter positive (m > 1) value for 'm': "))
                n = int(input("Enter positive (n > 1) value for 'n': "))
                x = gcd_middle(m, n)[0]
                y = gcd_middle(m, n)[1]
                z = sieve(m)
                z2 = sieve(n)
                print("Sieve's Algorithm based on 'm':", z)
                print("Sieve's Algorithm based on 'n':", z2)
                print("Prime factors for 'm':", primefactors(m))
                print("Prime factors for 'n':", primefactors(n))
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
                x = []
                y = []
                x1 = []
                y1 = []
                print("-> LOADING GRAPH <-")
                for i in range(1, 200):
                    n = i
                    n2 = i
                    gcd = gcd_avg(n)
                    ica = ica_avg(n2)
                    x.append(n)
                    y.append(gcd)
                    x1.append(n2)
                    y1.append(ica)

                print("-> GRAPH LOADED <-")
                print("Plotted Points Listed Below: ")
                print("Euclid Average's:", y)
                print("Consecutive Integer Average's:", y1)

                plt.plot(x, y, 'bs')
                plt.plot(x1, y1, 'ro')
                plt.axis([0, 100, 0, 10])
                blue_patch = mpatches.Patch(color='blue', label="Euclid's Algorithm")
                red_patch = mpatches.Patch(color='red', label='Consecutive Integer Algorithm')
                plt.legend(handles=[red_patch, blue_patch])
                plt.title("Average-Case Efficiencies Graph")
                plt.xlabel('Input Size "n"')
                plt.ylabel('Average Mod/Divisions')
                plt.show()

                x.clear()
                y.clear()
                print("")
                print("-> LOADING GRAPH <-")
                for i in range(1, 500):
                    n = i
                    gcd = gcd_avg(n)
                    x.append(n)
                    y.append(gcd)

                print("-> GRAPH LOADED <-")
                print("Input Size 'n':", x)
                print("Euclid Average's:", y)
                plt.plot(x, y, 'bs')
                plt.axis([0, 500, 0, 7])
                blue_patch = mpatches.Patch(color='blue', label="Euclid's Algorithm")
                plt.title("Average-Case Euclid's Efficiencies Graph")
                plt.xlabel('Input Size "n"')
                plt.ylabel('Average Mod')
                plt.show()

                x.clear()
                y.clear()
                print("")
                print("-> LOADING GRAPH <-")
                for i in range(1, 500):
                    n = i
                    gcd = ica_avg(n)
                    x.append(n)
                    y.append(gcd)

                print("-> GRAPH LOADED <-")
                print("Input Size 'n':", x)
                print("Consecutive Integer Average's:", y)
                plt.plot(x, y, 'bs')
                plt.axis([0, 500, 0, 500])
                red_patch = mpatches.Patch(color='red', label='Consecutive Integer Algorithm')
                plt.title("Average-Case Consecutive integer Efficiencies Graph")
                plt.xlabel('Input Size "n"')
                plt.ylabel('Average Divisions')
                plt.show()

                print("")

            elif option == 2:
                print("Task 2: ")
                x = []
                y = []
                y1 = []
                k = 1000
                fib = fib_seq(k)
                total_Mod = 0
                print("Plotted Points Listed Below:")
                for i in range(0, k-2):
                    start = time.time()
                    total_Mod = gcd_count(fib[i+1], fib[i])
                    end = time.time()
                    x.append(fib[i+1])
                    y.append(total_Mod)
                    y1.append((end-start))

                #  First Graph
                print("Modulo Division Plot Points:")
                print("Value's of 'm':", x)
                print("Number of Modulo Divisions:", y)
                plt.plot(x, y, 'bs')
                plt.axis([-500, 5000, 0, 20])
                plt.title("Worst-Case Efficiency For Euclid's Algorithm Graph")
                plt.xlabel('Value of "m"')
                plt.ylabel('Number of Modulo Divisions')
                plt.show()

                print("")

                #  Second Graph
                print("Time Based Plot Points:")
                print("Value's of 'm':", x)
                print("Time Taken:", y1)
                plt.plot(x, y1, 'ro')
                plt.axis([-500, 5000, 0, 9.1457672119140625e-06])
                plt.title("Worst-Case Efficiency For Euclid's Algorithm Graph")
                plt.xlabel('Value of "m"')
                plt.ylabel('Time Taken')
                plt.show()

                print("")

            elif option == 3:
                print("Task 3: ")
                size = 200
                x = []
                y = []

                print("-> LOADING GRAPH <-")
                for i in range(1, 1000):
                    m = random.randint(2, 4000)
                    n = random.randint(2, 4000)
                    x_temp = gcd_middle(m, n)[3]
                    y_temp = gcd_middle(m, n)[2]
                    x.append(x_temp)
                    y.append(y_temp)

                print("-> GRAPH LOADED <-")
                print("Max List Values:", x)
                print("Number of Comparisons:", y)
                plt.plot(x, y, 'ro')
                plt.axis([0, 12, 0, 31])
                plt.title("Common Factor Algorithm Complexity Graph")
                plt.xlabel('Max List Value')
                plt.ylabel('Number of Comparisons')
                plt.show()
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
