from mcpi_e.minecraft import Minecraft
import mcpi_e.block as Block 
import random as rn
from mcpi_e.vec3 import Vec3
import mcrcon 
import time

pName1 = "fladifox"
pName2 = "Nuvichok"
adrs = "26.65.92.192"

spawn1 = "162 196 -29"
spawn2 = "192 196 -29"

mc = Minecraft.create(address=adrs, playerName=pName2)
rcon = mcrcon.MCRcon(adrs, "rcon123")
rcon.connect()

def GetPlayerReady():
    mc.postToChat("Кто готов к битве? Напиши '+'")
    while True:
        messages = mc.events.pollChatPosts()

        for mes in messages:
            if mes.message == "+":
                return mes.entityId, mc.entity.getName(mes.entityId), mc.entity.getPos(mes.entityId)

def Stroika(startpos: Vec3):
    endpos = startpos + Vec3(4, 5, 4)
    posGlavBlock = startpos + Vec3(2, 6, 2)
    mc.setBlocks(startpos, endpos, Block.STONE_BRICK)
    mc.setBlock(posGlavBlock, Block.EMERALD_ORE)
    return posGlavBlock

def PlayerStart(name: str, id: int, posBase: Vec3, cordSpawn):
    mc.entity.setPos(id, posBase)
    rcon.command("clear " + name)
    rcon.command("gamemode survival " + name)
    rcon.command("give " + name + " minecraft:wooden_sword")
    rcon.command("give " + name + " minecraft:golden_apple")
    rcon.command("give " + name + " minecraft:cooked_beef 3")
    rcon.command("give " + name + " minecraft:iron_helmet")
    rcon.command("give " + name + " minecraft:white_wool 128")
    rcon.command("give " + name + " minecraft:wooden_pickaxe")
    rcon.command("give " + name + " minecraft:shears")
    rcon.command("spawnpoint " + name + " " + cordSpawn)
    for i in range (5):
        rcon.command("summon firework_rocket " + cordSpawn + " {LifeTime:30,FireworksItem:{id:firework_rocket,Count:1,tag:{Fireworks:{Flight:2,Explosions:[{Type:1,Flicker:0,Trail:0,Colors:[I;14602026],FadeColors:[I;3887386,4312372]}]}}}}")
        time.sleep(0.1)
    

def End(name, startpos, id):
    rcon.command("gamemode creative " + name)
    rcon.command("clear " + name)
    rcon.command("spawnpoint " + name + " -24 64 13")
    mc.entity.setPos(id, startpos)

player1ID, player1Name, start1Pos = GetPlayerReady()
player2ID, player2Name, start2Pos = GetPlayerReady()
mc.postToChat("Набор закончен. Батл между " + player1Name + " и " + player2Name + " !!!")

pos1Baza = Vec3(0,100,0)
pos2Baza = Vec3(30,100,0)

mc.setBlocks(0,100,0, 36,115,12, Block.AIR)

pos1GlavBlock = Stroika(pos1Baza)
pos2GlavBlock = Stroika(pos2Baza)

time.sleep(1)

PlayerStart(player1Name, player1ID, pos1GlavBlock, spawn1)
PlayerStart(player2Name, player2ID, pos2GlavBlock, spawn2)

sec = 120
lastTick = time.time()
delay = 20

mc.postToChat("До конца боя " + str(sec) + " секунд")
mc.postToChat("Напиши gg, чтобы выйти из боя")
mc.postToChat("Напиши t, чтобы вернуться к базе")

winnerName = ""

while sec > 0:
    if lastTick + delay < time.time():
        mc.postToChat("До конца боя " + str(sec) + " секунд")
        mc.postToChat("Напиши gg, чтобы выйти из боя")
        
        lastTick = time.time()
        sec = sec - delay       

    messages = mc.events.pollChatPosts()

    for mes in messages:
        if mes.entityId == player1ID:
            if mes.message == "gg":
                sec = 0
            if mes.message == "t":
                PlayerStart(player1Name, player1ID, pos1GlavBlock, spawn1)
        if mes.entityId == player2ID:
            if mes.message == "gg":
                sec = 0
            if mes.message == "t":
                PlayerStart(player2Name, player2ID, pos2GlavBlock, spawn2)
    
    if mc.getBlock(pos2GlavBlock) != 129:
        winnerName = player1Name
        sec = 0  
    
    if mc.getBlock(pos1GlavBlock) != 129:
        winnerName = player2Name
        sec = 0
                
            
End(player1Name, start1Pos, player1ID)
End(player2Name, start2Pos, player2ID)
mc.postToChat("Бой закончен!")
mc.postToChat("Победил " + winnerName + ", поздравляем!")