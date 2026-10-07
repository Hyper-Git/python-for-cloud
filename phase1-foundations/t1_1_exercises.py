instance_id = "i-0abc123def"
instance_type = "t3.micro"
number_of_vcpus = 2
hourly_cost_in_dollars = 0.0118
running = True
monthly_cost = hourly_cost_in_dollars * 730 

print(f"{instance_id} ({instance_type}): {number_of_vcpus} vCPUs, ${hourly_cost_in_dollars}/hour, running: {running}")
print(f"Monthly cost: ${monthly_cost}")
print(type(monthly_cost))
print(f"Monthly cost: ${monthly_cost:.2f}")
