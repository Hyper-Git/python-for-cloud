#Business problem : a team wants to keeep application in S3 for compliance. 
#Finance asks, “How much data will we be storing, 
# and what will it cost a month?”
logs_per_day = float(input("What is the amount of logs produced per day in GB: "))
retention_in_days = int(input("How long the logs are kept: "))
total_stored = logs_per_day * retention_in_days
s3_price_per_gb = 0.024
monthly_s3_cost = total_stored * s3_price_per_gb

print("Retention: " + str(retention_in_days) + " days")
print(f"Stored logs: {total_stored:.1f} GB")
print(f"Monthly S3 cost: ${monthly_s3_cost:.2f}")


