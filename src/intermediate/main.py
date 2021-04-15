from generator import create_execution_engine, compile_ir
from ctypes import CFUNCTYPE, c_double
from example import generate_example

engine = create_execution_engine()
mod = compile_ir(engine, generate_example())

# Look up the function pointer (a Python int)
func_ptr = engine.get_function_address("fpadd")

# Run the function via ctypes
cfunc = CFUNCTYPE(c_double, c_double, c_double)(func_ptr)
res = cfunc(10.0, 20.0)
print(res)