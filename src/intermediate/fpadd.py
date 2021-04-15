"""
https://llvmlite.readthedocs.io/en/latest/user-guide/ir/examples.html

This file demonstrates a trivial function "fpadd" returning the sum of
two floating-point numbers.
"""
from llvmlite import ir
from generator import create_execution_engine, compile_ir
from ctypes import CFUNCTYPE, c_double

def generate_assembly():
    double = ir.DoubleType()
    fnty = ir.FunctionType(double, (double, double))

    module = ir.Module(name=__file__)
    func = ir.Function(module, fnty, name="fpadd")

    block = func.append_basic_block(name="entry")
    builder = ir.IRBuilder(block)
    a, b = func.args
    result = builder.fadd(a, b, name="res")
    builder.ret(result)

    return str(module)

def run_assembly():
    engine = create_execution_engine()
    mod = compile_ir(engine, generate_assembly())

    func_ptr = engine.get_function_address("fpadd")
    cfunc = CFUNCTYPE(c_double, c_double, c_double)(func_ptr)
    res = cfunc(10.0, 20.0)

    return res

print(run_assembly())