from taxi_environment import TaxiEnv
from taxi_wrapper import Taxi

# Initialize a new environment with 1 taxi at a random location and display it:
env = TaxiEnv(num_taxis=1, num_passengers=2, max_fuel=None,
              taxis_capacity=None, collision_sensitive_domain=False,
              fuel_type_list=None, option_to_stand_by=True)
# env = TaxiEnv()
env.reset()
env.s = 1022
env.render()

# Initialize a new taxi object for the taxi, compute the shortest path to the point [4,4]:
cur_state = env.state
taxis_location = cur_state[0]
taxi1 = Taxi(taxis_location[0])
taxi1.compute_shortest_path([4, 4])
print(f'PATH: {taxi1.path_cords}, ACTIONS: {taxi1.path_actions}')

# Move the taxi to the destination and visualize the map
while taxi1.path_cords:
    env.step([taxi1.get_next_step()[1]])
    env.render()




