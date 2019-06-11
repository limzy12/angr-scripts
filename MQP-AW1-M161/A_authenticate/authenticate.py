### Python script to crack password of authenicate.c ###
import angr, monkeyhex

# Loading binary and state
proj = angr.Project('authenticate')
state = proj.factory.entry_state()
print('Binary loaded')

# Start the simulation manager
sim = proj.factory.simgr(state)
print('Simulation manager started at %s' % hex(sim.active[0].addr))
print(sim)

# Set the desired address and the address to avoid
# Note: we need to take into account the base address loaded
FIND_ADDR = 0x00400819
AVOID_ADDR = 0x00400806

# Explore the binary
path = sim.explore(find = FIND_ADDR, avoid = AVOID_ADDR)
print('Binary exploration COMPLETE.')
print(path)

# Print the steps taken
print("------Steps taken------")
for step in path.found[0].history.descriptions:
    print(step)

# Print stuff in state.posix.dumps
print('POSIX dump: ' + str(path.found[0].posix.dumps(0)))
