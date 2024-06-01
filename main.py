import pygame, sys, random

moving = False


# each biome has a random chance of selection up to Heath
class Square:

	def __init__(self, image, x, y, biome):
		self.squareRect = pygame.Rect(x, y, squareSize, squareSize)
		self.player = ""
		self.image = image
		self.biome = biome
		self.obstacal = self.obstacle()
		self.fog = False
		self.inView = False
	# self.building = buildingSelector()

	def obstacle(self):
		if self.image == "pond":
			return None
		elif self.biome == "mountainField" or self.biome == "mountainSand":
			return mountain
		else:
			return None

class Castle:
	def __init__(self, x, y, xVal, yVal):
		self.rect = (x,y)
		self.squareRect = pygame.Rect(xVal, yVal, squareSize, squareSize)
class Characters:

	def __init__(self, grid, pos, image, health):
		self.grid = grid
		self.pos = pos
		self.image = image
		self.rect = game.imageMap[grid][pos].squareRect
		self.health = health
		# self.visLat = visLat
		# self.visLong = visLong
		self.moveableTiles = self.possMovement()

	def possMovement(self):
		if self.grid == 0 and self.pos == 0:
			return [(0, 1), (0, 5), (0, 6)]
		elif self.grid == 4 and self.pos == 4:
			return [(4, 3), (4, 8), (4, 9)]
		elif self.grid == 20 and self.pos == 20:
			return [(20, 15), (20, 16), (20, 21)]
		elif self.grid == 24 and self.pos == 24:
			return [(24, 23), (24, 19), (24, 18)]
		# corners are above
		elif (self.grid == 5 or self.grid == 10 or self.grid == 15
			  or self.grid == 20) and self.pos == 0:
			return [(self.grid, 1), (self.grid, 6), (self.grid, 5),
					(self.grid - 5, 20), (self.grid - 5, 21)]
		elif (self.grid == 0 or self.grid == 5 or self.grid == 10
			  or self.grid == 15) and self.pos == 20:
			return [(self.grid, 15), (self.grid, 16), (self.grid, 21),
					(self.grid + 5, 0), (self.grid + 5, 1)]
		elif (self.grid == 4 or self.grid == 9 or self.grid == 14
			  or self.grid == 19) and self.pos == 24:
			return [(self.grid, 18), (self.grid, 19), (self.grid, 23),
					(self.grid + 5, 3), (self.grid + 5, 4)]
		elif (self.grid == 9 or self.grid == 14 or self.grid == 19
			  or self.grid == 24) and self.pos == 4:
			return [(self.grid, 3), (self.grid, 8), (self.grid, 9),
					(self.grid - 5, 23), (self.grid - 5, 24)]
		elif (self.grid == 9 or self.grid == 4 or self.grid == 14 or self.grid == 24 or self.grid == 19) and (self.pos == 9 or self.pos == 14 or self.pos == 19):
			return [(self.grid, self.pos +5), (self.grid, self.pos - 5), (self.grid, self.pos -1), (self.grid, self.pos + 4), (self.grid, self.pos - 6)]
		elif (self.grid == 9 or self.grid == 4 or self.grid == 14 or self.grid == 19) and self.pos == 24:
			return [(self.grid, self.pos -1), (self.grid, self.pos -5), (self.grid, self.pos -6), (self.grid +5, 4), (self.grid +5, 3)]
		elif (self.grid == 1 or self.grid == 2
			  or self.grid == 3) and (self.pos == 1 or self.pos == 2 or self.pos == 3):
			return [(self.grid, self.pos + 1), (self.grid, self.pos - 1),
					(self.grid, self.pos + 5), (self.grid, self.pos + 6),
					(self.grid, self.pos + 4)]
		elif (self.grid == 1 or self.grid == 2
			  or self.grid == 3) and self.pos == 0:
			return [(self.grid, 1), (self.grid, 5), (self.grid, 6), (self.grid - 1, 4), (self.grid-1, 9)]
		elif (self.grid == 20 or self.grid == 21 or self.grid == 22 or self.grid == 23
			  or self.grid == 24) and (self.pos == 21 or self.pos == 22 or self.pos == 23):
			return [(self.grid, self.pos + 1), (self.grid, self.pos - 1),
					(self.grid, self.pos - 5), (self.grid, self.pos - 4),
					(self.grid, self.pos - 6)]
		elif (self.grid == 21 or self.grid == 22 or self.grid == 23
			  or self.grid == 20) and self.pos == 24:
			return [(self.grid, self.pos - 1), (self.grid+1, 20),
					(self.grid+1, 15), (self.grid, self.pos - 6),
					(self.grid, self.pos - 5)]
		elif (self.grid == 21 or self.grid == 22 or self.grid == 23
			  or self.grid == 24) and self.pos == 20:
			return [(self.grid, self.pos - 5), (self.grid - 1, 24),
					(self.grid - 1, 19), (self.grid, self.pos + 1),
					(self.grid, self.pos - 4)]
		elif self.grid == 24 and (self.pos == 9 or self.pos == 14 or self.pos == 19):
			return [(24, self.pos-1), (24, self.pos+5), (24, self.pos-5), (24, self.pos+4), (24, self.pos-6)]
		elif (self.grid == 0 or self.grid == 5 or self.grid == 10 or self.grid == 15 or self.grid == 20) and (self.pos == 5 or self.pos == 10 or self.pos == 15):
			return [(self.grid, self.pos + 1), (self.grid, self.pos -5), (self.grid, self.pos + 5), (self.grid, self.pos -4), (self.grid, self.pos + 6)]
		# add for bottom row as well and top row
		elif self.pos == 0:
			return [(self.grid, 1), (self.grid, 5), (self.grid, 6),
					(self.grid - 5, 20), (self.grid - 5, 21),
					(self.grid - 6, 24), (self.grid - 1, 4),
					(self.grid - 1, 9)]
		elif self.pos == 4:
			return [(self.grid, 3), (self.grid, 8), (self.grid, 9),
					(self.grid - 5, 23), (self.grid - 5, 24),
					(self.grid - 4, 20), (self.grid + 1, 0),
					(self.grid + 1, 5)]
		elif self.pos == 20:
			return [(self.grid, 15), (self.grid, 21), (self.grid, 16),
					(self.grid + 5, 0), (self.grid + 5, 1),
					(self.grid - 1, 24), (self.grid - 1, 19),
					(self.grid + 4, 4)]
		elif self.pos == 24:
			return [(self.grid, 19), (self.grid, 18), (self.grid, 23),
					(self.grid + 1, 20), (self.grid + 1, 15),
					(self.grid + 5, 4), (self.grid + 5, 3), (self.grid + 6, 0)]
		elif self.pos == 5 or self.pos == 10 or self.pos == 15:
			return [(self.grid, self.pos + 1), (self.grid, self.pos + 5),
					(self.grid, self.pos - 5), (self.grid, self.pos - 4),
					(self.grid, self.pos + 6), (self.grid - 1, self.pos + 4),
					(self.grid - 1, self.pos - 1),
					(self.grid - 1, self.pos + 9)]
		elif self.pos == 1 or self.pos == 2 or self.pos == 3:
			return [(self.grid, self.pos + 1), (self.grid, self.pos - 1),(self.grid, self.pos + 5), (self.grid, self.pos + 6),(self.grid, self.pos + 4), (self.grid - 5, self.pos + 20),(self.grid - 5, self.pos + 21), (self.grid - 5, self.pos + 19)]
		elif self.pos == 9 or self.pos == 14 or self.pos == 19:
			return [(self.grid, self.pos + 5), (self.grid, self.pos + 4),
					(self.grid, self.pos - 1), (self.grid, self.pos - 5),
					(self.grid, self.pos - 6), (self.grid + 1, self.pos - 4),
					(self.grid + 1, self.pos + 1),
					(self.grid + 1, self.pos - 9)]
		elif self.pos == 21 or self.pos == 22 or self.pos == 23:
			return [(self.grid, self.pos + 1), (self.grid, self.pos - 1),
					(self.grid, self.pos - 5), (self.grid, self.pos - 4), (self.grid, self.pos - 6), (self.grid + 5, self.pos - 20), (self.grid + 5, self.pos - 19), (self.grid + 5, self.pos - 21)]
		else:
			return [(self.grid, self.pos + 1), (self.grid, self.pos - 1),
					(self.grid, self.pos + 5), (self.grid, self.pos - 5),
					(self.grid, self.pos + 6), (self.grid, self.pos + 4),
					(self.grid, self.pos - 4), (self.grid, self.pos - 6)]

	def randomMove(self):  
		global location #########################################################################################################################################################################################################################################################################################
		possibleMoves = self.possMovement()
		location = random.choice(possibleMoves)
		if game.imageMap[location[0]][location[1]].biome == "pond":
			self.image = redBoat
		else:
			self.image = knightRed
		self.grid = location[0]
		self.pos = location[1]

		print("Enemy moved to " + str(self.grid), str(self.pos))

