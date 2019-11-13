class CuckooHashing:
	def __init__(self,s):
		self.size = s
		self.table1 =[]
		self.table2 = []
		for _ in range(self.size):
			self.table1.append("empty")
			self.table2.append("empty")

	# HASH FUNCTION 1
	def hash1(self,key):
		return key%self.size

	# HASH FUCNTION 2
	def hash2(self,key):
		return int((key/self.size)%self.size)

	# PRINT TABLES
	def printTables(self):
		print("\n\t\t======== PRINTING TABLES ========\n")
		print("\n\t\tTABLE 1\t\t\t TABLE 2")
		print("\t\t-------\t\t\t -------\n")
		for x in range(self.size):
			print("\t\t" +str(x) + " -> " + str(self.table1[x]) + "\t\t" + str(x)+ " -> " + str(self.table2[x]) + "\n")

	# SEARCH ELEMENT IN TABLE
	def search(self,key):
		index = self.hash1(key)
		index1 = self.hash2(key)

		# CASE 1: Element is present in table 1
		if (self.table1[index] == key):
			print("\n" + str(key) + " is present in Table1[" +str(index)+"]")
			return 1,index

		# CASE 2: Element is present in table 2
		if (self.table2[index1] == key):
			print("\n" + str(key) + " is present in Table2[" +str(index1)+"]")
			return 2,index1

		# CASE 3: Element is not present in either Tables
		print("\nElement " + str(key) + " is not present in either Tables")
		return -1,"empty"

	# DELETE ELEMENT IN TABLE
	def delete(self,key):
		tableNo, index = self.search(key)

		# CASE 1: Element not found
		if (tableNo == -1 and index == "empty"):
			return

		# CASE 2: Deleting Element from table 1
		if (tableNo == 1):
			self.table1[index] = "empty"
			print("\nElement " + str(key) + " deleted successfully!")
			return

		# CASE 3: Deleting Element from table 3
		if (tableNo == 2):
			self.table2[index] = "empty"
			print("\nElement " + str(key) + " deleted successfully!")
			return

	def insert(self,originalKey,key,table):
		# Intializing Variables
		if (table == "table1"):
			insertingTable = self.table1
			index = self.hash1(key)
			nextTable = "table2"
		elif (table == "table2"):
			insertingTable = self.table2
			index = self.hash2(key)
			nextTable = "table1"

		if originalKey == key:
			print("loop Detected")

		# CASE 1: Arg Table is empty then insert
		if (insertingTable[index] == "empty"):
			insertingTable[index] = key
			print(key,"inserted",originalKey)
			return


		# CASE 2: Arg Table is not empty insert new key and call insert() again on conflictingKey
		if (insertingTable[index] != "empty"):
			conflicitingKey = insertingTable[index]
			print(key,conflicitingKey,originalKey)
			insertingTable[index] = key
			self.insert(key,conflicitingKey,nextTable)
			return






def menu():
	print("\n\t\t======== MENU ========")
	print("\n\t\tPress 1: To Search key")
	print("\t\tPress 2: To Insert key")
	print("\t\tPress 3: To Delete key")
	print("\t\tPress 4: To Print Tables")
	print("\t\tPress 5: To Exit")

def main():
	instance = CuckooHashing(11)
	while(1):
		menu()
		option = input("\n\t\tPlease enter your option: ")

		# CASE 1: Search an Element in tables
		if option == "1":
			key = input("\nPlease enter the key that you wish to search: ")
			instance.search(int(key))

		# CASE 2: Insert an Element in tables
		elif option == "2":
			while(1):
				key = input("\nPlease enter the key(s) that you wish to insert (q for exit): ")
				if(key == "q"):
					break
				else:
					instance.insert(-1,int(key),"table1")

		# CASE 3: Delete an Element in tables
		elif option == "3":
			key = input("\nPlease enter the key that you wish to delete: ")
			instance.delete(int(key))

		# CASE 4: Print Tables
		elif option == "4":
			instance.printTables()

		# CASE 5: Exit
		elif option == "5":
			print("Exiting Cuckoo Hashing..")
			break

main()