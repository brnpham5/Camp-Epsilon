import linecache
#import Choice

class DataFile_Handler():
	CurrentDataFile = ""
	NextAct = 0
	CurrentLine = -1

	def __init__(self, filepath):
		self.newAct(filepath)

	def newAct(self, filepath):
		self.CurrentDataFile = filepath
		self.NextAct = 0
		self.CurrentLine = 0
		
	def getCurrentLine(self):
		return self.CurrentLine
	
	def getCurrentAct(self):
		return self.CurrentDataFile
		
	def keyword_Handler(self):	
		currLine = linecache.getline(self.CurrentDataFile, self.CurrentLine).split("_")
		return currLine
	
	def setLineNumber(self, lineNum):
		self.CurrentLine = lineNum
	
	#deprecated due to change in design
	#def getDSC(self):
	#		DSC = (linecache.getline(self.CurrentDataFile, self.CurrentLine)).split("_")
	#		self.updateLine()
	#		return DSC
	
	#deprecated due to change in design	
	#def getNPC(self):
	#		NPC = (linecache.getline(self.CurrentDataFile, self.CurrentLine)).split("_")
	#		self.updateLine()
	#		return NPC
	
	#altered due to design change
	def getCHC(self):
	#	parsed1 = (linecache.getline(self.CurrentDataFile, self.CurrentLine)).split("_")
	#	self.updateLine()
	#	parsed2 = (linecache.getline(self.CurrentDataFile, self.CurrentLine)).split("_")
	#	self.updateLine()
	#	choices = Choice.Choice()
	#	choices.setChoice(parsed1, parsed2)
	#	return choices
		parsed = (linecache.getline(self.CurrentDataFile, self.CurrentLine)).split("_")
		self.updateLine()
		parsed.append((linecache.getline(self.CurrentDataFile, self.CurrentLine)).split("_"))
		self.updateLine()
		return parsed

	#deprecated due to change in design	
	#def updateSFX(self):
	#	parsed = (linecache.getline(self.CurrentDataFile, self.CurrentLine)).split("_")
	#	self.updateLine()
	#	return parsed
		
	#deprecated due to change in design	
	#def updateMUS(self):
	#	parsed = (linecache.getline(self.CurrentDataFile, self.CurrentLine)).split("_")
	#	self.updateLine()
	#	return parsed
	
	#deprecated due to change in design
	#def updateBKG(self):
	#	parsed = (linecache.getline(self.CurrentDataFile, self.CurrentLine)).split("_")
	#	self.updateLine()
	#	return parsed
		
	#deprecated due to change in design
	#def updateLike(self):
	#	parsed = (linecache.getline(self.CurrentDataFile, self.CurrentLine)).split("_")
	#	self.updateLine()
	#	#call the method to update player Like value
		
	def updateNextAct(self, changeInValue):
		if(changeInValue == 0):
			self.NextAct = self.NextAct - 1
		else:
			self.NextAct = self.NextAct + 1
		self.updateLine()
	
	def endAct(self, version):
		#This is the code for the protype
		#Comment out after remaing acts are written
		if(CurrentDataFile == "ACT1.txt"):
			self.newAct("ComingSoon.txt")

		#This is the process for changing acts after they're written
		#Remove comments once prototyping is complete
		#if(CurrentDataFile == "ACT1.txt"):
		#	if(self.NextAct >= 0):
		#		if(version == 0):
		#			self.newAct("ACT2H1.txt")
		#		else:
		#			self.newAct("ACT2H2.txt")
		#	else:
		#		if(version == 0):
		#			self.newAct("ACT2S1.txt")
		#		else:
		#			self.newAct("ACT2S2.txt")
		#			
		#elif(CurrentDataFile == "ACT2S1.txt"):
		#	if(self.NextAct >= 0):
		#		self.newAct("ACT3S2.txt")
		#	else:
		#		self.newAct("ACT3S3.txt")
		#elif(CurrentDataFile == "ACT2S2.txt"):
		#	if(self.NextAct >= 0):
		#		self.newAct("ACT3S1.txt")
		#	else:
		#		self.newAct("ACT3S3.txt")
		#elif(CurrentDataFile == "ACT2H1.txt"):
		#	if(self.NextAct >= 0):
		#		self.newAct("ACT3H2.txt")
		#	else:
		#		self.newAct("ACT3H3.txt")
		#elif(CurrentDataFile == "ACT2H2.txt"):
		#	if(self.NextAct >= 0):
		#		self.newAct("ACT3H1.txt")
		#	else:
		#		self.newAct("ACT3H3.txt")
		#
	def updateLine(self):
		self.CurrentLine = self.CurrentLine + 1
	
	