class gameMap:

	def __init__(self):
		edgeBiomes = ["sand", "field", "mountainField", "mountainSand"]
		biomes = ["sand", "field", "pond", "mountainField", "mountainSand"]
		finalMap = []
		currentMap = []
		miniMap = []
		for i in range(25):
			if i >= 5 or i % 5 == 0 or (i + 1) % 5 == 0 or i >= 20:
				type = random.choice(edgeBiomes)
			else:
				type = random.choice(biomes)
			if type == "sand":
				currentMap.append(
					random.choices(biomes, weights=[50, 10, 5, 1, 1], k=25))
			elif type == "field":
				currentMap.append(
					random.choices(biomes, weights=[10, 50, 5, 1, 1], k=25))
			elif type == "mountainField":
				currentMap.append(
					random.choices(biomes, weights=[1, 20, 5, 2, 0], k=25))
			elif type == "mountainSand":
				currentMap.append(
					random.choices(biomes, weights=[20, 1, 5, 0, 2], k=25))
			else:
				currentMap.append(
					random.choices(biomes, weights=[1, 1, 4, 0, 0], k=25))
		currentMap = self.villageSpawn(currentMap)
		self.map = currentMap
		self.imageMap = self.drawMap()

	def villageSpawn(self, currentMap):
		villagePosLocations = [6, 7, 8, 11, 12, 13, 16, 17, 18]
		for i in range(0, 25):
			randomLocation = random.choice(villagePosLocations)
			if i == 0:
				if currentMap[i][randomLocation] == "sand" or currentMap[i][
					randomLocation] == "mountainSand":
					currentMap[i][randomLocation] = "sandVillageBlue"
				else:
					currentMap[i][randomLocation] = "fieldVillageBlue"
			elif i == 24:
				if currentMap[i][randomLocation] == "sand" or currentMap[i][
					randomLocation] == "mountainSand":
					currentMap[i][randomLocation] = "sandVillageRed"
				else:
					currentMap[i][randomLocation] = "fieldVillageRed"
			else:
				if currentMap[i][randomLocation] == "sand" or currentMap[i][
					randomLocation] == "mountainSand":
					currentMap[i][randomLocation] = "sandVillageOpen"

				else:
					currentMap[i][randomLocation] = "fieldVillageOpen"
		return currentMap

	def drawMap(self):
		global pondList
		global blueCastles
		mapping = self.map
		for i in range(0, len(mapping)):  # 25
			for t in range(0, len(mapping[i])):
				xVal = 0
				yVal = 0
				counter = 0
				posI = i
				posT = t
				while posI > 4:
					posI -= 5
					counter += 1
				xVal += posI * 300
				yVal += counter * 300
				counter = 0
				while posT > 4:
					posT -= 5
					counter += 1
				xVal += posT * 60
				yVal += counter * 60
				if mapping[i][t] == "pond":
					image = pondImage
					mapping[i][t] = Square(image, xVal, yVal, "pond")
					pondList.append((i,t))
				elif mapping[i][t] == "sand":
					image = sandImage
					roll = random.randint(0, 10)
					if roll == 1:
						mapping[i][t] = Square(image, xVal, yVal, "sandTree")
					else:
						mapping[i][t] = Square(image, xVal, yVal, "sand")
				elif mapping[i][t] == "sandVillageOpen":
					image = sandImage
					mapping[i][t] = Square(image, xVal, yVal,"sandVillageOpen")
				elif mapping[i][t] == "fieldVillageOpen":
					image = fieldImage
					mapping[i][t] = Square(image, xVal, yVal,"fieldVillageOpen")
				elif mapping[i][t] == "sandVillageRed":
					image = sandImage
					mapping[i][t] = Square(image, xVal, yVal, "sandVillageRed")
				elif mapping[i][t] == "fieldVillageRed":
					image = fieldImage
					mapping[i][t] = Square(image, xVal, yVal,"fieldVillageRed")
				elif mapping[i][t] == "sandVillageBlue":
					image = sandImage
					mapping[i][t] = Square(image, xVal, yVal, "sandVillageBlue")
					newCastle = Castle(i, t, xVal, yVal)
					blueCastles.append(newCastle)
				elif mapping[i][t] == "fieldVillageBlue":
					image = fieldImage
					mapping[i][t] = Square(image, xVal, yVal, "fieldVillageBlue")
					newCastle = Castle(i, t, xVal, yVal)
					blueCastles.append(newCastle)
				elif mapping[i][t] == "mountainField":
					image = fieldImage
					mapping[i][t] = Square(image, xVal, yVal, "mountainField")
				elif mapping[i][t] == "mountainSand":
					image = sandImage
					mapping[i][t] = Square(image, xVal, yVal, "mountainSand")
				elif mapping[i][t] == "field":
					image = fieldImage
					roll = random.randint(0, 10)
					if roll == 1:
						mapping[i][t] = Square(image, xVal, yVal, "fieldTree")
					else:
						mapping[i][t] = Square(image, xVal, yVal, "field")
		return mapping

	def drawElements(self):
		global drawList, castleList, blueKnightList, mineList, treeList, captureStuff, blueLocations, captureTree, redKnightList, pondList, pp
		treeList = []
		mineList = []
		pp = True
		for character in blueLocations:
			blueKnightList.append((character.grid, character.pos))
		for character in redLocations:
			redKnightList.append((character.grid,character.pos))

		for i in range(0, len(self.imageMap)):
			for t in range(0, len(self.imageMap[i])):
				screen.blit((self.imageMap[i][t]).image, (self.imageMap[i][t]).squareRect)  # error here
				if self.imageMap[i][t].biome == "mountainField" or self.imageMap[i][t].biome == "mountainSand":
					screen.blit(mountain, self.imageMap[i][t].squareRect)
					mineList.append((i, t))

				elif self.imageMap[i][t].biome == "sandVillageOpen" or self.imageMap[i][t].biome == "fieldVillageOpen":
					screen.blit(openVillage, self.imageMap[i][t].squareRect)
					castleList.append((i, t))

				elif self.imageMap[i][t].biome == "sandVillageBlue" or self.imageMap[i][t].biome == "fieldVillageBlue":
					screen.blit(blueVillage, self.imageMap[i][t].squareRect)
					if len(blueLocations) == 0 and round == 0:  #you have free will :)
						blueLocations.append(Characters(i, t, knightBlue, 15))
				elif self.imageMap[i][t].biome == "sandVillageRed" or self.imageMap[i][t].biome == "fieldVillageRed":
					screen.blit(redVillage, self.imageMap[i][t].squareRect)
					if round == 0 and len(redLocations) == 0:
						redLocations.append(Characters(i, t, knightRed, 15))

				elif self.imageMap[i][t].biome == "fieldTree":

					screen.blit(tree, self.imageMap[i][t].squareRect)
					treeList.append((i, t))
				elif self.imageMap[i][t].biome == "sandTree":
					screen.blit(cactus, self.imageMap[i][t].squareRect)
					treeList.append((i, t))
				elif self.imageMap[i][t].biome == "mineBlue":
					screen.blit(mountain, self.imageMap[i][t].squareRect)
					screen.blit(mineBlue, self.imageMap[i][t].squareRect)
				elif self.imageMap[i][t].biome == "lumberYardBlue":
					screen.blit(lumberBlue, self.imageMap[i][t].squareRect)
				if captureStuff:
					for j in range(len(mineList)):
						for k in range(len(blueKnightList)):
							if mineList[j] == blueKnightList[k]:
								self.imageMap[i][t].biome = "mineBlue"
								captureStuff = False
				if captureTree:
					for j in range(len(treeList)):
						for k in range(len(blueKnightList)):
							if treeList[j] == blueKnightList[k]:
								self.imageMap[i][t].biome = "lumberYardBlue"
								captureTree = False

		for character in blueLocations:
			if game.imageMap[character.grid][character.pos].biome == "pond":
				screen.blit(blueBoat, self.imageMap[character.grid][character.pos].squareRect)
			else:
				screen.blit(character.image, self.imageMap[character.grid][character.pos].squareRect)
			health = character.health
			if health != None and health > 0:
				try:
					text = valFont.render(str(health), True, (255,255,255))
					screen.blit(text, self.imageMap[character.grid][character.pos].squareRect)
				except:
					pass
			elif health < 0:
				blueLocations.remove(character)
			#############################################################
		for character in redLocations:
			screen.blit(character.image,self.imageMap[character.grid][character.pos].squareRect)
			health = character.health
			if health != None and health > 0:
				try:
					text = valFont.render(str(health), True, (255,255,255))
					screen.blit(text, self.imageMap[character.grid][character.pos].squareRect)
				except:
					pass

		for marker in range(0, len(drawList)):
			screen.blit(blueMarker, drawList[marker][0])
		captureStuff = False
		captureTree = False

	def moveLeft(self):
		global count_x
		if count_x > 0:
			for i in range(0, len(self.imageMap)):
				for t in range(0, len(self.imageMap[i])):
					self.imageMap[i][t].squareRect.x += 60
			count_x -= 1

	def moveRight(self):
		global count_x
		if count_x < 10:
			for i in range(0, len(self.imageMap)):
				for t in range(0, len(self.imageMap[i])):
					self.imageMap[i][t].squareRect.x -= 60
			count_x += 1

	def moveUp(self):
		global count_y
		if count_y > 0:
			for i in range(0, len(self.imageMap)):
				for t in range(0, len(self.imageMap[i])):
					self.imageMap[i][t].squareRect.y += 60
			count_y -= 1

	def moveDown(self):
		global count_y
		if count_y < 10:
			for i in range(0, len(self.imageMap)):
				for t in range(0, len(self.imageMap[i])):
					self.imageMap[i][t].squareRect.y -= 60
			count_y += 1


