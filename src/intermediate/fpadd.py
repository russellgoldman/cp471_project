"""
https://llvmlite.readthedocs.io/en/latest/user-guide/ir/examples.html

This file demonstrates a trivial function "fpadd" returning the sum of
two floating-point numbers.
"""
from llvmlite import ir
from generator import create_execution_engine, compile_ir
from ctypes import CFUNCTYPE, c_double, c_void_p

def generate_assembly():
    void = ir.VoidType()
    int = ir.IntType(255)
    double = ir.DoubleType()
    fnty = ir.FunctionType(void, [])

    module = ir.Module(name=__file__)
    func = ir.Function(module, fnty, name="fpadd")

    block = func.append_basic_block(name="entry")
    builder = ir.IRBuilder(block)
    # a, b = func.args
    
    # result = builder.fadd(a, b, name="res")
    # builder.ret(result)

    # while loop
    while_body_block = builder.append_basic_block('w_body')
    while_after_block = builder.append_basic_block('w_after')

    i = ir.Constant(int, 0)
    j = ir.Constant(int, 10)
    i_ptr = builder.alloca(i) #create the addresses
    j_ptr = builder.alloca(j)
    # with builder.if_then(builder.icmp_signed('<', i, j)):
    #     print('here')
    #     i = builder.add(i, ir.Constant(int, 1), 'b')

    # start of while loop
    builder.cbranch(builder.icmp_signed('<', i_ptr, j_ptr), while_body_block, while_after_block)
    builder.position_at_start(while_body_block)
    i_ptr = builder.add(i, ir.Constant(int, 1), 'b')

    # decide whether to loop again
    # builder.cbranch(builder.icmp_signed('<', i_ptr, j_ptr), while_body_block, while_after_block)
    # builder.position_at_start(while_after_block)
        
    builder.ret_void()
    # print(str(module))
    return str(module)

def run_assembly():
    engine = create_execution_engine()
    compile_ir(engine, generate_assembly())

    func_ptr = engine.get_function_address("fpadd")
    cfunc = CFUNCTYPE(c_void_p)(func_ptr)
    res = cfunc()

    return res


print(run_assembly())

"""
number = 0                  =>   number = ir.Constant(ir.DoubleType(), 0)
i = 0                       =>   i      = ir.Constant(ir.DoubleType(), 0)
L1: if i < 10 goto L2       =>
goto L3
L2: number = number + i
number = 3
number = 5
  i = i + 1
goto L1
L3:


Number number = 0;
for(Number i = 0; i < 10; i++) {
    number = number + i;
    number = 3;
    number = 5;
}

"""