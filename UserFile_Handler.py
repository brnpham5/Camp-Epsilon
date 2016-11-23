import os

class UserFile_Handler():
	CurrentDataFile = ""
	PlayerName = ""
	Likability = 0
	
	def __init__(self, name):
		self.setDataFile("ACT1.txt")
		self.setPlayerName(name)
		self.setLike(0)
		
	def updateUser(self, fileData):
		self.setDataFile(fileData[1])
		self.setPlayerName(fileData[0])
		self.setLike(int(fileData[2]))
		
	def setDataFile(self, newFile):
		self.CurrentDataFile = newFile
	
	def getDataFile(self):
		return self.CurrentDataFile
	
	def setPlayerName(self, name):
		self.PlayerName = name
		
	def getPlayerName(self):
		return self.PlayerName
		
	def getFileNames(self):
		fd = open("SaveFile.txt")
		allFiles = []
		for line in fd:
			currLine = line.split("_")
			allFiles.append(currLine[0])
			
		return allFiles
		
	def setLike(self, num):
		self.Likability = num
		
	def updateLike(self, changeInValue):
		if(changeInValue == 0):
			self.Likability = self.Likability - 1
		else:
			self.Likability = self.Likability + 1
		
	def getLike(self):
		return self.Likability
		
	def loadFile(self, fileName):
		if(self.fileIsEmpty("SaveFile.txt")):
			return False
			
		fd = open("SaveFile.txt")
		for line in fd:
			currLine = line.split("_")
			if(currLine[0] == fileName):
				self.updateUser(currLine)
				fd.close()
				return True
		
		fd.close()		
		return False
		
	def saveFile(self):
		if(self.fileIsEmpty("SaveFile.txt")):
			fd = open("SaveFile.txt", 'w')
			fd.write(self.getPlayerName() + "_" + self.getDataFile() + "_" + str(self.getLike()) + "\n")
			return True	
			
		fd = open("SaveFile.txt", 'r')
		files = fd.readlines()
		fd.close()
		
		fd = open("SaveFile.txt", 'w')
		result = False
		for line in files:
			parsed = line.split("_")
			if(parsed[0] == self.getPlayerName()):
				fd.write(self.getPlayerName() + "_" + self.getDataFile() + "_" + str(self.getLike()) + "\n")
				result = True
			else: 
				fd.write(line)
		
		if(result != True):
			fd.write(self.getPlayerName() + "_" + self.getDataFile() + "_" + str(self.getLike()) + "\n")
				
			
		fd.close()
		return True
		
	def fileIsEmpty(self, filename):
		return os.stat(filename).st_size == 0