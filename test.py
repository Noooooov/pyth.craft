from mcpi_e.minecraft import Minecraft
import mcpi_e.block as Block 
import random as rn
from mcpi_e.vec3 import Vec3
import mcrcon 
import time

pName1 = "fladifox"
pName2 = "Nuvichok"
adrs = "26.65.92.192"

mc = Minecraft.create(address=adrs, playerName=pName2)
rcon = mcrcon.MCRcon(adrs, "rcon123")
rcon.connect()