# map size ask
pygame.init()
pygame.font.init()
pygame.mixer.init()
squareSize =  60
mapHeight = 11212
screenView = squareSize * 15
screenSize = 100
# game window
screen = pygame.display.set_mode((screenView, screenView))

# time
clock = pygame.time.Clock()

# defining variables

biomes = ["sand", "field", "pond"]
fieldObjects = ["tree", "openVillage", "mountain"]
sandObjects = ["cactus", "openVillage", "mountain"]
buildings = ["lumberYardRed", "lumberYardBlue", "redMine", "blueMine","capturedVillageRed", "capturedVillageBlue"]
blueLocations = []
redLocations = []
round = 0
lastRound = round
displayBlue = False
mineList = []
treeList = []
captureStuff = False
captureTree = False
pondList = []
pp = True
# define our images
fieldImage = pygame.image.load("Images/grass.png")
pondImage = pygame.image.load("Images/pond.png")
sandImage = pygame.image.load("Images/sand.png")
mountain = pygame.image.load("Images/mountain.png")
openVillage = pygame.image.load("Images/openVillage.png")
tree = pygame.image.load("Images/tree.png")
cactus = pygame.image.load("Images/cactus.png")
redVillage = pygame.image.load("Images/redVillage.png")
blueVillage = pygame.image.load("Images/blueVillage.png")
knightBlue = pygame.image.load("Images/knightBlue.png")
knightRed = pygame.image.load("Images/knightRed.png")
archerBlue = pygame.image.load("Images/archerBlue.png")
archerRed = pygame.image.load("Images/archerRed.png")
blueBoat = pygame.image.load("Images/blueBoat.png")
#########################################################################################################
riderBlue = pygame.image.load("Images/riderBlue.png")
riderRed = pygame.image.load("Images/riderRed.png")
lumberBlue = pygame.image.load("Images/lumbarYardBlue.png")
lumberRed = pygame.image.load("Images/lumbarYardRed.png")
mineBlue = pygame.image.load("Images/blueMine.png")
mineRed = pygame.image.load("Images/redMine.png")
redMarker = pygame.image.load("Images/attackMarker.png")
blueMarker = pygame.image.load("Images/moveMarker.png")
redBoat = pygame.image.load("Images/redBoat.png")
#button = pygame.image.load("Images/button.png")
#button = pygame.transform.scale(button, (120, 60))
fieldImage = pygame.transform.scale(fieldImage, (60, 60))
sandImage = pygame.transform.scale(sandImage, (60, 60))
pondImage = pygame.transform.scale(pondImage, (60, 60))
openVillage = pygame.transform.scale(openVillage, (60, 60))
mountain = pygame.transform.scale(mountain, (60, 60))
tree = pygame.transform.scale(tree, (60, 60))
cactus = pygame.transform.scale(cactus, (60, 60))
redVillage = pygame.transform.scale(redVillage, (60, 60))
blueVillage = pygame.transform.scale(blueVillage, (60, 60))
knightBlue = pygame.transform.scale(knightBlue, (60, 60))
knightRed = pygame.transform.scale(knightRed, (60, 60))
archerBlue = pygame.transform.scale(archerBlue, (60, 60))
archerRed = pygame.transform.scale(archerRed, (60, 60))
riderBlue = pygame.transform.scale(riderBlue, (60, 60))
riderRed = pygame.transform.scale(riderRed, (60, 60))
lumberBlue = pygame.transform.scale(lumberBlue, (60, 60))
lumberRed = pygame.transform.scale(lumberRed, (60, 60))
mineBlue = pygame.transform.scale(mineBlue, (60, 60))
mineRed = pygame.transform.scale(mineRed, (60, 60))
redMarker = pygame.transform.scale(redMarker, (60, 60))
blueMarker = pygame.transform.scale(blueMarker, (60, 60))
blueBoat = pygame.transform.scale(blueBoat, (60,60))
redBoat = pygame.transform.scale(redBoat, (60,60))
sandMusic = pygame.mixer.Sound("Music/GerudoValley.mp3")
fieldMusic = pygame.mixer.Sound("Music/JourneyOfPraireKingOutlaw.mp3")
moveGrass = pygame.mixer.Sound("Music/grasseffect.mp3")
moveSand = pygame.mixer.Sound("Music/sandeffect.mp3")
moveWater = pygame.mixer.Sound("Music/waterSound.mp3")
waterTheme = pygame.mixer.Sound("Music/waterTheme.mp3")
channelOne = pygame.mixer.Channel(0)
channelTwo = pygame.mixer.Channel(1)
channelThree = pygame.mixer.Channel(2)
channelFour = pygame.mixer.Channel(3)
channelFive = pygame.mixer.Channel(4)
valFont = pygame.font.Font("valFont.ttf", 15)
channelOne.play(fieldMusic)
channelOne.pause()
channelTwo.play(sandMusic)
channelTwo.pause()
channelThree.play(waterTheme)
channelThree.pause()
# variables
characterList = [knightBlue, riderBlue, archerBlue]
blueWin = False
redWin = False
count_x = 0
count_y = 0
press_stat = False
drawList = []
castleList = []
blueKnightList = []
redKnightList = []
lastRound = round
gameOver = None
blueCastles = []
x = 0
y = 0
location = []
# Game
game = gameMap()


