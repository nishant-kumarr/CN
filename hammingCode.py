def calculate_parity(bits, indices):
    parity = 0
    for index in indices:
        if index < len(bits) and bits[index] == '1':
            parity ^= 1
    return parity

def encode_hamming(data):
    n = len(data)
    r = 0
    while (2**r) < (n + r + 1):
        r += 1

    total_length = n + r
    hamming_code = ['0'] * total_length
    j = 0

    for i in range(1, total_length + 1):
        if (i & (i - 1)) == 0:
            continue
        hamming_code[i - 1] = data[j]
        j += 1

    for i in range(r):
        parity_pos = 2**i
        indices_to_check = [k for k in range(total_length) if (k + 1) & parity_pos]
        hamming_code[parity_pos - 1] = str(calculate_parity(hamming_code, indices_to_check))

    return ''.join(hamming_code)

def decode_hamming(hamming_code):
    total_length = len(hamming_code)
    r = 0
    while (2**r) < (total_length + 1):
        r += 1

    error_position = 0
    for i in range(r):
        parity_pos = 2**i
        indices_to_check = [k for k in range(total_length) if (k + 1) & parity_pos]
        if calculate_parity(hamming_code, indices_to_check) != 0:
            error_position += parity_pos

    if error_position != 0:
        print(f"Error detected at position {error_position}. Correcting...")
        hamming_code = list(hamming_code)
        hamming_code[error_position - 1] = '1' if hamming_code[error_position - 1] == '0' else '0'

    data_bits = [hamming_code[i - 1] for i in range(1, total_length + 1) if (i & (i - 1)) != 0]
    return ''.join(data_bits)

# Input from the user
data = input("Enter binary data (e.g., 1011): ")
print("Original data:", data)

# Encoding
encoded = encode_hamming(data)
print("Encoded Hamming code:", encoded)

# Simulate an error (optional)
print("Introduce an error to test (optional).")
encoded_with_error = list(encoded)
error_bit = int(input(f"Enter error position (1-{len(encoded)}), or 0 for no error: "))
if error_bit > 0:
    encoded_with_error[error_bit - 1] = '1' if encoded_with_error[error_bit - 1] == '0' else '0'
    encoded_with_error = ''.join(encoded_with_error)
    print("Encoded with error:", encoded_with_error)

    # Decoding
    decoded = decode_hamming(encoded_with_error)
else:
    decoded = decode_hamming(encoded)

print("Decoded (corrected) data:", decoded)
