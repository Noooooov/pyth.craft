from mcpi_e.minecraft import Minecraft
import random as rn
import mcpi_e.block as Block 
import time

adrs = "26.249.215.9"
pt = 4711
pname = "Nuvichok"
mc = Minecraft.create(adrs, pt, pname)


while True:
    x = rn.randint(3, 10)
    y = rn.randint(5, 15)
    z = rn.randint(3, 10)
    mc.player.setTilePos(x, y, z)
    time.sleep(3)