servers = ['web-01', 'web-02', 'web-03', 'web-04', 'web-05']
print(servers[0])
print(servers[-1])
servers.append('web-06')
print(f"Added 'web-06': {servers}")
servers.remove('web-02')
print(f"Removed 'web-02': {servers}")

if 'web-01' in servers:
    print("Server present.")
else: 
    print("Server absent.")

for server in servers:
    print(f"Checking {server}")