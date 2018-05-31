import sys
sys.path.append(".")

from mininet.topo import Topo
from switch import get_switch_amount
import math

class MyTopo(Topo):

	def __init__ (self, hosts, levels):
		self.hosts_number = hosts
		self.switches_number = get_switch_amount(levels)
		self.hosts = []
		self.switches = []
		print hosts
		print levels
		# Initialize topology
		Topo.__init__(self)
		# Create switch
		self.create_switches()
		# Create hosts
		self.create_hosts()
		# Add links between switches and hosts
		self.addLink(s1, s2)
		self.addLink(s1, h1)
		self.addLink(s1, h2)
		self.addLink(s2, h3)
		self.addLink(s2, h4)

	def create_hosts(self):
		hname = 'host_'
		for i in xrange(self.hosts_number):
			self.hosts.append(self.addHost(hname + i))

	def create_switches(self):
		swname = 'switch_'
		for i in xrange(self.switches_number):
			self.switches.append(self.addSwitch(swname + i))

	def create_links(self):
		return

topos = { 'customTopo': MyTopo }
