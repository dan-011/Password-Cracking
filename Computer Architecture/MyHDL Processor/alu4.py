from myhdl import block, always_comb, concat, instances
from alu1 import ALU1bit

# ALU1bit(a, b, carryin, bnegate, operation, result, carryout):

@block
def ALU4bits(a, b, alu_operation, result, zero):

    """ 4-bit ALU

    """
    # create internal signals

    # bnegate and operation are not regular signals
    # they are shadow siginals that follow alu_operation
    # we do not need to set value for bnegate and operation manually
    bnegate = alu_operation(2)      # bit 2    
    operation = alu_operation(2,0)  # bits 0 and 1

    cout = [Signal(bool(0)) for _ in range(4)]

    # create individual bits in result
    # we cannot use shadow signals of result 
    # because shadow signals are read only
    result_bits = [Signal(bool(0)) for _ in range(4)]

    # TODO
    # instantiat four 1-bit ALUs
    # An example of instantiating ALU4bits is in testbench() function  
    # 
    # Use shadow signals to connnect individual bits in 
    # signals `a` and `b` to 1-bit ALUs. 
    # For example, use a(0), not a[0], for bit 0 in `a`
    # a[0] is bit 0's value and will not change when `a` changes
    alu0 = ALU1bit(a(0), b(0), bnegate, bnegate, operation, result_bits[0], cout[0])
    alu1 = ALU1bit(a(1), b(1), cout[0], bnegate, operation, result_bits[1], cout[1])
    alu2 = ALU1bit(a(2), b(2), cout[1], bnegate, operation, result_bits[2], cout[2])
    alu3 = ALU1bit(a(3), b(3), cout[2], bnegate, operation, result_bits[3], cout[3])

    @always_comb
    def comb_output():
        # TODO
        # Compute the value of output signals `result` and `zero`
        # from the output of 1-bit ALUs
        # We can use Python operations, like `and` and  `or`
        # To set individual bits in `result`, we can do
        #   result.next[0] = ... 
        result.next[0] = result_bits[0]
        result.next[1] = result_bits[1]
        result.next[2] = result_bits[2]
        result.next[3] = result_bits[3]
        zero.next = not (result_bits[0] or result_bits[1] or result_bits[2] or result_bits[3])
    # return all logic  
    return instances()

if __name__ == "__main__":
    from myhdl import intbv, delay, instance, Signal, StopSimulation, bin
    import argparse

    # testbench itself is a block
    @block
    def test_comb(args):

        # create signals
        # use intbv for multiple bits
        a = Signal(intbv(0)[4:])
        b = Signal(intbv(0)[4:])
        result = Signal(intbv(0)[4:0])
        alu_operation = Signal(intbv(0)[4:])
        zero = Signal(bool(0))

        # instantiating a block
        alu = ALU4bits(a, b, alu_operation, result, zero)

        @instance
        def stimulus():
            print("ALU_opration a     b    | result zero")
            for op in args.operation_list:
                alu_operation.next = op
                for i in range(16):
                    bi = intbv(i)
                    a.next = args.a
                    b.next = bi[4:]
                    yield delay(10)
                    print("{:11}  {}  {} | {}   {}".format(
                        bin(op, 4), bin(a, 4), bin(b, 4),
                        bin(result, 4), int(zero)))

            # stop simulation
            raise StopSimulation()

        return alu, stimulus

    operation_list = [-1, 0, 1, 2, 6]
    parser = argparse.ArgumentParser(description='4-bit ALU')
    parser.add_argument('op', nargs='?', type=int, default=-1, choices=operation_list, 
            help='alu operation in decimal. -1 for all operations')

    parser.add_argument('-a', type=int, default=0b1010, help='input a in decimal')
    parser.add_argument('--trace', action='store_true', help='generate trace file')

    args = parser.parse_args()
    # print(args)

    if args.op < 0:
        args.operation_list = operation_list[1:]
    else:
        args.operation_list = [args.op]

    tb = test_comb(args)
    tb.config_sim(trace=args.trace)
    tb.run_sim()

