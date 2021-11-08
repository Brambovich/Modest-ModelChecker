## Author:  Bram Meijer
## Date:    19-11-2019

import sys
from importlib import util
from timeit import default_timer as timer
from queue import PriorityQueue
from collections import OrderedDict
from operator import itemgetter
from heapq import heappush, heappop


def printtrace(network, depth):
    total_length = len(depth)
    laststate = depth.pop()
    print("TRACE:\n")
    for i in range(len(depth)):
        secondlaststate = depth.pop()
        print(laststate)
        transitions = network.get_transitions(secondlaststate)
        for j in range(len(transitions)):
            if network.jump_np(secondlaststate, transitions[j]) == laststate:
                print("         ^^^")
                print("         ",network.transition_labels[transitions[j].label])
                print("         ^^^")

                #print("nothing found")
        laststate = secondlaststate
    print(laststate)
    print("\n\ntrace was: ", total_length, " long\n")
    
                
def checkproperty(network, propertynumber):
    initial_state = network.get_initial_state()
    transitions = network.get_transitions(initial_state)


    states = set()
    depth = list()
    states.add(initial_state)
    depth.append(initial_state)
    #print("number of transitions from initial:",len(transitions))
    current_state = initial_state
    n = 0

    states
    while True:
        #print("current state:",current_state,"transistions:",len(transitions),"     n = ",n)
        
        #print("number of states =",len(states))
        #print(str(network.get_expression_value(current_state, 0)))
        next_state = network.jump_np(current_state, transitions[n])

        
        #cost += network._get_transient_value(next_state,"sent")
        #print("      transient cost is: " ,cost)
        if network.get_expression_value(next_state, propertynumber):
            
            print("property proven!!")
            depth.append(next_state)
            printtrace(network, depth)

            
            
            return True
            #return next_state
        
        previouslength = len(states)
        states.add(next_state)
        
            
        if len(states) > previouslength :
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
            
            current_state = depth.pop()
            transitions = network.get_transitions(current_state)
            n = 0
        else: 
            print("number of states: ",len(states))
            #if propertyproven:
            print("property was not proven!")
            break


  
