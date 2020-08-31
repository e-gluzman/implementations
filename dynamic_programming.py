import numpy as np
import sys
if "../" not in sys.path:
  sys.path.append("../") 
from lib.envs.gridworld import GridworldEnv

env = GridworldEnv()

#tup = env.P[1][3][0][3]
#print(tup)

def policy_eval(policy, env, discount_factor=1.0, theta=0.00001):
    """
    Evaluate a policy given an environment and a full description of the environment's dynamics.
    
    Args:
        policy: [S, A] shaped matrix representing the policy.
        env: OpenAI env. env.P represents the transition probabilities of the environment.
            env.P[s][a] is a list of transition tuples (prob, next_state, reward, done).
            env.nS is a number of states in the environment. 
            env.nA is a number of actions in the environment.
        theta: We stop evaluation once our value function change is less than theta for all states.
        discount_factor: Gamma discount factor.
    
    Returns:
        Vector of length env.nS representing the value function.
    """

    # Start with a random (all 0) value function
    V = np.zeros(env.nS)
    
    while True:   #any(Vdiff > theta):
        
        delta_V = 0

        for i in range(env.nS):
            
            # need to calculate the value of taking each of the available actions

            action_val = np.zeros(env.nA)

            for a in range(env.nA):
                
                # get transition tuple for this state and action
                tup = env.P[i][a][0]
                
                # calculate the value of this action/state? 
                #  value = reward + gamma * (prob * V[next_state])
                # error here I think, probability missing
                action_val[a] = tup[0] * (tup[2] + discount_factor * V[tup[1]])
            
           
            Vold = V[i]
            Vnew = np.dot(policy[i],action_val)
            delta_V = max(delta_V,np.abs(Vnew - Vold))
            # get state value by multiplying probability of taking action (policy) by action value
            V[i] = Vnew
            
            #print(action_val)
            #print(policy[i])
            #print(V[i])
            #print(delta_V)

        # function only works if I use this delta rule to terminate
        if delta_V < theta:
            break
    return np.array(V)

random_policy = np.ones([env.nS, env.nA]) / env.nA
v = policy_eval(random_policy, env)

expected_v = np.array([0, -14, -20, -22, -14, -18, -20, -20, -20, -20, -18, -14, -22, -20, -14, 0])
np.testing.assert_array_almost_equal(v, expected_v, decimal=2) 