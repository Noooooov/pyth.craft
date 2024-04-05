from mcpi_e.minecraft import Minecraft
import mcpi_e.block as Block 
import random as rn
from mcpi_e.vec3 import Vec3
import mcrcon 

pName1 = "fladifox"
pName2 = "Nuvichok"
adrs = "26.249.215.9"
pt = 4711

x = rn.randint(10, 150)
y = rn.randint(-60, 60)
z = rn.randint(10, 150)
posBlock = Vec3(x, y, z)

mc = Minecraft.create(adrs, pt, pName2)
rcon = mcrcon.MCRcon(adrs, "rcon123",25575)
rcon.connect()
mc.postToChat("ЗАПУЩЕН ИСКАТЕЛЬ ОНЛАЙН")
mc.setBlock(posBlock, Block.DIAMOND_BLOCK)

while True:
    pPos:Vec3 = mc.player.getTilePos()
    s = (posBlock - pPos).length()
    s = int(s)
    block = mc.getBlock(posBlock)
    if s > 100:
        mc.postToChat("Северни полюс")
    elif s > 70:
        mc.postToChat("Арктические пустыни")
    elif s > 50:
        mc.postToChat("По лесам бродиишь")
    elif s > 25:
        mc.postToChat("Тепло")
    elif s > 15:
        mc.postToChat("Ещё теплее")
    elif s > 10:
        mc.postToChat("Горячо")
    elif s > 5:
        mc.postToChat("Кипяток")
    elif s > 3:
        mc.postToChat("Ломай уже блок давай!!!")
    if block != 57:
        mc.postToChat("Блок найден")
        mc.postToChat("ИСКАТЕЛЬ ОНЛАЙН ОКОНЧЕН")
        break

rcon.command("give Nuvichok minecraft:stick 6400")