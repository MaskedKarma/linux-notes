## Networking
A network is how computers communicate with each other. When a deployment fails, an API won't respond, or a container can't reach a database — the problem is usually networking. You need to understand it well enough to diagnose problems and talk to people who fix them.

## IP Addresses
An IP address is a unique identifier that tells traffic where to go on a network. Like a postal address for your machine.

IPv4 — `192.168.1.1` — four numbers 0–255 separated by dots. Still dominant.
IPv6 — `2001:0db8:85a3::8a2e:0370:7334` — newer and longer, exists because we ran out of IPv4 addresses.

Public IP — visible on the internet, assigned by your ISP. Your router has one.
Private IP — only visible inside your local network. Your laptop is probably something like `192.168.1.x` or `10.0.0.x`.

## DNS
DNS (Domain Name System) translates human-readable domain names into IP addresses. When you type `google.com` your computer asks a DNS server, which replies with an IP like `142.250.187.206`. Your computer then connects to that IP. Without it you'd have to memorise IP addresses for every website.

DNS only ever resolves the domain — `youtube.com`. Everything after it (`/watch?v=abc123`) is a path, handled by the server after the connection is made. DNS never sees it.

The full resolution chain when the answer isn't cached — browser local cache, local DNS resolver (`127.0.0.53` on Linux), router, ISP's recursive resolver, root nameservers, TLD nameservers (`.com`, `.org`), authoritative nameserver (the domain owner's own DNS), IP returned. Most of the time the answer is cached early in that chain and the full journey never happens.

## DNS Records
When a company registers a domain they create records on their nameserver pointing it at their servers.
```
A record     — maps a domain to an IPv4 address.   google.com → 142.250.187.206
AAAA record  — maps a domain to an IPv6 address
CNAME record — maps a domain to another domain.    www.google.com → google.com
MX record    — mail server for the domain
TXT record   — arbitrary text, used for verification and security
```
Subdomains are separate DNS records. `mail.google.com` and `google.com` point at different servers — same registrar, separate records. When you deploy something to AWS you'll create A records pointing your domain at your server's IP.

## Ports
An IP address gets traffic to the right machine. A port gets it to the right application on that machine. The IP is the building, the port is the room number.
```
80    HTTP        Unencrypted web traffic
443   HTTPS       Encrypted web traffic
22    SSH         Secure shell access
5432  PostgreSQL  Database
3306  MySQL       Database
6379  Redis       Cache
8080  HTTP alt    Common for local dev servers
```
In DevOps you'll constantly be opening ports in firewalls, mapping ports in Docker, and checking why something can't reach a service on a specific port.

## HTTP and HTTPS
HTTP is the protocol browsers and servers use to communicate. HTTPS is HTTP with encryption via TLS — data is encrypted in transit so nobody can intercept it. In 2026 everything should be HTTPS.

Request methods — `GET` retrieves something, `POST` sends data to create something, `PUT` updates something, `DELETE` removes something.

Status codes you'll read constantly in logs and API responses.
```
200   OK — success
201   Created
301   Moved permanently
400   Bad request — you sent something wrong
401   Unauthorised — you need to log in
403   Forbidden — logged in but no permission
404   Not found
500   Internal server error — something broke on the server
```

## HTTP Requests
When your browser makes a request it sends more than just a URL — it sends headers, a method, and sometimes a body. The server sees all of it.
```
GET /watch?v=abc123 HTTP/1.1
Host: youtube.com
User-Agent: Mozilla/5.0 ...
Accept: text/html
Cookie: [your session token]
```
`Host` — which domain you're requesting. One server can host many domains. `User-Agent` — identifies your browser and OS. `Cookie` — if you're logged in, your session token lives here. This is how the server knows who you are.

## What Happens When You Visit a URL
Typing `https://youtube.com/watch?v=abc123` and pressing enter triggers this entire sequence.

1. URL parsed into scheme (`https`), domain (`youtube.com`), path (`/watch`), query string (`?v=abc123`).
2. DNS resolves `youtube.com` to an IP.
3. TCP handshake — both sides confirm they're ready before any data flows. SYN → SYN-ACK → ACK.
4. TLS handshake — server sends its SSL certificate, browser validates it against trusted Certificate Authorities, both sides agree on a session key. Everything from here is encrypted.
5. HTTP request sent — browser asks for `/watch?v=abc123` with headers and cookies attached.
6. Packets routed across the internet — data travels as small chunks through multiple routers. TCP reassembles them in order using sequence numbers.
7. Load balancer receives the request — distributes traffic across many servers so no single one gets overwhelmed.
8. Server processes the request — reads the path, queries a database, checks your login cookie, builds a response.
9. HTTP response returned — status code, headers, and the HTML body.
10. Browser parses HTML — finds CSS, JavaScript, images. Each new domain triggers its own DNS lookup. JavaScript runs and may make further API calls returning JSON.
11. Page rendered. All of that in under a second on a fast connection.

## Localhost
`localhost` is your own machine. IP `127.0.0.1` always refers to yourself. When you run a local development server you access it at `localhost:8000` — the port after the colon is which application on your machine you're talking to.

## Client and Server
Client — makes requests. Your browser, a Python script calling an API, a mobile app. Server — listens for requests and responds. A web server, an API, a database. The same machine can be both. When you run a FastAPI app locally, your laptop is the server and your browser is the client.

## APIs
An API (Application Programming Interface) is a defined way for two systems to talk to each other over HTTP. Instead of a human visiting a webpage, a program sends a request and gets structured data back — usually JSON. Weather apps, payment systems, GitHub, AWS — all exposed via APIs.

## Diagnostic Commands
`ping` tests basic connectivity. Sends packets to a host and measures response time. Use it to check "can this machine reach that machine at all."
```bash
ping google.com -c 4
```
`curl` makes an HTTP request from the terminal. Use it to test APIs and see exactly what a request and response look like.
```bash
curl https://httpbin.org/get
```
`nslookup` looks up what IP addresses are registered for a domain. Large services return multiple IPs so traffic can be spread across servers — DNS-based load balancing.
```bash
nslookup google.com
```
`traceroute` shows every hop your traffic takes to reach a destination. Use it to find where in the chain a connection is failing. `* * *` means that router didn't respond — common and not a problem on its own. If ping succeeds but traceroute goes silent, the traffic is still getting through.
```bash
traceroute google.com
```