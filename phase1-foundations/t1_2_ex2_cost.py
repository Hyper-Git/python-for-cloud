# Monthly instance cost calculator 
instance_type = input("What is the instance type: ")
instance_hourly_cost = float(input("What is the hourly cost for the instance: "))
number_of_instances = int(input("How many instances you want to run: "))
instance_monthly_cost = instance_hourly_cost * number_of_instances * 730

print(f"{number_of_instances} x {instance_type} for one month: ${instance_monthly_cost:.2f}")
