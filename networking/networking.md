## Networking
Every system you'll work with communicates over a network. When a deployment fails, an API won't respond, or a container can't reach a database — the problem is usually networking. You need to understand it well enough to diagnose problems and talk to people who fix them.

## IP Addresses
Every device on a network has an IP address — a unique identifier that tells traffic where to go. Like a postal address for your machine.

IPv4 — `192.168.1.1` — four numbers 0-255 separated by dots. Still dominant.
IPv6 — `2001:0db8:85a3::8a2e:0370:7334` — newer and longer, exists because we ran out of IPv4 addresses.

Public IP — visible on the internet, assigned by your ISP. Your router has one.
Private IP — only visible inside your local network. Your laptop is probably something like `192.168.1.x` or `10.0.0.x`.

## DNS
DNS (Domain Name System) translates human-readable domain names into IP addresses. When you type `google.com`, your computer asks a DNS server which replies with an IP like `142.250.187.206`. Your computer then connects to that IP. Without it you'd have to memorise IP addresses for every website.

The process when you visit `google.com` — browser checks local cache, then asks your router, then your ISP's DNS server, then works up the chain to a root DNS server until it gets an IP back.

## Ports
An IP address gets traffic to the right machine. A port gets it to the right application on that machine. The IP is the building, the port is the room number.

| Port | Protocol | Use |
|------|----------|-----|
| 80 | HTTP | Unencrypted web traffic |
| 443 | HTTPS | Encrypted web traffic |
| 22 | SSH | Secure shell access |
| 5432 | PostgreSQL | Database |
| 3306 | MySQL | Database |
| 6379 | Redis | Cache |
| 8080 | HTTP alt | Common for local dev servers |

In DevOps you'll constantly be opening ports in firewalls, mapping ports in Docker, and checking why something can't reach a service on a specific port.

## HTTP and HTTPS
HTTP is the protocol browsers and servers use to communicate. HTTPS is HTTP with encryption via TLS — data is encrypted in transit so nobody can intercept it. In 2026 everything should be HTTPS.

Request methods:
- `GET` — retrieve something
- `POST` — send data to create something
- `PUT` — update something
- `DELETE` — remove something

Status codes you'll read constantly in logs and API responses:
- `200` — OK, success
- `201` — Created
- `301` — Moved permanently
- `400` — Bad request — you sent something wrong
- `401` — Unauthorised — you need to log in
- `403` — Forbidden — logged in but no permission
- `404` — Not found
- `500` — Internal server error — something broke on the server

## Localhost
`localhost` is your own machine. IP `127.0.0.1` always refers to yourself. When you run a local development server you access it at `localhost:8000` — the port after the colon is which application on your machine you're talking to.

## Client and Server
Client — makes requests. Your browser, a Python script calling an API, a mobile app.
Server — listens for requests and responds. A web server, an API, a database.

The same machine can be both. When you run a FastAPI app locally, your laptop is the server and your browser is the client.

## APIs
An API (Application Programming Interface) is a defined way for two systems to talk to each other over HTTP. Instead of a human visiting a webpage, a program sends a request and gets structured data back — usually JSON. Weather apps, payment systems, GitHub, AWS — all exposed via APIs.

## Diagnostic Commands

`ping` tests basic connectivity to a host. Sends packets and measures response time. Use it to quickly check "can this server reach that server at all."
```bash
ping google.com -c 4
```
The output shows the IP DNS resolved the domain to, sequence numbers confirming packets arrived in order, round trip time in ms, and packet loss. 0% packet loss means the connection is healthy.

`curl` makes an HTTP request from the terminal. Use it to test APIs, check responses, and see exactly what a request looks like to a server.
```bash
curl https://httpbin.org/get
```
The response shows your request reflected back — headers your request carried, your public IP in `origin`, and the User-Agent showing what made the request. When you make an HTTP request you're not just sending a URL — you're sending headers, a method, potentially a body, and the server sees all of it.

`nslookup` looks up what IP addresses are registered for a domain in DNS. Large services like Google return multiple IPs so traffic can be distributed across servers — this is called DNS-based load balancing.
```bash
nslookup google.com
```
`127.0.0.53` in the output is your local DNS resolver — your machine's first stop before going out to the internet.

`traceroute` shows every hop your traffic takes to reach a destination. A hop is each router or device your traffic passes through. Useful for finding exactly where in the chain a connection is failing.
```bash
traceroute google.com
```
`* * *` means that device didn't respond to traceroute — many routers block it by default for security. It doesn't mean failure. If ping succeeds but traceroute goes silent after a few hops, those routers are just silent — the traffic is still getting through.