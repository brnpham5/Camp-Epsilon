import linecache
import Choice

class DataFile_Handler():
	CurrentDataFile = "\0"
	NextAct = 0
	CurrentLine = -1

	def __init__(self, filepath):
		self.newAct(filepath)

	def newAct(self, filepath):
		self.CurrentDataFile = filepath
		self.NextAct = 0
		self.CurrentLine = 0
		
	def getCurrentAct(self):
		return self.CurrentDataFile
		
	def keyword_Handler(self, lineNum):
		if(int(lineNum) > -1):
			self.CurrentLine = int(lineNum)
			
		currLine = linecache.getline(self.CurrentDataFile, self.CurrentLine).split("_")
		
		if(currLine[0] == "DSC"):
			return self.getDSC()
		elif(currLine[0] == "NPC"):
			return self.getNPC()
		elif(currLine[0] == "CHC"):
			return self.getCHC()
		elif(currLine[0] == "SFX"):
			return self.updateSFX()
		elif(currLine[0] == "MUS"):
			return self.updateMUS()
		elif(currLine[0] == "BKG"):
			return self.updateBKG()
		elif(currLine[0] == "ENA"):
			return self.endAct(currLine[1])
		elif(currLine[0] == "ENC"):
			self.updateLine()
		elif(currLine[0] == "BRN"):
			return self.updateNextAct()
		elif(currLine[0] == "LIK"):
			return self.updateLike()
		elif(currLine[0] == "JMP"):
			return self.jumpToLine(currLine[1])
		else:
			self.updateLine()
	
	def jumpToLine(self, lineNum):
		self.CurrentLine = lineNum
		return self.keyword_Handler(self.CurrentLine)
	
	def getDSC(self):
			DSC = (linecache.getline(self.CurrentDataFile, self.CurrentLine)).split("_")
			self.updateLine()
			return DSC
		
	def getNPC(self):
			NPC = (linecache.getline(self.CurrentDataFile, self.CurrentLine)).split("_")
			self.updateLine()
			return NPC
		
	def getCHC(self):
		parsed1 = (linecache.getline(self.CurrentDataFile, self.CurrentLine)).split("_")
		self.updateLine()
		parsed2 = (linecache.getline(self.CurrentDataFile, self.CurrentLine)).split("_")
		self.updateLine()
		choices = Choice.Choice()
		choices.setChoice(parsed1, parsed2)
		return choices
		
	def updateSFX(self):
		parsed = (linecache.getline(self.CurrentDataFile, self.CurrentLine)).split("_")
		self.updateLine()
		return parsed
		
		
	def updateMUS(self):
		parsed = (linecache.getline(self.CurrentDataFile, self.CurrentLine)).split("_")
		self.updateLine()
		return parsed
		
	def updateBKG(self):
		parsed = (linecache.getline(self.CurrentDataFile, self.CurrentLine)).split("_")
		self.updateLine()
		return parsed
		
	def updateLike(self):
		parsed = (linecache.getline(self.CurrentDataFile, self.CurrentLine)).split("_")
		self.updateLine()
		#callthe method to update player Like value
		
	def updateNextAct(self):
		parsed = (linecache.getline(self.CurrentDataFile, self.CurrentLine)).split("_")
		self.NextAct = self.NextAct + (int(parsed[1]))
		self.updateLine()
	
	def endAct(self, version):
		if(CurrentDataFile == "ACT1.txt"):
			if(self.NextAct >= 0):
				if(version == 0):
					self.newAct("ACT2H1.txt")
				else:
					self.newAct("ACT2H2.txt")
			else:
				if(version == 0):
					self.newAct("ACT2S1.txt")
				else:
					self.newAct("ACT2S2.txt")
					
		elif(CurrentDataFile == "ACT2S1.txt"):
			if(self.NextAct >= 0):
				self.newAct("ACT3S2.txt")
			else:
				self.newAct("ACT3S3.txt")
		elif(CurrentDataFile == "ACT2S2.txt"):
			if(self.NextAct >= 0):
				self.newAct("ACT3S1.txt")
			else:
				self.newAct("ACT3S3.txt")
		elif(CurrentDataFile == "ACT2H1.txt"):
			if(self.NextAct >= 0):
				self.newAct("ACT3H2.txt")
			else:
				self.newAct("ACT3H3.txt")
		elif(CurrentDataFile == "ACT2H2.txt"):
			if(self.NextAct >= 0):
				self.newAct("ACT3H1.txt")
			else:
				self.newAct("ACT3H3.txt")
		
	def updateLine(self):
		self.CurrentLine = self.CurrentLine + 1
	
	

