# Simulation of hamming code

### Input
Binary string input parity bits included e.g 010010011000011001001

### Output wihtout error
[INPUT BINARY]: 010010011000011001001
No Error detected

### Output with error detected
[INPUT BINARY]: 010010011010011001001
Error position is in index 10
[CORRECT BINARY]: 010010011000011001001

### Error Correction
Error correction is automatic if error detected in the input against its parity bit.

`correctError("010010011000011001001")`