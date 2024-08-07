import pandas as pd

states_df = pd.read_csv("main_data/50_states.csv")
state_coord = states_df["Alabama"]

print(state_coord)