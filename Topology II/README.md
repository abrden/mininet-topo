## Linear topology with firewall

This folder contains a linear topology of S switches plus a custom firewall with built-in rules.

To run the sample please run `./setup.sh SWITCHES` where `SWITCHES` is the number of switches in the topology. (Eg. `./setup.sh 3`)

### Firewall

The firewall has the following built-in rules:
- Hosts 1 and 3 (h0 and h2) cant communicate between each other
- ICMP packets with port destionation 80 will be blocked
- UDP Packets with port destination 5001 in host 1 will be blocked

### Use-Cases

#### Hosts h0 and h2 uncommunicated

```
mininet> pingall
mininet> h0 ping h2
mininet> h2 ping h1
```

#### ICMP Packets with port destination 80

```
mininet> h0 python -m SimpleHTTPServer 80 &
mininet> h3 wget -O - h0
```

#### UDP Packets with port destination 5001 (default) in h1

```
mininet> xterm h1 h2
# Server / UDP / Interval for bandwith 1 / Port
mininet Node h1> iperf -s -u -i 1 -p 5001
# Client / UDP / Bandwidth / Number of bytes to transport / Port
mininet Node h2> iperf -c 10.0.0.1 -u -b 1m -n 1000 -p 5001
```
