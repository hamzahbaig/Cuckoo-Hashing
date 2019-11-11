class CuckooHashing:
	def __init__(self,s):
		self.size = s
		self.table1 =[]
		self.table2 = []
		for _ in range(self.size):
			self.table1.append("empty")
			self.table2.append("empty")

	def hash1(self,key):
		return key%11

	def hash2(self,key):
		return int((key/11)%11)

	def printTables(self):
		print("\n\t\t======== PRINTING TABLES ========\n")
		print("\n\t\tTABLE 1\t\t\t TABLE 2")
		print("\t\t-------\t\t\t -------\n")
		for x in range(self.size):
			print("\t\t" +str(x) + " -> " + str(self.table1[x]) + "\t\t" + str(x)+ " -> " + str(self.table2[x]) + "\n")

	def insert(self,key):
		index = self.hash1(key)
		index1 = self.hash2(key)

		# CASE 1: if the Table 1 slot is empty
		if (self.table1[index] == "empty"):
			self.table1[index] = key
			return

		# CASE 2: if the Table 1 slot is not empty but Table 2 slot is empty
		elif (self.table1[index] != "empty"):
			# storing confliciting value
			conflictingElement = self.table1[index]
			if(self.table2[index1] == "empty"):
				# moving conflicting value to next table
				conflictingElementIndex = self.hash2(conflictingElement)
				self.table2[conflictingElementIndex] = conflictingElement
				# storing the new value
				self.table1[index] = key


def menu():
	print("\tPress 1: To Search key")
	print("\tPress 2: To Insert key")
	print("\tPress 3: To Delete key")
	print("\tPress 4: To Pprint Tables")
	print("\tPress 5: To Exit")

def main():
	instance = CuckooHashing(11)
	menu()
	instance.insert(500)
	instance.insert(20)
	instance.insert(36)
	instance.insert(75)
	instance.insert(100)
	instance.insert(3)
	instance.insert(105)
	instance.insert(67)
	instance.insert(53)
	instance.printTables()

main()