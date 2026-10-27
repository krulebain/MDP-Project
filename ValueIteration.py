#Implement the value iteration algorithm and use it to find the optimal policy for this MDP.  
# Set all value estimates to 0 initially. Use a discount rate (lambda) of 0.99. 
# Each time you update the value of a state, print out the previous value, the 
# new value, the estimated value of each action, and the action selected. Continue 
# to update each state until the maximum change in the value of any state in a single 
# iteration is less than 0.001.  At the end, print out the number of iterations (i.e., 
# the number of times you updated each state), the final values for each state, and the 
# final optimal policy. 
V = {}
for s in states:
    V[s] = 0.0
V["END"] = 0.0

iterations = 0
while True:
    iterations = iterations + 1
    new_v = {}
    biggest_change = 0.0
    
    for s in states:
        best_value = None
        best_action = None
        for a in mdp[s]:
            action_value= 0.0
            for(prob, next_s, reward) in mdp[s][a]:
                action_value = action_value + prob * (reward + GAMMA * V[next_s])
            if best_value is None or action_value > best_value:
                best_value = action_value
                best_action = a
                
        new_v[s] = best_value
        change = abs(best_value - V[s])
        if change > biggest_change:
            biggest_change = change
        
    for s in states:
        V[s] = new_v[s]
    if biggest_change < 0.001:
        break