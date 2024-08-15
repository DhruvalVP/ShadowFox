# If you cross a 490 meterlong street in 7 minutes, calculate your speed in meters per second. Print the answer without any decimal point in it. Hint: Speed = Distance / Time

street_len = 490    # meter
time_taken = 7  # minutes
min_1 = 60 # 1 minute = 60 seconds

time_taken = time_taken * min_1

speed = int(street_len/time_taken)  # calculate speed to integer value

print(f"Speed is {speed} meters per second.")