import sys
sys.path.append(".")

from mininet.topo import Topo
from switch import get_switch_amount
from mininet.log import setLogLevel 
import math

class MyTopo(Topo):

	def __init__ (self, hosts, levels):
		# setLogLevel('debug')
		self.my_hosts_number = hosts
		self.my_switches_number = get_switch_amount(levels)
		self.my_hosts = []
		self.my_switches = []
		print self.my_hosts_number
		print self.my_switches_number
		
		# Initialize topology
		Topo.__init__(self)
		# Create switch
		# s1 = self.addSwitch('switch_1')
		self.create_switches()
		# Create hosts
		# h1 = self.addHost('host_1')
		# h2 = self.addHost('host_2')
		self.create_hosts()
		# Add links between switches and hosts
		# self.addLink(s1, s2)
		# self.addLink(s1, h1)
		# self.addLink(s1, h2)
		# self.addLink(s2, h3)
		# self.addLink(s2, h4)

	def create_hosts(self):
		hname = 'host_'
		for i in xrange(self.my_hosts_number):
			self.my_hosts.append(self.addHost(hname + str(i)))

	def create_switches(self):
		swname = 'switch_'
		for i in xrange(self.my_switches_number):
			self.my_switches.append(self.addSwitch(swname + str(i)))

	def create_links(self):
		return

topos = { 'customTopo': MyTopo }
