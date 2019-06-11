### Python script to find flags for Linux chmod cmd ###
import angr, claripy, monkeyhex

def hook_getopt(state):
    state.regs.eax = SYMB

def solve():

    global SYMB

    # Set load options and load binary
    loadOpt = {'main_opts':{'arch':'x86'}}
    proj = angr.Project('chmod', load_options = loadOpt)
    
    # Get address to be hooked
    main_obj = proj.loader.main_object
    HOOK_ADDR = main_obj.plt['getopt_long']

    argv = ['chmod', claripy.BVS('flags', 8)]
    state = proj.factory.entry_state(args = argv, addr = HOOK_ADDR)
    state.add_constraints(argv[1] >= ' ')
    state.add_constraints(argv[1] <= '~')
    SYMB = argv[1]

    proj.hook(HOOK_ADDR, hook_getopt(state), length = 5)
    
    sim = proj.factory.simgr(state)
    sim.explore()

    print(sim.found)
if __name__ == '__main__':
    solve()
