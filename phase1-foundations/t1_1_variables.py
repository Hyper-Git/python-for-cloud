job_id = "YRK-0142"
customer = "Mrs Patel"
units = 14
worktop_metres = 6.4
deposit_paid = True

print(job_id)
print(type(units))
print(type(worktop_metres))
print(type(deposit_paid))
print(type("14"))

units_text = "14"

print(units + 1) 
print(units_text + "1")
print(f"Job {job_id} for {customer}: {units} units, {worktop_metres}m of worktop")
# This line charashes on purpose : str + int raises a TypeError
#print(units_text + 1)
