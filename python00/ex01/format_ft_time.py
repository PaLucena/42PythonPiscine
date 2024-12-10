from datetime import datetime
import time

curr_time = time.time()
seconds_time = f"{curr_time:,.4f}"
cientf_time = f"{curr_time:.2e}"

curr_time = datetime.now()
format_time = curr_time.strftime("%b %d %Y")

print(f"Seconds since January 1, 1970: {seconds_time} or {cientf_time} in scientific notation")
print(format_time)
