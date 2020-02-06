def rgb2hex(red, green, blue):
    
    # The standard hex(arg) function returns a string with the hex value of the
    # arg, prefixed with '0x'.

    # [2:] is used to get rid of the '0x' prefix.

    # % 256 is used to keep the integer values between 0 and 255, as requested
    # by the rgb pattern.

    # Floats are converted to integers with the standard int() function.

    # If something fails, raise the following error message (with ValueError or
    # TypeError):

    # "The arguments 'red', 'green' and 'blue' in the function rgb2hex() must be
    # either integers or floats.'"

    error_message = "The arguments 'red', 'green' and 'blue' in the function " \
                  + "rgb2hex() must be either integers or floats."

    try:
        hex_value = '#'
        hex_value += hex(int(red) % 256)[2:].zfill(2)
        hex_value += hex(int(green) % 256)[2:].zfill(2)
        hex_value += hex(int(blue) % 256)[2:].zfill(2)
        return hex_value
    except ValueError as err:
        err.args = (error_message,)
        raise
    except TypeError as err:
        err.args = (error_message,)
        raise