#include <stdio.h>
#include <string.h>
#include "snappy.h"

/*
* int_to_float_buffer
* 
* First convert an int to float, then write the contents
* to data buffer that can be passed between C and SNAPpy.
*/
void int_to_float_buffer(int16_t i, uint8_t * float_buffer)
{
    float f = (float) i;
    memcpy(float_buffer, &f, sizeof(float));
}

/*
* float_buffer_to_int
*
* Write the contents of a float buffer back into a float,
* then return the int-truncated contents back to SNAPpy.
*/
int16_t float_buffer_to_int(uint8_t * float_buffer)
{
    float f = 0.0;
    memcpy(&f, float_buffer, sizeof(float));
    return (int)f;
}

/*
* get_pi
*
* Loads pi into a float buffer and returns the buffer to SNAPpy.
*/
void get_pi(uint8_t * float_buffer)
{
    float pi = 3.14159;
    memcpy(float_buffer, &pi, sizeof(float));
}

/*
* add
*
* Take two float buffers, load their contents into floats,
* add them together and load the result into a return buffer.
*/
void add(uint8_t * fb1, uint8_t * fb2, uint8_t * result)
{
    float f1 = 0.0;
    float f2 = 0.0;
    
    memcpy(&f1, fb1, sizeof(float));
    memcpy(&f2, fb2, sizeof(float));
    
    float f3 = f1 + f2;
    
    memcpy(result, &f3, sizeof(float));
}