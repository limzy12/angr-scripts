## Demonstration of how angr's symbolic solver depends on length of the bitvectors

import angr, monkeyhex

bitlength = 64

proj = angr.Project('/bin/true')

for i in range(1, bitlength):
    print('Testing bitlength %d' % i)

    state = proj.factory.entry_state()
    input = state.solver.BVS('input', i) 
    operation = (((input + 4) * 3) >> 1) + input
    target = 200
    state.solver.add(operation == target)
    
    if state.satisfiable():
        result = state.solver.eval(input)
        print("Result: %s" % result)
    else:
        print("Not satisfiable")
