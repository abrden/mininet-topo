#!/bin/bash

# We copy our own firewall impl into the pox samples
sudo cp firewall.py pox/pox/samples/firewall_impl.py

# Run pox in another pid. Using our firewall impl
./pox/pox.py samples.firewall_impl forwarding.l2_learning &

# We notify the user what we will do
echo "About to run mininet with $1 switches"
echo "Please consider running a 'pingall' command to check its status"

# Run mininet
sudo mn sudo mn --custom topo.py --topo customTopo,$1 --controller remote --arp --mac --switch ovsk
