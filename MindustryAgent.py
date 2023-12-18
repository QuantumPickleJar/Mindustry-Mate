"""
The orchestrator between the decision making logic and state management programming
"""
class MindustryAgent:
    def __init__(self):
        self.state_manager = StateManager()
        self.decision_maker = DecisionMaker()

    def update_game_state(self, new_state):
        # Update the game state
        self.state_manager.update_state(new_state)

    def make_decision(self):
        # Make a decision based on the current state
        # get the proposed actions from the decision maker
        proposed_actions = self.decision_maker.propose_actions()

        # evaluate the proposed actions
        prioritized_actions = self.decision_maker.prioritize_actions(proposed_actions)
        
        # return the decision
        pass