import angr, monkeyhex, binascii

FIND_ADDR = 0x00000a59
AVOID_ADDR = 0x08048554

proj = angr.Project('./testing', auto_load_libs = False)
state = proj.factory.entry_state()
simulation = proj.factory.simulation_manager(state)

print(simulation)
print("Searching for 'Success!' output")

simulation.explore(find = FIND_ADDR, avoid = AVOID_ADDR)


print(simulation.found)

