# PYTHON program to find sum of all
# divisors of a natural number
import math

# Function to calculate sum of all proper
# divisors num --> given natural number
def sum_divisors(num) :
	if num == 0:
		return 0
	else:	# Final result of summation of divisors
		result =0
		i = 2
		while i<= (math.sqrt(num)) :

			# if 'i' is divisor of 'num'
			if (num % i == 0) :

				# if both divisors are same then
				# add it only once else add both
				if (i == (num / i)) :
					result = result + i;
				else :
					result = result + (i + num/i);
			i = i + 1

		# Add 1 to the result as 1 is also
		# a divisor
	return round(result + 1);

print(sum_divisors(0))
# 0
print(sum_divisors(3)) # Should sum of 1
# 1
print(sum_divisors(36)) # Should sum of 1+2+3+4+6+9+12+18
# 55
print(sum_divisors(102)) # Should be sum of 2+3+6+17+34+51
# 114
