import argparse

import rlglue.RLGlue as RLGlue

from common import Message, MessageType


class Experiment(object):
    # To consult all parameters present, check out the argument parser below
    def __init__(self, arg_dict):
        self.step = 0
        self.n_train_episodes = 0
        self.agent_params = None

        # Simple load the whole argument dictionary into self
        for key in arg_dict:
            setattr(self, key, arg_dict[key])


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

        while self.step <= self.steps:
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

        print "A job well done."
        RLGlue.RL_cleanup()



    def message_agent(self, msg, data=None):
        return RLGlue.RL_agent_message(Message(msg, data).dumps())



if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Run DQN Recurrent experiment')
    parser.add_argument('--steps', metavar='S', type=int, default=10**5,
                        help='total amount of steps to train for')

    parser.add_argument('--report_freq', metavar='R', type=int, default=5*10**3,
                        help='frequency of report output for both experiment and agent')
    parser.add_argument('--eval_freq', metavar='E', type=int, default=10**4,
                        help='frequency of greedy evaluation for metric gathering')
    parser.add_argument('--save_freq', metavar='S', type=int, default=5*10**4,
                        help='todo')

    args = parser.parse_args()

    experiment = Experiment(vars(args))
    experiment.start()