# Other functions
def checkWin():
	global gameOver
	if round > 2:
		if len(redLocations) == 0 and len(blueLocations) == 0:
			gameOver = "DRAW"
		elif len(redLocations) == 0:
			gameOver = "BLUEWIN!"
		elif len(blueLocations) == 0:
			gameOver = "RED WIN!"


def moveEnemies():
	global redLocations, blueLocations
	for enemy in range(len(redLocations)):
		redLocations[enemy].randomMove()
		for blue in range(len(blueLocations)):
			if round > 2 and redLocations[enemy].grid == blueLocations[blue].grid and redLocations[enemy].pos == blueLocations[blue].pos:
				print("damage happening enemy hit player")
				redLocations[enemy].health -=  5
				blueLocations[blue].health -= 10
	randList = []
	for i in range(len(redLocations)):
		if redLocations[i].health > 0:
			randList.append(redLocations[i])
	redLocations = randList

def pause():
	global channelOne
	global channelTwo
	global channelThree
	global channelFour
	global channelFive
	channelOne.pause()
	channelTwo.pause()
	channelThree.pause()
	channelFour.pause()
	channelFive.pause()


def playMusic(character, var):
	pause()
	if game.imageMap[character.grid][character.pos].biome == "mountainField" or game.imageMap[character.grid][character.pos].biome == "field" or game.imageMap[character.grid][character.pos].biome == "fieldTree" or game.imageMap[character.grid][character.pos].biome == "fieldVillageOpen" or game.imageMap[character.grid][character.pos].biome == "fieldVillageBlue" or game.imageMap[character.grid][character.pos].biome == "fieldVillageRed":
		channelOne.unpause()
		if channelOne.get_queue() == None:
			channelOne.queue(fieldMusic)
		if var == True:
			channelFour.play(moveGrass)
	elif game.imageMap[character.grid][character.pos].biome == "pond":
		channelThree.unpause()
		if channelThree.get_queue == None:
			channelThree.queue(waterTheme)
		if var == True:
			channelFour.play(moveWater)
	else:
		# print(game.imageMap[character.grid][character.pos])
		channelTwo.unpause()
		if channelTwo.get_queue() == None:
			channelTwo.queue(sandMusic)
		if var == True:
			channelFour.play(moveSand)

