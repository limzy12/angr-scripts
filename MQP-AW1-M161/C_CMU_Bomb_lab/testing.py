import angr, monkeyhex

proj = angr.Project('bomb')
s = proj.factory.call_state(addr = 0x40145c, ret_addr = 0x400f0a, stack_base =
        0x401460)
print(s.regs.rbp)
print(s.regs.rip)
