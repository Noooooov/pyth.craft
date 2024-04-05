from mcpi_e.minecraft import Minecraft
import mcpi_e.block as Block 

pName1 = "fladifox"
pName2 = "Nuvichok"
adrs = "26.249.215.9"
pt = 4711
shirDB = 30
visDB = 60
dlinDB = 40

def GetAns(pName:str):
    while True:
        messages = mc.events.pollChatPosts()
        for message in messages:
            if message.entityId == mc.getPlayerEntityId(pName):
                return message.message

mc = Minecraft.create(adrs, pt, pName2)
x, y, z = mc.player.getTilePos()
x = x + 10
mc.setBlocks(x, y, z, x+shirDB, y+visDB, z+dlinDB, Block.DIAMOND_BLOCK )
mc.setBlocks(x, y+1, z, x+shirDB-1, y+visDB-1, z+dlinDB-1, Block.AIR)
mc.setBlocks(x, y+1, z, x, y+1, z+dlinDB-1, Block.DIAMOND_BLOCK)
mc.setBlocks(x, y+1, z, x+shirDB-1, y+1, z, Block.DIAMOND_BLOCK)

while True:
    xPos, yPos, zPos = mc.player.getTilePos()

    if x < xPos < x+shirDB and z < zPos < z+dlinDB and y < yPos < y+visDB:
        mc.setBlocks(x+2, y+3, z+2, x+shirDB-1, y+visDB-1, z+dlinDB-1, Block.WATER)
    else:
        mc.setBlocks(x+2, y+3, z+2, x+shirDB-1, y+visDB-1, z+dlinDB-1, Block.AIR)