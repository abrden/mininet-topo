from mininet.topo import Topo
from mininet.log import setLogLevel 
import math

HOSTS_NUMBER = 4

class MyTopo(Topo):

	def __init__ (self, switches):
		# setLogLevel('debug')
		self.my_hosts_number = HOSTS_NUMBER
		self.my_switches_number = switches
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
		hname = 'h'
		for i in xrange(self.my_hosts_number):
			self.my_hosts.append(self.addHost(hname + str(i)))

	def create_switches(self):
		swname = 's'
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

		# Switchs linking
		for i in xrange(self.my_switches_number - 1):
			self.addLink(self.my_switches[i], self.my_switches[i + 1])


topos = { 'customTopo': MyTopo }
