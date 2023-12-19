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
        '''
        Evaluates all of the eneemy entities currently present, and 
        accumulates a threat level based on the summed value. 

        Different units will have different points to add towards the 
        threat level
        '''
        threat_level = 0
        for enemy in self.enemy_spawns:
            if enemy['type'] == 'strong_lad':
                threat_level += 10
            elif enemy['type'] == 'lad':
                threat_level += 5
            # TODO: add more enemy types later, including accounting for their health pool and abilities
                
        return {"threat_level": threat_level}

    def get_building_info(self):
        
        pass

    def get_unit_info(self):

        pass

