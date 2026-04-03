servers = ['web-01', 'web-02', 'web-03', 'web-04', 'web-05']   # list of strings — in real DevOps this might come from an API or config file

for server in servers:                          # for loop iterates over the list, each pass assigns the next item to 'server'
    print(f"Checking server: {server}")         # f-string lets us insert the current server name into the message each iteration

for i in range(5, 0, -1):                       # range(start, stop, step) — starts at 5, stops before 0, counts down by 1 each step
    print(i)                                    # prints 5, 4, 3, 2, 1 — the stop value (0) is excluded, same as a countdown timer
print("Done")                                   # outside the loop (no indent) so it only runs once after the loop finishes

while True:                                     # infinite loop — runs forever until something inside explicitly breaks it
    answer = input("Type a server name: ")      # re-runs every iteration, asking for fresh input each time
    if answer == "exit":                        # the only escape — checks if the user typed the exit keyword
        print("Goodbye")
        break                                   # break exits the while loop immediately, without it the loop would never stop