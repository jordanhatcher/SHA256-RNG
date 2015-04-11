import hashlib
import math

class Rng:
	def __init__(self,seed):
		self.state = seed.encode('utf-8')

	def init_rng(self,seed):
		self.state = seed.encode('utf-8')

	def random_int(self, lower_end=0, upper_end=100):
		range_length = upper_end - lower_end

		if(range_length != 1):
			num_digits = math.ceil(math.log(range_length,16)) #number of hex digits to generate


			valid = False
			random_int_string = ''

			while not valid: #loop until random number is in a valid range
				for digit in range(0,num_digits):
					hasher = hashlib.sha256()
					hasher.update(self.state)
					state = hasher.hexdigest()
					self.state = state.encode('utf-8') #use the hash digest as the next state
					random_int_string += state[:1] #take the first digit to use for generating the random number
				
				random_int_val = int(random_int_string,16) #convert the string to an integer value

				if(random_int_val < range_length): #is number in range?
					valid = True
				else:
					random_int_string = ''

			random_int_val = random_int_val + lower_end #adjust number to fit custom range
			return random_int_val
		else:
			return lower_end

	def random_float(self, lower_end=0, upper_end=1):
		float_str = '0.'

		for digit in range(17): #generate 17 random digits
			float_str += str(self.random_int(0,10))
		float_val = float(float_str) #get a number between 0 and 1
		
		range_length = upper_end - lower_end
		float_val = (float_val*range_length) + lower_end #adjust the number to fit custom range
		return float_val

def main():
	r = Rng("Yeah amazing random text :p") #seed the generator
	for i in range(10):
		print(r.random_float())

if __name__ == '__main__':
	main()

