from llvmlite import ir
from generator import create_execution_engine, compile_ir
from ctypes import CFUNCTYPE, c_double, c_void_p

def generate_assembly():
    c = None
    d = None
    e = None
    f = None
    g = None
    h = None

    void = ir.VoidType()
    double = ir.DoubleType()
    fnty = ir.FunctionType(double, (double, double))

    module = ir.Module(name=__file__)
    func = ir.Function(module, fnty, name='goto')

    block = func.append_basic_block(name='entry')
    builder = ir.IRBuilder(block)
    a, b = func.args

    c = builder.fadd(a, b, 'c')
    bb_new = builder.append_basic_block(name='foo')

    with builder.goto_block(bb_new):
        d = builder.fadd(a, b, 'd')
        with builder.goto_entry_block():
            e = builder.fsub(a, b, 'e')

        f = builder.fsub(b, a, 'f')
        builder.branch(bb_new)

    g = builder.fmul(b, a, 'g')
    with builder.goto_block(bb_new):
        f = builder.fmul(a, b, 'h')

    builder.ret(c)
    print(str(module))
    return str(module)


def run_assembly():
    engine = create_execution_engine()
    mod = compile_ir(engine, generate_assembly())

    func_ptr = engine.get_function_address("goto")
    cfunc = CFUNCTYPE(c_double, c_double, c_double)(func_ptr)
    res = cfunc(1, 2)

    return res


print(run_assembly())

"""
c = a + b
{
    d = a + b
}
e = a - b
f = a - b



"""