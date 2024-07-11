def shift_in(number, bit, bits=16):
    # Left shift the number
    shifted = (number << 1) & ((1 << bits) - 1)

    # If we're shifting in a 1, set the rightmost bit
    if bit == 1:
        shifted |= 1

    return shifted


def n_groups_of_4_bits(number, n):
    # Convert the number to binary and remove the '0b' prefix
    binary = bin(number)[2:]

    # Pad the binary string to 16 bits
    padded_binary = binary.zfill(16)

    # Split the binary string into groups of 4 bits
    groups = [padded_binary[i : i + 4] for i in range(0, len(padded_binary), 4)]

    # Take only the first N groups
    return groups[n:]


def group_4bits(number, n):
    selected_groups = n_groups_of_4_bits(number, n)
    return set(int(group[1:], 2) for group in selected_groups if group[0] == "0")


def shift_register_simulator(pattern, num_multiplexers=4, num_bits=4):
    total_bits = num_bits * num_multiplexers
    value = 2**total_bits - 1

    all_values = set()
    for i in range(total_bits + 3):
        value = shift_in(value, int(pattern[i]) if i < num_bits else 1, total_bits)
        all_values |= group_4bits(value, num_multiplexers)

    print(pattern, all_values)


assert shift_in(0b1111, 1, 4) == 0b1111
assert shift_in(0b1111, 0, 4) == 0b1110
assert shift_in(0b1111, 0, 2) == 0b10
assert shift_in(0b1111, 1, 2) == 0b11
assert shift_in(0b1111_1111_1111_1111, 0, 16) == 0b1111_1111_1111_1110


def generate_binary_strings(bits=4):
    return [format(i, f"0{bits}b") for i in range(2**bits)]


def main():
    for binary in generate_binary_strings(bits=4):
        shift_register_simulator(binary, num_multiplexers=2, num_bits=4)
