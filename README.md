[![](https://cloud.githubusercontent.com/assets/1317406/12406044/32cd9916-be0f-11e5-9b18-1547f284f878.png)](http://www.synapse-wireless.com/)

# SNAPpy Example - Floating Point Numbers in C

IAR can handle floating point in C, while SNAPpy cannot.  There may be times where you may want to pass a floating point number back up to a SNAPpy function and then pass it to another C function later.  This example shows how this can be done using SNAPpy string buffers as a data buffer to hold the float as binary data (not "3.14159", but using memcpy() to write the float to the uint8_t *, and just treat it as a buffer to carry the float around.

## License

Copyright © 2016 [Synapse Wireless](http://www.synapse-wireless.com/), licensed under the [Apache License v2.0](LICENSE.md).

<!-- meta-tags: vvv-atmega, vvv-Mmath, vvv-python, vvv-c, vvv-snappy, vvv-example -->
