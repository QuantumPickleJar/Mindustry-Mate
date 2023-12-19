"""
The *The Strategist*
This file contains the DecisionMaker class, which is responsible for making decisions based on the data
provided by the StateManager class.  

Logic for determining the priority of actions, which actions would result in the most benefit, etc.
is contained herein
"""
class DecisionMaker:    

    RSC_THRESHOLD = {
        "copper": 250, 
        "lead": 250,
        "coal": 250,
        "titanium": 250,
        "silicon": 250,
        "thorium": 0,
        "plastanium": 0,
        "phase_fabric": 0,
        "surge_alloy": 0,
        "spore_pod": 0,
        "sand": 0,
        "blast_compound": 0,
        "pyratite": 0,
        "metaglass": 0,
        "scrap": 0,
        "graphite": 0,
        "coal_liquid": 0,
        "petroleum": 0,
        "water": 0,
        "slag": 0,
        "oil": 0,
        "cryofluid": 0
    }

    def __init__(self):
        # self.state_manager = StateManager()
        pass

    def propose_actions(self):
        # provide a list of desirable actions given the state
        actions = []
        if state_manager.evaluate_resources() < RSC_THRESHOLD:
            actions.append("gather_resources")
        if state_manager.get_enemy_info().get()
        pass

    def prioritize_actions(self, proposed_actions):
        # Prioritize the proposed actions
        # This will be based on the current state of the game
        # and the proposed actions
        

        pass