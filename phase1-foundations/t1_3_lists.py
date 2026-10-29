servers = ["web-01", "web-02", "db-01"]

print(servers[0])
print(servers[2])
print(servers)

cpu_readings = [42, 57, 61, 88]

print(len(cpu_readings))
print(cpu_readings[-1])
print(cpu_readings[1] + cpu_readings[2])
print(f"Latest CPU: {cpu_readings[-1]}% ")

alerts = ["disk-full"]
alerts.append("cpu-high")
alerts.append("service-down")

print(alerts)
print(len(alerts))

alerts[0] = "disk warning"
print(alerts[0])
print(alerts)




