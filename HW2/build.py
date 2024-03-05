from cffi import FFI


ffi = FFI()

ffi.cdef("""
    double cadd(double a, double b);
    double csub(double a, double b);
    double cmul(double a, double b);
    double cdiv(double a, double b);
""")

# with open("./operation.h") as f:
#     ffi.cdef(f.read())

ffi.set_source("_operation", '#include "operation.h"', sources=["operation.c"])

if __name__ == "__main__":
    ffi.compile()