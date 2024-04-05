from mcpi_e.minecraft import Minecraft
import mcpi_e.block as Block 
import random as rn
from mcpi_e.vec3 import Vec3
import mcrcon 
import time

adrs = "26.229.93.50"

mc = Minecraft.create(address=adrs)
rcon = mcrcon.MCRcon(adrs, "rcon123")
rcon.connect()

class Player(object):
    def __init__(self, ID, name):
        self.ID = ID
        self.name = name
        self.startPos = 0
    
    def tp(self, pos):
        mc.entity.setPos(self.ID, pos)

    def GetPos(self):
        pos = mc.entity.getPos(self.ID)
        return pos

class Platform(object):
    def __init__(self, player:Player, pos: Vec3, size = 3, block = 101, dist = 100):
        self.block = block
        self.dist = dist
        self.pos = pos
        self.size = size
        self.player = player
        self.lavaPosX = self.pos.x+1

    def build(self):
        mc.setBlocks(self.pos, self.pos.x+self.dist+20, self.pos.y+self.size+10, self.pos.z+self.size+10, Block.AIR)
        mc.setBlocks(self.pos, self.pos.x+self.dist, self.pos.y+self.size+1, self.pos.z+self.size+1, Block.GLASS)
        mc.setBlocks(self.pos.x+1, self.pos.y+1, self.pos.z+1, self.pos.x+self.dist, self.pos.y+self.size, self.pos.z+self.size, Block.AIR)
        mc.setBlocks(self.pos.x+1, self.pos.y+1, self.pos.z+1, self.pos.x+2, self.pos.y+1, self.pos.z+self.size, 171)
        mc.setBlocks(self.pos.x+self.dist+2, self.pos.y, self.pos.z, self.pos.x+self.dist+6, self.pos.y, self.pos.z+4, Block.DIAMOND_BLOCK)
        mc.setBlocks(self.pos.x+self.dist+3, self.pos.y, self.pos.z+1, self.pos.x+self.dist+5, self.pos.y, self.pos.z+3, Block.AIR)
        mc.setBlocks(self.pos.x+self.dist+4, self.pos.y-1, self.pos.z+2, self.pos.x+self.dist+4, self.pos.y+1, self.pos.z+2, Block.DIAMOND_BLOCK)
        self.EndBlock()

    def CreateObsecT1(self, x):
        startPos = Vec3(self.pos.x+x, self.pos.y+1, self.pos.z+2)
        
        mc.setBlocks(startPos, startPos + Vec3(0,2,0), Block.BEDROCK)
        mc.setBlocks(startPos + Vec3(0,2,-1),startPos + Vec3(0,2,1), Block.BEDROCK)
        mc.setBlocks(self.pos.x+x, self.pos.y, self.pos.z+1, self.pos.x+x+1, self.pos.y, self.pos.z+1, Block.AIR)

    def CreateObsecT2(self, x):
        startPos = Vec3(self.pos.x+x, self.pos.y+1, self.pos.z+2)
        
        mc.setBlocks(startPos, startPos + Vec3(0,2,0), Block.BEDROCK)
        mc.setBlocks(startPos + Vec3(0,2,-1),startPos + Vec3(0,2,1), Block.BEDROCK)
        mc.setBlocks(self.pos.x+x, self.pos.y, self.pos.z+3, self.pos.x+x+1, self.pos.y, self.pos.z+3, Block.AIR)

    def CreateObsec1(self, x):
        startPos = Vec3(self.pos.x+x, self.pos.y+1, self.pos.z+2)

        mc.setBlocks(startPos + Vec3(0,0,-1),startPos + Vec3(0,0,1), Block.BEDROCK)

    def CreateObsec2(self, x):
        startPos = Vec3(self.pos.x+x, self.pos.y+1, self.pos.z+2)

        mc.setBlocks(startPos + Vec3(0,2,-1),startPos + Vec3(0,2,1), Block.BEDROCK)
        mc.setBlocks(startPos + Vec3(1,-1,-1),startPos + Vec3(3,-1,1), Block.AIR)

    def CreateObsec3(self, x):
        startPos = Vec3(self.pos.x+x, self.pos.y+1, self.pos.z+2)
        
        mc.setBlocks(startPos + Vec3(1,-1,-1), startPos + Vec3(5,-1,1), Block.AIR)
        mc.setBlock(startPos + Vec3(3,-1,0), Block.GLASS)
        mc.setBlocks(startPos + Vec3(1,1,-1), startPos + Vec3(1,1,0), Block.BEDROCK)
        mc.setBlocks(startPos + Vec3(5,1,0), startPos + Vec3(5,1,1), Block.BEDROCK)

    def Start(self):
        startPos = Vec3(self.pos.x+2, self.pos.y+1, self.pos.z+3) 

        self.player.startPos = self.player.GetPos()
        self.player.tp(startPos)
        rcon.command("gamemode adventure " + self.player.name)
        rcon.command("give " + self.player.name + " minecraft:flint_and_steel")



    def Lava(self):
        if self.lavaPosX < self.pos.x+self.dist:
            startPos = Vec3(self.lavaPosX, self.pos.y+1, self.pos.z+1)
            endPos = startPos + Vec3(0, self.size - 1, self.size - 1)

            mc.setBlocks(startPos, endPos, Block.LAVA_FLOWING)
            self.lavaPosX = self.lavaPosX + 1
            

    def RnObsec(self, x):
        random = rn.randint(1,4)
        if random == 1:
            self.CreateObsecT1(x)
            x=x+3
            self.CreateObsecT2(x)
        if random == 2:
            self.CreateObsec1(x)
        if random == 3:
            self.CreateObsec2(x)
        if random == 4:
            self.CreateObsec3(x)
        return x
    
    def EndBlock(self):
        self.EndBlockPos = Vec3(self.pos.x+self.dist+4, self.pos.y+2, self.pos.z+2)
        mc.setBlock(self.EndBlockPos, Block.TNT)

    def ClearLava(self):
        mc.setBlocks(self.pos.x, self.pos.y-1, self.pos.z+1, self.pos.x+self.dist, self.pos.y-1, self.pos.z+3, Block.AIR)
        mc.setBlocks(self.pos.x+self.dist, self.pos.y+1, self.pos.z+1, self.pos.x+self.dist-1, self.pos.y+3, self.pos.z+3, Block.AIR)

    def ClearPlat(self):
        mc.setBlocks(self.pos.x-1, self.pos.y-1, self.pos.z-1, self.pos.x+self.dist+30, self.pos.y+5, self.pos.z+5, Block.AIR)
    
    def OnDeath(self):
        rcon.command("gamemode creative " + self.player.name)
        rcon.command("clear " + self.player.name + " minecraft:flint_and_steel")
        self.player.tp(self.player.startPos)


