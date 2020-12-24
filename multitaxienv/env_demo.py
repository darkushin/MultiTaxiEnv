from taxi_environment import TaxiEnv
from taxi_wrapper import Taxi

env = TaxiEnv(num_taxis=2, num_passengers=2, max_fuel=None,
              taxis_capacity=None, collision_sensitive_domain=False,
              fuel_type_list=None, option_to_stand_by=True)

env = TaxiEnv()
env.reset()
env.s = 1022
env.render()

obser = env.step([2, 2])
env.render()
taxi1 = Taxi(obser[0][0][0])
taxi1.compute_path([4, 4])
print(f'PATH: {taxi1.path_to_dist}, ACTIONS: {taxi1.path_actions}')


