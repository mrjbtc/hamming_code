"""
    @Author: mrjbtc <marjunebatac@gmail.com>
    @Date: 2024/11/23
    @Links: 
    	https://www.geeksforgeeks.org/hamming-code-in-computer-network/ 
    	https://users.cs.fiu.edu/~downeyt/cop3402/hamming.html
"""

import functools

'''
 Get the positions and values of the parity bits
 {
 	position: 1|0
 }
'''
def getParityBits(binary):
	binary = list(binary)
	length = len(binary)
	parityBits = {}
	
	for position in range(0, length):
		parityBitPosition = pow(2, position) # parity bit positions are 1, 2, 4, 8, 16, ....
		if  parityBitPosition <= length:
			parityBits[parityBitPosition-1] = int(binary[parityBitPosition-1]) # parityBitPosition-1 because array starts at 0
	return parityBits

def parityCheck(binary, parityBits):
	binary = list(binary)
	parity = {}
	for parityBitPosition in parityBits:
		bits = []
		start = parityBitPosition
		powerOfTwoParityBit = parityBitPosition+1 # plus 1 due to array start from zero
		end = powerOfTwoParityBit
		while True:
			data = binary[start:end+parityBitPosition] # getting the necessary data in the array
			start += powerOfTwoParityBit*2
			end += powerOfTwoParityBit*2
			if not data:
				break
			bits += data

		# excluding the parity bit, so removing the very first post
		bits.pop(0)

		# XOR operation to calculate the parity of the entire list which is covered by the parity bits
		parity[parityBitPosition] = functools.reduce(lambda a, b: int(a) ^ int(b), bits)
	  
	return parity

def detectError(binary):
	parityBits = getParityBits(binary)
	parity = parityCheck(binary, parityBits)
	parityError = []
	for parityPosition, parityBit in parity.items():
		if parityBit != parityBits[parityPosition]:
			parityError.append(int(parityPosition)+1) # plus one since array start from zero

	if len(parityError) > 0:
		errorPosition = sum(parityError)-1 # minus one, to pin point the exact position in the array.
		print("Error position is in index", errorPosition)
		return errorPosition

	print("No Error detected")
	return None

def correctError(binary):
	print("[INPUT BINARY]:", binary)
	errorPosition = detectError(binary)
	if errorPosition is None:
		return # If no error detected then stop from here.

    # Error correction
	binary = list(binary)
	binary[errorPosition] = str(int(binary[errorPosition]) ^ 1) # XOR operation for the position in the array
	correctBinary = ''.join(binary)
	print("[CORRECT BINARY]:", correctBinary)
	return correctBinary


correctError("010010011000011001001")
