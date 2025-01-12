import time
# IMP
for i in range(1, 6):
    print(f"Processing: {i}", end="\r")  # Overwrite the same line
    time.sleep(1)  # Wait for 1 second

print("Done!")  # Final message
# IMP