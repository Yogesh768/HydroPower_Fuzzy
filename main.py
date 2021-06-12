from ranges import *
from control_rules import *

dc_ctrl = ctrl.ControlSystem(rules)
dc = ctrl.ControlSystemSimulation(dc_ctrl)

dc.input["Water Level"] = int(input("Enter Water Level: "))
dc.input["Flow Rate"] = int(input("Enter Flow Rate: "))

dc.compute()

print("Drain Valve: ",dc.output["Drain Valve"],"%")
print("Release Valve: ",dc.output["Release Valve"],"%")
drain_valve.view(sim = dc)
release_valve.view(sim = dc)

plt.show()