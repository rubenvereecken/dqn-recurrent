import copy
import cPickle as pickle
import argparse
from rlglue.agent.Agent import Agent
from rlglue.agent import AgentLoader as AgentLoader
from rlglue.types import Action
from rlglue.types import Observation

import numpy as np

from common import Message, MessageType

FRAME_WIDTH = 160
FRAME_HEIGHT = 210
FRAME_SIZE = FRAME_WIDTH * FRAME_HEIGHT
RAM_SIZE = 128

class QAgent(Agent):
    def __init__(self, args):
        # I'm of half a mind to just dump all args into the agent, but then it wouldn't 
        # be very pretty to debug or anything. So I'll be nice and write boilerplate. Thank me future me!
        # for key in arg_dict:
        #     setattr(self, key, arg_dict[key])

        # self.state_dim  = args.state_dim            # State dimensionality.
        # self.actions    = args.actions
        # self.n_actions  = len(self.actions)
        # self.verbose    = args.verbose
        # self.best       = args.best

        # # epsilon annealing
        # self.ep         = args.ep or 1             # Exploration rate
        # self.ep_start   = self.ep                  # Annealing start
        # self.ep_end     = args.ep_end or self.ep   # Lowest possible ep?
        # self.ep_endt    = args.ep_endt or 1000000  # Stop annealing at some t

        # # These will be used to keep track of transitions
        # self.last_action = None
        # self.last_observation = None
        pass

    def agent_init(self,taskSpec):
        # Maybe we can do something with the task spec at some point, verify that it meets expectations
        pass

    def extract_frame(self, observation):
        # Frames are located right after the RAM. Every value is in [0, 127]
        return np.array(observation.intArray[RAM_SIZE:RAM_SIZE+FRAME_SIZE], dtype=np.uint8)
        
            
    def agent_start(self,observation):
        #Generate random action, 0 or 1
        thisIntAction=self.randGenerator.randint(0,1)
        returnAction=Action()
        returnAction.intArray=[thisIntAction]
        
        last_action=copy.deepcopy(returnAction)
        last_observation=copy.deepcopy(observation)

        return returnAction
    
    def agent_step(self,reward, observation):
        #Generate random action, 0 or 1
        thisIntAction=self.randGenerator.randint(0,1)
        returnAction=Action()
        returnAction.intArray=[thisIntAction]
        
        last_action=copy.deepcopy(returnAction)
        last_observation=copy.deepcopy(observation)

        return returnAction
    
    def agent_end(self,reward):
        pass
    
    def agent_cleanup(self):
        pass
    
    def agent_message(self,inMessage):
        print inMessage


if __name__=="__main__":
    parser = argparse.ArgumentParser(description='Run DQN Recurrent experiment')
    parser.add_argument('--learn_start', metavar='L', type=int, default=5*10**4,
                        help='only start learning after an amount of steps in order to build a db')
    args = parser.parse_args()

    AgentLoader.loadAgent(QAgent(args))
