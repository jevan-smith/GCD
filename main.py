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

def fib_seq(k):
	"""
	This function computes fibonacci sequence
	Input: one non-negative number
	Output: returns fibonacci sequence in an array
	"""
	array = [0, 1]
	for i in range(0, k):
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
    		print("[1] Task 1")
    		print("[2] Task 2")
    		print("[3] Task 3")
    		print("[4] Go Back")
    		print("[5] Exit")

    		option = int(input("Option: "))
    		print("")

    		if option == 1:
    			n = int(input("Enter positive value for 'n': "))
    			print("Average number of Modulo Divisions GCD is:", gcd_avg(n))
    			print("Average number of Divisions GCD is:", ica_avg(n))
    			print("")
    		elif option == 2:
    			k = int(input("Enter positive value for 'k': "))
    			fib = fib_seq(k)
    			print("Fibonacci Sequence:", fib)
    			total_Mod = 0
    			for i in range(k):
    				total_Mod += gcd_count(fib[i+1], fib[i])
    			print("Total number of Modulo Divisions is:", total_Mod)
    			print("")
    		elif option == 3:
    			print("task3\n")
    		elif option == 4:
    			break
    		elif option == 5:
    			print("Goodbye!\n")
    			exit()
    		else:
    			print("Invalid input, try again.\n")
    elif option == 2:
        print("Test2\n")
    elif option == 3:
        print("Goodbye!\n")
        exit()
    else:
        print("Invalid input, try again.\n")
""" 
End of Main program loop
"""
