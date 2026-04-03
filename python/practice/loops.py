servers = ['web-01', 'web-02', 'web-03', 'web-04', 'web-05']

for server in servers:
    print(f"Checking server: {server}")
for i in range(5, 0, -1):
    print(i) 
print("Done")

while True:
    answer = input("Type a server name: ")
    if answer == "exit":
        print("Goodbye")
        break