def capture():
	global available, blueCastles, game, blueLocations, counter
	print(blueLocations)
	counter = 0
	for character in blueLocations:
		if game.imageMap[character.grid][character.pos].biome == "sandVillageOpen":
			game.imageMap[character.grid][character.pos] = Square(sandImage, game.imageMap[character.grid][character.pos].squareRect[0], game.imageMap[character.grid][character.pos].squareRect[1], "sandVillageBlue")
			counter += 1
		elif game.imageMap[character.grid][character.pos].biome == "fieldVillageOpen":
			game.imageMap[character.grid][character.pos] = Square(fieldImage, game.imageMap[character.grid][character.pos].squareRect[0], game.imageMap[character.grid][character.pos].squareRect[1], "fieldVillageBlue")
			counter += 1
		blueCastles.append(Castle(character.grid, character.pos, game.imageMap[character.grid][character.pos].squareRect[0], game.imageMap[character.grid][character.pos].squareRect[1]))
		
		print(blueCastles)
		
	for castle in blueCastles:
		blueCharacterHere = random.choice(characterList)
		available = True
		if counter == 0:
			return None
		for blue in blueLocations:
			if blue.grid == castle.rect[0] and blue.pos == castle.rect[1]:
				available = False
		for red in redLocations:
			if red.grid == castle.rect[0] and red.pos == castle.rect[1]:
				available = False
		if available == True:
			print(castle.rect[0], castle.rect[1])
			blueLocations.append(Characters(castle.rect[0], castle.rect[1], blueCharacterHere, 15))
			counter -= 1

