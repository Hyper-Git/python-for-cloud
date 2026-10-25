server = input("Server name: ")
disk   = input("Disk used %: ")
limit  = int(input("Alert limit %: "))

print(f"{server}: disk {disk}%, limit {limit}%")
print(type(disk))
print(type(limit))
