data = [(172031028000, 171031011000), (10010043016, 171031011111), (172031028011, 172031031121)]

# Add the dots to the IP
def proc_ip(a: int):
    a = str(a)
    return f'{a[:3]}.{a[3:6]}.{a[6:9]}.{a[9:]}'

# Add the dots to both ips on the tuple
def proc_tuple(a: tuple):
    return (proc_ip(a[0]), proc_ip(a[1]))

# Process each tuple
result = [proc_tuple(elem) for elem in data]

print(result)