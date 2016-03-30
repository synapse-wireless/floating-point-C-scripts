'''
Using Floating Point in SNAPpy with C Support

SNAPpy with C support provides the ability to use floating point
in your C code.  This functionality does not require any additional
libraries or includes:  declaring 'float f' is enough.  However,
there are two things of note that are worth mentioning.

 1.  Code size increase 

Adding floating point operations will increase
your generated code size by around 800 bytes.  This may be significant
depending on your script and other operations.

 2.  Getting your floats between C -> SNAPpy -> C

SNAPpy does not support floating type.  If you need to return a float
from a C function back to SNAPpy and provide it to another C function
later, you will need to use a string as a temporary buffer.  The float
will NOT be converted into a printable type when stored in the string.
Instead, the float is memcpy'd to the string, simply using it as a
uint8_t buffer which carries the bytes of the string between calls.
Then, when the float is needed in a C function again, you can memcpy
it back from the uint8_t to a float.  Note that when using a temporary
buffer, you may have to create a copy of the buffer to pass to your C
code:

float_buf1 = "     "
...
    temp = float_buf1[:]
    c_function_call(temp)

as the SNAPpy compiler will treat float_buf1 as a constant in such 
an instance.

These example functions are ONLY intended to demonstrate how one would 
hand floating type variables back and forth between SNAPpy and C.

'''

import_c("floatoing_point.c")

float_buf1 = "     "
float_buf2 = "     "
float_buf3 = "     "

@c_function(api=["none", "str"])
def get_pi(s):
    pass

@c_function(api=["none", "int", "str"])
def int_to_float_buffer(int, float_buffer):
    pass

@c_function(api=["none", "str", "str", "str"])
def add(f1, f2, f3):
    pass
    
@c_function(api=["int", "str"])
def float_buffer_to_int(s):
    pass

'''
1.  Generate editable versions of our temporary buffers.
2.  Load pi into them.
3.  Call add
4.  Return the int() of them.
'''
def pi_addition_test():
    temp = float_buf1[:]
    temp2 = float_buf2[:]
    temp3 = float_buf3[:]
    get_pi(temp)
    get_pi(temp2)

    add(temp, temp2, temp3)
    return float_buffer_to_int(temp3)
    
    
'''
1.  Generate editable versions of our temporary buffers.
2.  Load integer values into them, which are converted to floats
3.  Call add
4.  Return the int() of them.
'''
def int_to_float_addition_test():
    temp = float_buf1[:]
    temp2 = float_buf2[:]
    temp3 = float_buf3[:]
    
    int_to_float_buffer(7, temp)
    int_to_float_buffer(3, temp2)
    
    add(temp, temp2, temp3)
    return float_buffer_to_int(temp3)
    