#A palindromic number reads the same both ways. The largest palindrome made from the product of two 2-digit numbers is 9009 = 91 * 99
#Find the largest palindrome made from the product of two 3-digit numbers

#NOTES
#The smallest possible product would be 10,000, and the largest possible product would be 998,001 (5 or 6 digits)

firstFactor = input('What is the first factor: ')
secondFactor = input('What is the second factor: ')
palindromeList = []

for firstFactor in range(100, 999):
	for secondFactor in range(firstFactor, 999):
		possiblePalindrome = firstFactor * secondFactor
		if len(str(possiblePalindrome)) % 2 == 0:
			if str(possiblePalindrome)[0] == str(possiblePalindrome)[-1] and str(possiblePalindrome)[1] == str(possiblePalindrome)[-2] and str(possiblePalindrome)[2] == str(possiblePalindrome)[-3]:
				palindromeList.append(possiblePalindrome)
		if len(str(possiblePalindrome)) % 2 != 0:
			if str(possiblePalindrome)[0] == str(possiblePalindrome)[-1] and str(possiblePalindrome)[1] == str(possiblePalindrome)[2]:
				palindromeList.append(possiblePalindrome)



#print palindromeList
print 'The largest product of two 3-digit numbers that is a palindrome is: %d' % max(palindromeList)