def click():
	global blueLocations, drawList, round, lastRound, blueKnightList, redKnightList
	mousePos = pygame.mouse.get_pos()
	mouseRect = pygame.Rect(mousePos[0], mousePos[1], 1, 1)
	hit = False
	for character in range(0, len(blueLocations)):
		if blueLocations[character].rect.colliderect(mouseRect):
			playMusic(blueLocations[character], False)
			hit = True
			drawList = []
			for tile in blueLocations[character].moveableTiles:
				infoTuple = (game.imageMap[tile[0]][tile[1]].squareRect, [tile[0], tile[1], blueLocations[character]])
				drawList.append(infoTuple)

	for tile in range(0, len(drawList)):
		if isinstance(drawList[tile][0],pygame.rect.Rect) and mouseRect.colliderect(drawList[tile][0]):
			hit = True
			for character in range(0, len(blueLocations)):
				#fix
				if blueLocations[character] == drawList[tile][1][2]:
					found = (blueLocations[character], character)
					break
			blueLocations[found[1]] = Characters(drawList[tile][1][0], drawList[tile][1][1], found[0].image, found[0].health)
			print("player moved to " + str(drawList[tile][1][0]), str(drawList[tile][1][1]))
			print(str(round))
			playMusic(blueLocations[found[1]], True)
			drawList = []
			for enemy in range(len(redLocations)):
				if round > 2 and redLocations[enemy].grid == blueLocations[character].grid and redLocations[enemy].pos == blueLocations[character].pos:
					redLocations[enemy].health -=  10
					blueLocations[index].health -= 5
			lastRound = round
			round += 1
			blueKnightList = []
			redKnightList = []
			moveEnemies()
			break
	if hit == False:
		drawList = []

