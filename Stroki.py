from mcpi_e.minecraft import Minecraft
import random as rn
import mcpi_e.block as Block 
import time

pName1 = "fladifox"
pName2 = "Nuvichok"
adrs = "26.249.215.9"
pt = 4711

def GetAns(pName:str):
    while True:
        messages = mc.events.pollChatPosts()
        for message in messages:
            if message.entityId == mc.getPlayerEntityId(pName):
                return message.message

mc = Minecraft.create(adrs, pt, pName2)
msg = "Hello world! " + pName2 + " " + pName1
mc.postToChat(msg)
ans = GetAns(pName2)
mc.postToChat(pName2 + " Answeres " + ans)
mc.postToChat("/kill @a")