from cffi import FFI


ffi = FFI()

with open("./operation.h") as f:
    ffi.cdef(f.read())

ffi.set_source("_cal_pi", '#include "cla_pi.h"', sources=["cla_pi.cpp"])

if __name__ == "__main__":
    ffi.compile()