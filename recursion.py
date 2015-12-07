__author__ = 'Patrick Abejar'


def fibonacci(position):
    """This function recursively calculates the Fibonacci number at the pos-
    ition provided as a parameter. It does so by looking at the next two pos-
    itions (position-1 and position-2) and adding them together, just as the
    Fibonacci sequence does to calculate the proceeding number. As shown in
    the sample Fibonacci sequence segment above position 0 has the number 1
    and position 1 has the number 1, which are encoded in this function as the
    base cases. Two positions are sufficient enough for the base cases as Fib-
    onacci sequence only examines two positions at a time to get the next pos-
    ition.

    :param position: Input is used to determine what number to return in the Fib-
    onacci sequence.

    :return: Returns the number in the Fibonacci sequence position requested.
    """

    #  Position: 0  1  2  3  4  5  6   7   8   9  10  11   12
    #  Number:   0  1  1  2  3  5  8  13  21  34  55  89  144

    if position == 1:
        return 1
    if position == 0:
        return 0

    return fibonacci(position-2) + fibonacci(position-1)


def gcd(num1, num2):
    """This uses Euclid's algorithm to determine what the greatest common de-
    nominator is between num1 and num2. According to that algorithm, we need
    only to divide num2 into num1 and then take the gcd of num2 and the re-
    mainder of the stated division operation. As one goes through numerous
    iterations of division, the numbers become increasingly smaller. This ev-
    entually will reach 0, in which the GCD of any number and 0 is the non-
    zero number. This will be used as a base case to stop the recursion. After
    many recursions we have a simplified (meaning smaller numbers) and equi-
    valent statement that yields the intended GCD of the previous two numbers.

    :param num1: will determine gcd of this number and num2
    :param num2: will determine gcd of this number and num1
    :return: returns the gcd of num1 and num2
    """

    # Sample: (42, 12) = (12, 6) = (6, 0)
    # Sample: (63, 14) = (14, 7) = (7, 0)

    if num2 == 0:
        return num1

    return gcd(num2, (num1 % num2))


def compareTo(s1, s2):
    """Based on ASCII assigned numbers, this function will determine if strings
    are equivalent to each other, lesser, or greater than the other. If a str-
    ing is equivalent to another string up until one point where one string
    terminates, that shorter string is considered lesser than the longer str-
    ing, consistent with ordering words and letters alphabetically.

    :param s1: a string to compare with s2
    :param s2: a string to comapre with s1
    :return: -1 if s1 < s2, 1 if s1 > s2, 0 if s1 and s2 are equivalent
    """

    # Will retrieve the next character (length of 1) to compare for s1 & s2
    next_char1 = s1[1:2]
    next_char2 = s2[1:2]

    # BASE CASES:
    # Checking that the strings have not terminated yet
    if len(next_char1) == 0 and len(next_char2) != 0:
        return -1
    elif len(next_char1) != 0 and len(next_char2) == 0:
        return 1
    elif len(next_char1) == 0 and len(next_char2) == 0:
        return 0

    # Uses ASCII values to compare which character currently being observed is
    # lesser or greater. This is consistent with the return convention listed
    # above.
    if ord(next_char1) < ord(next_char2):
        return -1
    elif ord(next_char1) > ord(next_char2):
        return 1

    # If characters present the same value, then the rest of the string is
    # looked at.
    return compareTo(s1[1:], s2[1:])


def main():
    """Implements the three above recursive functions into one menu."""

    print "Choose a recursive function you wish to run:\n" \
          "1 for FIBONACCI\n" \
          "2 for GCD\n" \
          "3 for STRING COMPARE\n"
    try:
        while True:
            decision = int(raw_input("\nYour choice: "))

            if decision == 1:
                pos = int(raw_input("What position in the Fibonacci Sequence do you want? "))
                print "Answer: ", fibonacci(pos)
            elif decision == 2:
                n1 = int(raw_input("Number 1: "))
                n2 = int(raw_input("Number 2: "))
                print "Answer: ", gcd(n1, n2)
            elif decision == 3:
                str1 = raw_input("String 1: ")
                str2 = raw_input("String 2: ")
                print "Response: ", compareTo(str1, str2)
            elif decision < 1 or decision > 3:
                print "Please enter 1, 2, or 3."

    except ValueError:
        print "Please enter a valid value."


if __name__ == "__main__":
    main()
