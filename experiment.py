import argparse

import rlglue.RLGlue as RLGlue

parser = argparse.ArgumentParser(description='Run DQN Recurrent experiment')
parser.add_argument('--maxsteps', metavar='S', type=int, default=0,
                   help='maximum steps per trial (0 for unlimited)')
parser.add_argument('--numeps', metavar='T', type=int, default=100,
                    help='number of episodes per trials')
args = parser.parse_args()

if __name__ == '__main__':
    print "\nExperiment starting!"
    taskSpec = RLGlue.RL_init()
    print taskSpec

    for whichEpisode in range(1, numeps+1):
	terminal=RLGlue.RL_episode(arg.maxsteps)
	totalSteps=RLGlue.RL_num_steps()
	totalReward=RLGlue.RL_return()

        # Not sure what this terminal variable is
        print "Episode {}\t#Steps {}\tTotal reward {}\tNatural end? {}".format(whichEpisode, totalSteps, totalReward, terminal)

    print "A job well done."
    RLGlue.RL_cleanup()
