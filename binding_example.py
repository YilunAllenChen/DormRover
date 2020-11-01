import ctypes
import pathlib


# https://realpython.com/python-bindings-overview/#ctypes

if __name__ == "__main__":
    libname = pathlib.Path().absolute() / 'lib.so'
    c_lib = ctypes.CDLL(libname)

    print(c_lib.add_extern(1,2))

    encoded_str = "hi from python".encode("utf-8")

    c_lib.print_content.argtypes = [ctypes.c_char_p]
    echo = c_lib.print_content(encoded_str)


    print(echo)