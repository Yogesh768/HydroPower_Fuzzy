import pandas as pd
from ranges import *
df = pd.read_csv('rules.csv')

rules = []

waterL = df["Water Level"].tolist()
flowR = df["Flow Rate"].tolist()

releaseV = df["Release Valve"].tolist()
drainV = df["Drain Valve"].tolist()


for i in range(25):
	rules.append(ctrl.Rule(water_level[waterL[i]] & flow_rate[flowR[i]], release_valve[releaseV[i]]))
	rules.append(ctrl.Rule(water_level[waterL[i]] & flow_rate[flowR[i]], drain_valve[drainV[i]]))