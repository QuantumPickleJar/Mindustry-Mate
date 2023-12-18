"""
The *Observer*
This is the state manager for the mindustry mate.  
The statemanager gathers information about the running game using the games API
Then, it cleans up the information into a more appropriate format for the decision maker
"""
class StateManager:
    def __init__(self):
        # Initialize state vars
        self.my_rsc = {}
        self.buildings = []
        self.units = []
        self.enemy_spawns = []


    def update_state(self, game_state):
        # Update the state based on the provided state
        self.my_rsc = game_state['my_rsc']
        self.buildings = game_state['buildings']
        self.units = game_state['units']
        self.enemy_spawns = game_state['enemy_spawns']    
        pass

    def evaluate_resources(self):
        # Evaluate the resources that the player has
        # This will be used to determine what MMate can do
        
        # evaluate scarcity of resources


        # return some evaluation or status
        pass

    def get_enemy_info(self):
    

        pass

    def get_building_info(self):

        pass

    def get_unit_info(self):

        pass

