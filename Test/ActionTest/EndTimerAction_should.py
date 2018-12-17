import unittest
from Game.Action.Other.EmptyAction import EmptyAction
from Game.Action.Other.EndTimeAction import EndTimeAction


class EndTimerActionTest(unittest.TestCase):

    def test_TimerActionRemoveHimselfFromTrackerTest(self):
        args = [1,set(),set(),set()]
        end_timer = EndTimeAction(EmptyAction(),5)
        args[3].add(end_timer)
        for i in range(6):
            self.assertEqual(end_timer.get_time(),5 -i)
            tracker = args[3].copy()
            for action_holder in tracker:
                for action in action_holder.get_actions:
                    action.act(*args)
        self.assertEqual(args[3].__len__(),0)

