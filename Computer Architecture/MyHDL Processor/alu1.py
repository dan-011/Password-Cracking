from myhdl import block, always_comb

@block
def ALU1bit(a, b, carryin, bnegate, operation, result, carryout):

    """ 1-bit ALU

    result and carrayout are output

    all other signals are input

    operation, the select signal to 4-input Mux, has two bits.
    We can compare operation directly integers, for example, 
        if operation == 0:

    """

    # the 'always_comb' decorator indicates a combinational circuit
    # the funciton name is not important. we could name it 'a_circuit'
    @always_comb
    def alu1_logic():
        # we can use Python do the computation
        # and then set the output signal
        # For example, to set signal s to value v
        #     s.next = v

        # notb is not a signal
        notb = not b

        # TODO
        input0 = None
        input1 = None
        input2 = None
        # Mux2
        if bnegate == 1:
            _b = notb
        else:
            _b = b
        # generate all inputs to Mux4 
        
        input0 = (a and _b)
        input1 = (a or _b)
        summation = a + _b + carryin
        carryout.next = 0
        input2 = 0
        if summation == 1:
            input2 = 1
        elif summation == 2:
            carryout.next = 1
        elif summation == 3:
            carryout.next = 1
            input2 = 1
        if operation == 0: result.next = input0
        elif operation == 1: result.next = input1
        elif operation == 2: result.next = input2
        elif operation == 3: result.next = 0
        # Mux4
        # remember to do "result.next = ..."

        # Generate carryout
        # again, remember to do "carryout.next = ..."

    # return the logic  
    return alu1_logic

if __name__ == "__main__":
    from myhdl import intbv, delay, instance, Signal, StopSimulation, bin
    import argparse

    # testbench itself is a block
    @block
    def test_comb(args):

        # create signals
        
        result = Signal(bool(0))
        carryout = Signal(bool(0))

        a, b, carryin, bnegate = [Signal(bool(0)) for i in range(4)]

        # operation has two bits
        operation = Signal(intbv(0)[2:])

        # instantiating a block
        alu1 = ALU1bit(a, b, carryin, bnegate, operation, result, carryout)

        @instance
        def stimulus():
            print("op a b cin bneg | cout res")
            for op in args.op:
                assert 0 <= op <= 3
                for i in range(16):
                    # use MyHDL intbv to split bits, instead of shift and AND
                    bi = intbv(i)
                    a.next, b.next, carryin.next, bnegate.next = \
                        bi[0], bi[1], bi[2], bi[3]
                    operation.next = op
                    yield delay(10)
                    print("{} {} {} {}    {}    | {}    {}".format(
                        bin(op, 2), 
                        int(a), int(b), int(carryin), int(bnegate), 
                        int(carryout), int(result)))

            # stop simulation
            raise StopSimulation()

        return alu1, stimulus

    parser = argparse.ArgumentParser(description='Testing 1-bit ALU')
    parser.add_argument('op', type=int, nargs='*', 
            default=[0, 1, 2], help='operation')
    # parser.add_argument('--less', '-l', type=int, default=0, choices=[0, 1], help='less signal')

    args = parser.parse_args()
    # print(args)

    tb = test_comb(args)
    tb.config_sim(trace=False)
    tb.run_sim()
