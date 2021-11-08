## Author:  Bram Meijer
## Date:    19-11-2019

import sys
from importlib import util
from timeit import default_timer as timer

  
## MAIN   
# Load the model
if len(sys.argv) < 2:
	print("Error: No model specified.")
	quit()
print("Loading model from \"{0}\"...".format(sys.argv[1]), end = "", flush = True)
spec = util.spec_from_file_location("model", sys.argv[1])
model = util.module_from_spec(spec)
spec.loader.exec_module(model)
network = model.Network() # create network instance
print(" done.")

start_time = timer()
##start timing

#check the statespace
initial_state = network.get_initial_state()
transitions = network.get_transitions(initial_state)
    

states = []
depth = []
states.append(initial_state)
depth.append(initial_state)
#print("number of transitions from initial:",len(transitions))
current_state = initial_state
n = 0
states
while True:
    print("current state:",current_state,"transistions:",len(transitions),"     n = ",n)
    #print("number of states =",len(states))
    #print(str(network.get_expression_value(current_state, 0)))
    next_state = network.jump_np(current_state, transitions[n])
    if next_state not in states :
        #print("---if")
        states.append(next_state)
        depth.append(next_state)
        transitions = network.get_transitions(next_state)
        current_state = next_state
        n = 0
    elif n < len(transitions)-1:
        #print("---elif n")
        #print("number of transitions: ",len(transitions))
        n += 1
    elif len(depth) > 1:
        #print("---elif")
        depth.pop()
        current_state = depth[-1]
        transitions = network.get_transitions(depth[-1])
        n = 0
    else: 
        break


print("number of states = ",len(states),"\n")
print("number of properties =",len(network.properties),"")

##stop timing
end_time = timer()
print("Done in {0:.2f} seconds.".format(end_time - start_time))