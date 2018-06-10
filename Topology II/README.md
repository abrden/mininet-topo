## Linear topology with firewall

This folder contains a linear topology of S switches plus a custom firewall with built-in rules.

To run the sample please run `./setup.sh SWITCHES` where `SWITCHES` is the number of switches in the topology. (Eg. `./setup.sh 3`)

### Firewall

The firewall has the following built-in rules:
- Hosts 1 and 3 cant communicate between each other
- ICMP packets with port destionation 80 will be blocked
- UDP Packets with port destination 5001 coming from the host 1 will be blocked
