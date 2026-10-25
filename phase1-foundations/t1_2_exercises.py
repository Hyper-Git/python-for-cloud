server_name = input("Server Name: ")
total_disk_size = float(input("What is the disk size: "))
used_disk_value = float(input("What is the used disk value in GB: "))
percentage_used = used_disk_value / total_disk_size * 100

print(f"{server_name}: {used_disk_value} GB used of {total_disk_size} GB ({percentage_used:.1f}%)")
