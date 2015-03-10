#The prime factors of 13195 are 5, 7, 13 and 29.

#What is the largest prime factor of the number 600851475143 ?

#Find Factors
	#divide by 2 to get the largest factor (LgPFactor)
	#loop from 2 to LgPFactor
	#divide number in question to see if % == 0
#If a factor (determined above)
	#Determine if factor is prime
		# if factor % 2 == 0
		# add to list (if list is < 3 in length continue, else terminate)

x = int(raw_input("Please enter a number: "))
halfLargeFactor = x/2
factorList = []
primeFactorList = []

for i in range(1, halfLargeFactor + 1):
	if x % i == 0:
		factorList.append(i)


for factor in factorList:
	isPrimeList = []
	for j in range(1, factor/2):
		if factor % 2 == 0:
			isPrimeList.append(j)
			if len(isPrimeList) > 2:
				break
	primeFactorList.append(factor)

print primeFactorList