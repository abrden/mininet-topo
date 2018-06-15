#!/bin/bash

# $1 = #Hosts
# $2 = #Switches

# We send pox to another pid
./pox/pox.py samples.spanning_tree &

# We notify the user what we will do
echo "About to run mininet with $1 hosts and $2 level of switches"
echo "Please consider running a 'pingall' command to check its status"

# Run mininet
sudo mn --custom topo.py --topo customTopo,$1,$2 --controller remote --arp --mac --switch ovsk