def checkxmin(network, propertynumber):
    reward = []	
    is_reward = network.properties[propertynumber].exp is not None and network.properties[propertynumber].exp.op == "xmin" and network.properties[propertynumber].exp.args[1].op == "ap"
    if is_reward:
	    reward = [network.properties[propertynumber].exp.args[0]]
    print("* The first property is", "" if is_reward else " not", " a cost-optimal reachability property.", sep = "")    
    initial_state = network.get_initial_state() 
    initial_state_transitions = network.get_transitions(initial_state)
    #next_state = network.jump_np(initial_state, initial_state_transitions[0], reward)
    #print(reward)
    #if reward[0] == 2:
    #    print("hoi")
    state_id = 0
    depth = list()
    state_cost = list()
    checked_states = dict()
    ##checked_states.append([initial_state,0,False])    
    checked_states[initial_state] = (0,state_id,list())
    #state = CostState(0,initial_state)
    heappush(state_cost,(0,state_id,initial_state))
    #print(str(checked_states[0][0]))
    current_state = initial_state
    next_state = initial_state
    cost = 0
    transnumber = 0
    #checked_states.append([next_state,reward[0]])
    #print(len(checked_states))
    transitions = initial_state_transitions
    #print(transitions)
    print("initial state is ", initial_state)
    current_state_cost = 0
    delete_current = False
    #print(initial_state_transitions)
    #print(checked_states)
    count_it = 0
    
    
    
    while True:
        
        reward = [network.properties[propertynumber].exp.args[0]]       
        #GET THE LOWEST OR SOMETHING
        #current_state = checked_states[min_index][0] 
        
        transitions = network.get_transitions(current_state)
        #print("current state is:",current_state)
        if(transnumber>=len(transitions)):
            print("         len of trans:", len(transitions), "transnumber: ", transnumber)
            print("         number of iterations:", count_it)
            print(current_state)
            fulltrace = checked_states[current_state][2]
            #fulltrace.append(current_state)
            fulltrace.reverse()
            fulltrace.append(current_state)

            printtrace(network, fulltrace)
            break



        checkthis = True
        if (count_it%5000 == 0 and checkthis):
            tmp_time = timer()
            hours, rem = divmod(tmp_time-start_time, 3600)
            minutes, seconds = divmod(rem, 60)
            print(" --->    Time is = {:0>2}:{:0>2}:{:05.2f}    <---".format(int(hours),int(minutes),seconds))
            print("         number of iterations:", count_it)
            print("         length of checked_states:", len(checked_states))
            print("current state:\n", current_state)
        elif (checkthis == False):
            print("cost is: ",cost)
            print("current state:\n", current_state, "\n")

        next_state = network.jump_np(current_state, transitions[transnumber], reward)

        cost = current_state_cost + reward[0]

       
        
        #check if the cost in the states was already there and if higher replace, else add
        
        depth = list()

        depth.append(current_state)
        if len(checked_states[current_state][2])>0 :
            depth = depth + checked_states[current_state][2]

        if(delete_current):
            del checked_states[current_state]
            delete_current = False
        #print(depth)
        
        if next_state in checked_states:
            if checked_states[next_state][0] > cost:
                state_id += 1
                tempcost = checked_states[next_state][0]
                tempid = checked_states[next_state][1]
                checked_states[next_state]= (cost,state_id, depth)
                
                state_cost.remove((tempcost, tempid, next_state))
                heappush(state_cost,(cost,state_id,next_state))
                    
                    
        else:
            #print("             state is added:", next_state)
            state_id += 1
            checked_states[next_state] = (cost,state_id,depth)
            heappush(state_cost,(cost,state_id,next_state))
            
        #hier moet ie ook nog in de dict worden gezet.
        
        #print(state_cost)
        current_lowest = heappop(state_cost)
    
		################### use sets or dictionaries. order queue for getting the state.
        if network.get_expression_value((current_lowest[2]), network.properties[propertynumber].exp.args[1].args[0]) == True:
            print("\n         FOUND! with cost value:",current_lowest[0])
            print("         In state:", current_lowest[2], "\n")
            fulltrace = checked_states[current_lowest[2]][2]
            #fulltrace.append(current_state)
            fulltrace.reverse()
            fulltrace.append(current_lowest[2])

            printtrace(network, fulltrace)

            break
        
        if current_state == current_lowest[2]:
            
            if transnumber < len(network.get_transitions(current_state))-1 :
                transnumber += 1
                heappush(state_cost, current_lowest)
                #print("increase transnumber, new one is:",transnumber)
            elif len(state_cost) >= 1:
                #print("in the else, len is:", len(state_cost))
                current_state = current_lowest[2]
                current_state_cost = current_lowest[0]
                delete_current = True
                transnumber = 0
            else:
                print("not found, number of states:", len(checked_states))  
                break  
                
                
                #add it to the depth
                #delete it
                #depth.append(current_state)  
                

        else: #change the current state to the state with the lowest cost
            #print("in the else")
            transnumber = 0
            current_state = current_lowest[2]
            current_state_cost = current_lowest[0]
            heappush(state_cost, current_lowest)

        count_it += 1
            
            


              
        

   
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
print(" -- START -- ")

start_time = timer()
##start timing

#check the statespace
#states = checkstatespace(network)
#print("number of states = ",len(states),"\n")
#print("number of properties =",len(network.properties),"")



## check all properties
j = 0
while j < len(network.properties):
    if network.properties[j].exp is not None and network.properties[j].exp.op == "exists" and network.properties[0].exp.args[0].op == "eventually" and network.properties[0].exp.args[0].args[0].op == "ap":
        propertyboolean = checkproperty(network, j)
## hier iets met provestate is niet NULL
    elif network.properties[j].exp is not None and network.properties[j].exp.op == "xmin" and network.properties[j].exp.args[1].op == "ap":
        print(network.properties[j])
        checkxmin(network, j)
        
    j += 1
    
##stop timing
end_time = timer()
hours, rem = divmod(end_time-start_time, 3600)
minutes, seconds = divmod(rem, 60)
print("done in = {:0>2}:{:0>2}:{:05.2f}".format(int(hours),int(minutes),seconds))