def End():
    for platT in platforms:
        plat: Platform = platT
        plat.OnDeath()
        plat.ClearPlat()
           
z = 200

while True: #самый главный цикл - на работу всего скрипта
    isWaitStart = True
    mc.postToChat("Программа запущена. Напиши 'Start' чтобы начать набор в гонку")

    lastTick = time.time()
    while isWaitStart == True: #цикл для отслеживания в чате "старт"
    
        if lastTick+20 < time.time():
            lastTick = time.time()
            mc.postToChat("Программа запущена. Напиши 'Start' чтобы начать набор в гонку")

        messages = mc.events.pollChatPosts()
        for mes in messages:
            print(mes.message)
            if mes.message.lower() == "start":
                isWaitStart = False

    #основаня программа        
    platforms = []
    mc.postToChat("Идёт набор в гонку. Напиши '+' чтобы присоединиться")
    isWaitPlayers = True

    #ждем игроков
    while isWaitPlayers == True:
        if lastTick+15 < time.time():
            isWaitPlayers = False
        
        messages = mc.events.pollChatPosts()
        for mes in messages:
            if mes.message == "+": 
                playerID, playerName, playerPos = mes.entityId, mc.entity.getName(mes.entityId), mc.entity.getPos(mes.entityId)

                playerReg = False
                for plat in platforms:
                    plat: Platform = plat
                    if plat.player.ID == playerID:
                        playerReg = True
                        break
                
                if playerReg == True:
                    rcon.command("w " + playerName + " Регистрация уже выполнена!")
                else:
                    player = Player(playerID, playerName)
                    plat = Platform(player = player, pos = Vec3(0,100, z))
                    platforms.append(plat)
                    mc.postToChat("Количество игроков: " + str(len(platforms)))
                    plat.build()

                    for x in range(plat.pos.x+10,  plat.dist, 7):
                        x = plat.RnObsec(x)

                    z = z+15

    isHavePlayers = True
    #проверка что игроки есть                
    if len(platforms) == 0:
        isHavePlayers = False

    if isHavePlayers == False:
        mc.postToChat("Игроки не присоединились")
        mc.postToChat("Игра отменена")
    
    else:  
        mc.postToChat("Игра начинается!")
        for plat in platforms:
            plat.Start()


        lavaMS = 0.5 #скорость обновления лавы в секундах
        mc.postToChat("Старт лавы через...")

        for i in range(3,0,-1):
            mc.postToChat(i)
            time.sleep(1)

        isRun = True
        while isRun == True:
            if len(platforms) == 0:
                mc.postToChat("Игра окончена")
                isRun = False
                break

            if lastTick + lavaMS < time.time():
                for platform in platforms:
                    platform.Lava()

                lastTick = time.time()

            for platform in platforms:
                    platform: Platform = platform
                    platform.ClearLava()
                    
                    if mc.getBlock(platform.EndBlockPos) == Block.AIR.id:
                        player = platform.player
                        mc.postToChat("Выиграл " + player.name)
                        
                        isRun = False
                        
                    if platform.player.GetPos().y < platform.pos.y-3:
                        platform.OnDeath()
                        platform.ClearPlat()
                        
                        platforms.remove(platform)
                        mc.postToChat(platform.player.name + " упал!")
                        mc.postToChat("Осталось игроков: " + str(len(platforms)))
                        break              
        End()   