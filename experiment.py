import argparse
import simplejson as json

import rlglue.RLGlue as RLGlue

from common import Message, MessageType

parser = argparse.ArgumentParser(description='Run DQN Recurrent experiment')
parser.add_argument('--steps', metavar='S', type=int, default=10**5,
                    help='total amount of steps to train for')

parser.add_argument('--report_freq', metavar='R', type=int, default=5*10**3,
                    help='frequency of report output for both experiment and agent')
parser.add_argument('--eval_freq', metavar='E', type=int, default=10**4,
                    help='frequency of greedy evaluation for metric gathering')
parser.add_argument('--save_freq', metavar='S', type=int, default=5*10**4,
                    help='todo')

# learn_start should be in experiment because it should know when to switch to greedy eval,
# since agent can't trivially control the experiment
parser.add_argument('--learn_start', metavar='L', type=int, default=5*10**4,
                    help='only start learning after an amount of steps in order to build a db')

args = parser.parse_args()

class Experiment(object):
    def __init__(self, args):
        self.step = 0
        self.max_steps = args.steps
        self.n_train_episodes = 0
        self.agent_params = None

    def start(self):
        print "\nExperiment starting!"
        taskSpec = RLGlue.RL_init()
        print taskSpec

        exp_params_for_agent = {}
        self.agent_params = self.message_agent(MessageType.exchange_params, exp_params_for_agent)

        # Keep overhead a bit lower by having functions inline
        def should_report(): self.step % args.report_freq == 0
        def should_evaluate(): step % args.eval_freq == 0 and step > self.agent_params['learn_start']
        def should_save(): step % args.save_freq == 0

        observ_action = RLGlue.RL_start()

        while self.step <= self.max_steps:
            observ_action_term = RLGlue.RL_step()

            # If game ends, start another
            if observ_action_term.terminal:
                # Not sure if we need to clean up after every episode, don't think so
                RLGlue.RL_start()
                self.n_train_episodes += 1

            if should_report():
                # TODO assert agent steps is equal
                print 'Steps: {}'.format(step)
                self.message_agent(MessageType.report)
            
            if should_evaluate():
                pass

            if should_save():
                pass



    def message_agent(self, msg, data=None):
        return RL_agent_message(Message(msg, data).dumps())



if __name__ == '__main__':
    experiment = Experiment(args)
    experiment.start()
    # Step through episodes. 1-based
    step = 0





         




    for whichEpisode in range(1, numeps+1):
	terminal=RLGlue.RL_episode(arg.maxsteps)
	totalSteps=RLGlue.RL_num_steps()
	totalReward=RLGlue.RL_return()

        # Not sure what this terminal variable is
        print "Episode {}\t#Steps {}\tTotal reward {}\tNatural end? {}".format(whichEpisode, totalSteps, totalReward, terminal)

    print "A job well done."
    RLGlue.RL_cleanup()
