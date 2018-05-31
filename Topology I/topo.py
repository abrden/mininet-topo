import sys
sys.path.append(".")

from mininet.topo import Topo
from switch import get_switch_amount
from mininet.log import setLogLevel 
import math

class MyTopo(Topo):

	def __init__ (self, hosts, levels):
		# setLogLevel('debug')
		self.levels = levels
		self.my_hosts_number = hosts
		self.my_switches_number = get_switch_amount(self.levels)
		self.my_hosts = []
		self.my_switches = []

		# Initialize topology
		Topo.__init__(self)
		# Create switch
		self.create_switches()
		# Create hosts
		self.create_hosts()
		# Add links between switches and hosts
		self.create_links()

	def create_hosts(self):
		hname = 'host_'
		for i in xrange(self.my_hosts_number):
			self.my_hosts.append(self.addHost(hname + str(i)))

	def create_switches(self):
		swname = 'switch_'
		for i in xrange(self.my_switches_number):
			self.my_switches.append(self.addSwitch(swname + str(i)))

	def create_links(self):
		# Hosts linking
		middle = int(math.ceil(len(self.my_hosts) / 2.0))
		for i, host in enumerate(self.my_hosts):
			if i < middle:
				self.addLink(self.my_switches[0], host)
			else:
				self.addLink(self.my_switches[-1], host)

		# Switch linking
		self._link_switches(self.levels, 0, 0)

	def _link_switches(self, level, root_offset, child_offset):
		if level == 1:
			return
		self.addLink(self.my_switches[0 + root_offset], self.my_switches[1 + child_offset])
		self.addLink(self.my_switches[0 + root_offset], self.my_switches[2 + child_offset])
		for i in xrange(1, level):
			self._link_switches(level - 1, i, child_offset + i * 2)
		self.addLink(self.my_switches[-1 - root_offset], self.my_switches[-2 - child_offset])
		self.addLink(self.my_switches[-1 - root_offset], self.my_switches[-3 - child_offset])			


topos = { 'customTopo': MyTopo }
