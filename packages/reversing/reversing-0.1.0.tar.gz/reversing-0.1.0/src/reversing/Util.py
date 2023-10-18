import struct
from arc4 import ARC4
from Crypto.Util.number import long_to_bytes as l2b, bytes_to_long as b2l
from Crypto.Cipher import AES

types = {
    16:'H',
    32:'I',
    64:'Q'
}
## macros function 

ROL = lambda val, r_bits, max_bits: \
    (val << r_bits%max_bits) & (2**max_bits-1) | \
    ((val & (2**max_bits-1)) >> (max_bits-(r_bits%max_bits)))
 
# Rotate right: 0b1001 --> 0b1100
ROR = lambda val, r_bits, max_bits: \
    ((val & (2**max_bits-1)) >> r_bits%max_bits) | \
    (val << (max_bits-(r_bits%max_bits)) & (2**max_bits-1))

def unpack_ls(buf:bytes,base:int,endian = '<')->bytes:
    """
    Unpacks a list of integers from the given bytes object representing binary data.

    Parameters:
    - buf (bytes): Input bytes object containing binary data to be unpacked.
    - base (int): Size of each number in bits. For example, if base is 8, each number is 8 bits (1 byte) long.
    - endian (str, optional): Byte order used to represent the numbers. 
                              Use '<' for little-endian (default) or '>' for big-endian.

    Returns:
    - list: A list of unpacked integers obtained from the input buf.

    Example Usage:

    ```
    binary_data = b'\x01\x02\x03\x04'
    >>> unpacked_numbers = unpack_ls(binary_data, 16)
    >>> print("Unpacked Numbers:", unpacked_numbers)
    Unpacked Numbers: [258, 772]

    >>> unpacked_numbers = unpack_ls(binary_data, 32, '>')
    >>> print("Unpacked Numbers:", unpacked_numbers)
    Unpacked Numbers: [16909060]
    ```
    
    Usage Notes:
    - Ensure that the 'base' parameter corresponds to the correct size of each number in bits.
    - The 'endian' parameter allows flexibility in handling byte order for compatibility with different data sources.
    """
    return list(struct.unpack(endian + str(base//8) + types[base],buf))

def pack_ls(l:list,base:int,endian = '<')->bytes:
    """
    Packs a list of integers into a bytes object representing binary data.

    Parameters:
    - l (list): List of integers to be packed into binary data.
    - base (int): Size of each number in bits. For example, if base is 8, each number is 8 bits (1 byte) long.
    - endian (str, optional): Byte order used to represent the numbers. 
                              Use '<' for little-endian (default) or '>' for big-endian.

    Returns:
    - bytes: A bytes object containing the packed binary data.

    Example Usage:

    ```
    numbers = [258, 772]
    >>> packed_data = pack_ls(numbers, 16)
    >>> print("Packed Data:", packed_data)
    Packed Data: b'\x01\x02\x03\x04'

    numbers = [16909060]
    >>> packed_data = pack_ls(numbers, 32, '>')
    >>> print("Packed Data:", packed_data)
    Packed Data: b'\x01\x02\x03\x04'
    ```
    
    Usage Notes:
    - Ensure that the 'base' parameter corresponds to the correct size of each number in bits.
    - The 'endian' parameter allows flexibility in handling byte order for compatibility with different data sources.
    """
    return list(struct.pack(endian + str(base//8) + types[base],l))

def xorb(b1:bytes, b2:bytes):
    """
    Performs element-wise XOR operation on two bytes objects and returns the result as a new bytes object.

    Notes:
    - If the input bytes objects are of different lengths, XOR operation wraps around the shorter bytes object cyclically.
    - The output bytes object is of the same length as the longer input bytes object.
    """
    l1 = len(b1)
    l2 = len(b2)
    if l1>l2:
        return bytes([b1[i]^b2[i%l2] for i in range(l1)])
    else:
        return bytes([b2[i]^b1[i%l1] for i in range(l2)])
def xorn(b:bytes, n:int):
    """
    Performs element-wise XOR operation between a bytes object and an integer within the range [0, 255].
    
    Parameters:
    - b (bytes): Input bytes object.
    - n (int): Integer value in the range [0, 255] for XOR operation.

    Returns:
    - bytes: A new bytes object containing the result of element-wise XOR operation between b and n.

    Notes:
    - The integer n is automatically masked to ensure it falls within the valid byte range [0, 255].
    - The output bytes object has the same length as the input bytes object b.
    """
    if n<0 or n>255:
        raise ValueError("Number not in range [0,256]")
    return bytes([b[i]^n&0xff for i in range(len(b))])