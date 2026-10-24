#Implement Q-learning and use it to find the optimal policy for this MDP.  
# Note that for this algorithm you will need the Q values, which are values 
# for state/action pairs. Similar to before, you will run episodes repeatedly
# until the maximum change in any Q value is less than 0.001.  Use a learning
# rate (alpha) of 0.1, and a discount rate (lambda) of 0.99.  
# Use an epsilon-greedy policy for training that places 80% of the weight on the optimal action, 
# and chooses a uniform random action with the remaining 20% probability 
# (recall that the Q-learning updates and convergence are independent of the policy being followed, 
# so it should converge as long as every state/action pair continues to be selected). 
#Each time you update a Q value, print out the previous value, the new value, the 
# immediate reward, and the Q value for the next state.  At the end, print out the 
# number of episodes, the final Q values, and the optimal policy
