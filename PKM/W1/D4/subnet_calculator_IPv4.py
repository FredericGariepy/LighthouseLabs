# Written 06.26.24
def cal_subnet_host(cird: int) -> str:
    network_class = int(cird/8) # what quarters of the IPv4 are filled. (Byte chunks)
    borrow = cird % 8 # How many bits are being borrowed by the subnetmask.
    subnets = 2**borrow # Number of subnets.
    total_bits = 4*8 # Total number of bits givent a IPv4 (4 bytes)
    host_bits = total_bits - (network_class * 8 + borrow) # Total number of remaining bits for host
    total_hosts = 2**host_bits # Total number of possible hosts per subnet
    usable_hosts_per_subnet = total_hosts - 2  
    print("For CIDR/{} network:\n There are {} subnets each with {} usable hosts".format(cird, subnets, usable_hosts_per_subnet))

for i in range(1,31):
    cal_subnet_host(i)
