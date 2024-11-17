# Function to determine the class of an IP address
def get_ip_class(ip):
    first_octet = int(ip.split('.')[0])
    if first_octet >= 1 and first_octet <= 127:
        return "Class A"
    elif first_octet >= 128 and first_octet <= 191:
        return "Class B"
    elif first_octet >= 192 and first_octet <= 223:
        return "Class C"
    elif first_octet >= 224 and first_octet <= 239:
        return "Class D"
    else:
        return "Class E"

# Function to convert subnet bits to subnet mask
def subnet_bits_to_mask(bits):
    mask = ['255', '255', '255', '255']
    i = 0
    while bits > 8:
        mask[i] = '255'
        bits -= 8
        i += 1
    if bits > 0:
        mask[i] = str(256 - (2 ** (8 - bits)))
    return '.'.join(mask)

# Function to calculate the subnet IP address based on subnet mask and IP
def calculate_subnet_ip(ip, subnet_mask):
    ip_parts = list(map(int, ip.split('.')))
    mask_parts = list(map(int, subnet_mask.split('.')))
    subnet_ip = [str(ip_parts[i] & mask_parts[i]) for i in range(4)]
    return '.'.join(subnet_ip)

# Main program
def main():
    # Input from user
    ip_address = input("Enter the IP address (e.g., 192.168.1.1): ")
    subnet_bits = int(input("Enter the number of subnet bits (e.g., 24): "))
    
    # Determine the IP class
    ip_class = get_ip_class(ip_address)
    print(f"IP Class: {ip_class}")

    # Convert subnet bits to subnet mask
    subnet_mask = subnet_bits_to_mask(subnet_bits)
    print(f"Subnet Mask: {subnet_mask}")
    
    # Calculate the subnet IP address
    subnet_ip = calculate_subnet_ip(ip_address, subnet_mask)
    print(f"Subnet IP Address: {subnet_ip}")

if __name__ == "__main__":
    main()
