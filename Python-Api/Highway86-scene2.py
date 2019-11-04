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
state.transform = spawns[3]
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

#spawn form spans[1]
forward = lgsvl.utils.transform_to_forward(spawns[1])
right = lgsvl.utils.transform_to_right(spawns[1])

state.transform.position = spawns[1].position 
state.transform.rotation = spawns[1].rotation
npc9 = sim.add_agent(NPClist[random.randint(0, 3)], lgsvl.AgentType.NPC, state)

state.transform.position = spawns[1].position + 20.0 * forward
state.transform.rotation = spawns[1].rotation
npc10 = sim.add_agent(NPClist[random.randint(0, 3)], lgsvl.AgentType.NPC, state)

state.transform.position = spawns[1].position + 40.0 * forward
state.transform.rotation = spawns[1].rotation
npc11 = sim.add_agent(NPClist[random.randint(0, 3)], lgsvl.AgentType.NPC, state)

state.transform.position = spawns[1].position + 60.0 * forward
state.transform.rotation = spawns[1].rotation
npc12 = sim.add_agent(NPClist[random.randint(0, 3)], lgsvl.AgentType.NPC, state)

state.transform.position = spawns[1].position + 80.0 * forward
state.transform.rotation = spawns[1].rotation
npc13 = sim.add_agent(NPClist[random.randint(0, 3)], lgsvl.AgentType.NPC, state)

state.transform.position = spawns[1].position + 100.0 * forward + lgsvl.Vector(0,-1,1)
state.transform.rotation = spawns[1].rotation
npc14 = sim.add_agent(NPClist[random.randint(0, 3)], lgsvl.AgentType.NPC, state)

state.transform.position = spawns[1].position + 120.0 * forward + lgsvl.Vector(0,-1,2)
state.transform.rotation = spawns[1].rotation
npc15 = sim.add_agent(NPClist[random.randint(0, 3)], lgsvl.AgentType.NPC, state)

state.transform.position = spawns[1].position + 140.0 * forward + lgsvl.Vector(0,-1,2)
state.transform.rotation = spawns[1].rotation
npc16 = sim.add_agent(NPClist[random.randint(0, 3)], lgsvl.AgentType.NPC, state)

state.transform.position = spawns[1].position + 160.0 * forward + lgsvl.Vector(0,-1.5,2)
state.transform.rotation = spawns[1].rotation
npc17 = sim.add_agent(NPClist[random.randint(0, 3)], lgsvl.AgentType.NPC, state)

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
npc9.follow_closest_lane(True, 15)
npc10.follow_closest_lane(True, 15)
npc11.follow_closest_lane(True, 15)
npc12.follow_closest_lane(True, 15)
npc13.follow_closest_lane(True, 15)
npc14.follow_closest_lane(True, 15)
npc15.follow_closest_lane(True, 15)
npc16.follow_closest_lane(True, 15)
npc17.follow_closest_lane(True, 15)

input("Press Enter to run")

sim.run()