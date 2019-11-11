class CuckooHashing:
	def __init__(self,s):
		self.size = s
		self.table1 =[]
		self.table2 = []
		for _ in range(self.size):
			table1.append(-1)
			table2.append(-1)
			
	def hash1(self,key):
		return key%11

	def hash2(self,key):
		return (key/11)%11

	# def insert(self,key):


def main():
	instance = CuckooHashing(11)
	print(instance.hash1(21))

main()