# game loop
while True:
	checkWin()
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			pygame.quit()
			sys.exit()
		if event.type == pygame.KEYDOWN:
			if event.key == pygame.K_LEFT:
				game.moveLeft()
			if event.key == pygame.K_RIGHT:
				game.moveRight()
			if event.key == pygame.K_UP:
				game.moveUp()
			if event.key == pygame.K_DOWN:
				game.moveDown()
			if event.key == pygame.K_c:
				capture()
			if event.key == pygame.K_k:
				captureStuff = True
				captureTree = True
				blueKnightList = []
				castleList = []
		if event.type == pygame.MOUSEBUTTONUP:
			click()


		if event.type == pygame.MOUSEBUTTONDOWN:
			mousePos = pygame.mouse.get_pos()
			mouseRect = pygame.Rect(mousePos[0], mousePos[1], 1, 1)
			clickNone = True
			press_stat += 1

	if gameOver != None:
		largeValFont = pygame.font.Font("valFont.ttf", 125)
		smallValFont = pygame.font.Font("valFont.ttf", 75)
		display = largeValFont.render((gameOver), True, (255,255,255))
		gameOverRect = pygame.Rect(50, 50, screenView - 50, 200)
		screen.blit(display, gameOverRect)
		playAgain = smallValFont.render("Click to Play Again", True, (255,255,255))
		playAgainRect = pygame.Rect(50, 300, screenView-50, 200)
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				pygame.quit()
				sys.exit()
			elif event.type == pygame.MOUSEBUTTONUP:
				mouse = pygame.mouse.get_pos()
				mouseRect = pygame.Rect(mouse[0], mouse[1], 1,1)
				if mouseRect.colliderect(playAgainRect):
					blueWin = False
					redWin = False
					count_x = 0
					count_y = 0
					press_stat = False
					drawList = []
					castleList = []
					blueKnightList = []
					redKnightList = []
					lastRound = round
					gameOver = None
					x = 0
					y = 0
					location = []
					blueLocations = []
					redLocations = []
					round = 0
					lastRound = round
					displayBlue = False
					mineList = []
					treeList = []
					captureStuff = False
					captureTree = False
					pondList = []
					pp = True
					blueCastles = []
					game = gameMap()
				####################################################################################################################
		screen.blit(display, gameOverRect)
		screen.blit(playAgain, playAgainRect)	

	else:
		screen.fill((0, 0, 0))
		game.drawElements()
	pygame.display.update()
	clock.tick(60)