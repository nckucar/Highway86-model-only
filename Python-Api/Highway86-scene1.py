# -*- coding: utf-8 -*-
"""
Created on Sat Nov  2 15:42:45 2019

@author: Chen-Xuan LIN
"""
import os
import lgsvl
import random

#Load Map
sim = lgsvl.Simulator(os.environ.get("SIMULATOR_HOST", "127.0.0.1"), 8181)
if sim.current_scene == "Highway86":
  sim.reset()
else:
  sim.load("Highway86")

spawns = sim.get_spawn()

NPClist = ['Sedan','SUV','Jeep','Hatchback']

#Ego Vehicle
state = lgsvl.AgentState()
state.transform = spawns[1]
a = sim.add_agent("vehicle_lincoln2017mkz", lgsvl.AgentType.EGO, state)

state = lgsvl.AgentState()


#NPC Vehicle , spawn for spwans[4] 
forward = lgsvl.utils.transform_to_forward(spawns[4])
right = lgsvl.utils.transform_to_right(spawns[4])

state.transform.position = spawns[4].position
state.transform.rotation = spawns[4].rotation
npc1 = sim.add_agent(NPClist[random.randint(0, 3)], lgsvl.AgentType.NPC, state)

state.transform.position = spawns[4].position + 10.0 * forward
state.transform.rotation = spawns[4].rotation
npc2 = sim.add_agent(NPClist[random.randint(0, 3)], lgsvl.AgentType.NPC, state)

state.transform.position = spawns[4].position + 20.0 * forward
state.transform.rotation = spawns[4].rotation
npc3 = sim.add_agent(NPClist[random.randint(0, 3)], lgsvl.AgentType.NPC, state)

#spwan form spans[5]
forward = lgsvl.utils.transform_to_forward(spawns[5])
right = lgsvl.utils.transform_to_right(spawns[5])

state.transform.position = spawns[5].position
state.transform.rotation = spawns[5].rotation
npc4 = sim.add_agent(NPClist[random.randint(0, 3)], lgsvl.AgentType.NPC, state)

state.transform.position = spawns[5].position + 10.0 * forward
state.transform.rotation = spawns[5].rotation
npc5 = sim.add_agent(NPClist[random.randint(0, 3)], lgsvl.AgentType.NPC, state)

state.transform.position = spawns[5].position + 20.0 * forward
state.transform.rotation = spawns[5].rotation
npc6 = sim.add_agent(NPClist[random.randint(0, 3)], lgsvl.AgentType.NPC, state)

state.transform.position = spawns[5].position + 30.0 * forward
state.transform.rotation = spawns[5].rotation
npc7 = sim.add_agent(NPClist[random.randint(0, 3)], lgsvl.AgentType.NPC, state)

state.transform.position = spawns[5].position + 40.0 * forward
state.transform.rotation = spawns[5].rotation
npc8 = sim.add_agent(NPClist[random.randint(0, 3)], lgsvl.AgentType.NPC, state)

#spawn form spans[2]
forward = lgsvl.utils.transform_to_forward(spawns[2])
right = lgsvl.utils.transform_to_right(spawns[2])

state.transform.position = spawns[2].position 
state.transform.rotation = spawns[2].rotation
npc9 = sim.add_agent(NPClist[random.randint(0, 3)], lgsvl.AgentType.NPC, state)

state.transform.position = spawns[2].position + 20.0 * forward
state.transform.rotation = spawns[2].rotation
npc10 = sim.add_agent(NPClist[random.randint(0, 3)], lgsvl.AgentType.NPC, state)

state.transform.position = spawns[2].position + 40.0 * forward
state.transform.rotation = spawns[2].rotation
npc11 = sim.add_agent(NPClist[random.randint(0, 3)], lgsvl.AgentType.NPC, state)

state.transform.position = spawns[2].position + 80.0 * forward
state.transform.rotation = spawns[2].rotation
npc12 = sim.add_agent(NPClist[random.randint(0, 3)], lgsvl.AgentType.NPC, state)

#spawn form spans[3]
forward = lgsvl.utils.transform_to_forward(spawns[3])
right = lgsvl.utils.transform_to_right(spawns[3])

state.transform.position = spawns[3].position 
state.transform.rotation = spawns[3].rotation
npc13 = sim.add_agent(NPClist[random.randint(0, 3)], lgsvl.AgentType.NPC, state)

state.transform.position = spawns[3].position + 30.0 * forward
state.transform.rotation = spawns[3].rotation
npc14 = sim.add_agent(NPClist[random.randint(0, 3)], lgsvl.AgentType.NPC, state)

state.transform.position = spawns[3].position + 60.0 * forward
state.transform.rotation = spawns[3].rotation
npc15 = sim.add_agent(NPClist[random.randint(0, 3)], lgsvl.AgentType.NPC, state)

state.transform.position = spawns[3].position + 100.0 * forward
state.transform.rotation = spawns[3].rotation
npc16 = sim.add_agent(NPClist[random.randint(0, 3)], lgsvl.AgentType.NPC, state)



# 11.1 m/s is ~40 km/h , 5.6 m/s is ~20 km/h
#Activity NPC
npc1.follow_closest_lane(True, 5.6)
npc2.follow_closest_lane(True, 5.6)
npc3.follow_closest_lane(True, 5.6)
npc4.follow_closest_lane(True, 5.6)
npc5.follow_closest_lane(True, 5.6)
npc6.follow_closest_lane(True, 5.6)
npc7.follow_closest_lane(True, 5.6)
npc8.follow_closest_lane(True, 5.6)
npc9.follow_closest_lane(True, 11.1)
npc10.follow_closest_lane(True, 11.1)
npc11.follow_closest_lane(True, 11.1)
npc12.follow_closest_lane(True, 11.1)
npc13.follow_closest_lane(True, 11.1)
npc14.follow_closest_lane(True, 11.1)
npc15.follow_closest_lane(True, 11.1)
npc16.follow_closest_lane(True, 11.1)

input("Press Enter to run")

sim.run()