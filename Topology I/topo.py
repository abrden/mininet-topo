from mininet.topo import Topo
from mininet.log import setLogLevel 
import math

def get_switch_amount(switch_level):
	sum = math.pow(2, switch_level - 1)
	while (0 < switch_level - 1):
		sum += math.pow(2, switch_level - 1)
		switch_level -= 1
	return sum

class MyTopo(Topo):

	def __init__ (self, hosts, levels):
		# setLogLevel('debug')
		self.levels = levels
		self.my_hosts_number = hosts
		self.my_switches_number = int(get_switch_amount(self.levels))
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
		self.create_links()
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
		# Hosts linking
		middle = int(math.ceil(len(self.my_hosts) / 2.0))
		for i, host in enumerate(self.my_hosts):
			if i < middle:
				self.addLink(self.my_switches[0], host)
			else:
				self.addLink(self.my_switches[-1], host)

		# Switch linking
		self._link_switches(self.levels, 0, 0)

	def _link_switches(self, level, root, child):
		if level == 1:
			return
		self.addLink(self.my_switches[0 + root], self.my_switches[1 + child])
		self.addLink(self.my_switches[0 + root], self.my_switches[2 + child])
		for i in xrange(1, level):
			self._link_switches(level - 1, i, child + i * 2)
		self.addLink(self.my_switches[-1 - root], self.my_switches[-2 - child])
		self.addLink(self.my_switches[-1 - root], self.my_switches[-3 - child])

	
	
	
	
	
	# def _link_switches2(self, s0, s1, s2):
	# 	if s0 > self.my_switches_number:
	# 		return
	# 	self.addLink(self.my_switches[s0], self.my_switches[s1])
	# 	self.addLink(self.my_switches[s0], self.my_switches[s2])

	# 	_link_switches(s1, s2 + 1, s2 + 2)
	# 	_link_switches(s2, s2 + 3, s2 + 4)

	# 	# Nivel 2
	# 	self.addLink(self.my_switches[0], self.my_switches[1])
	# 	self.addLink(self.my_switches[0], self.my_switches[2])

	# 	self.addLink(self.my_switches[1], self.my_switches[3])
	# 	self.addLink(self.my_switches[2], self.my_switches[3])		
		
	# 	# Nivel 3
	# 	self.addLink(self.my_switches[0], self.my_switches[1])
	# 	self.addLink(self.my_switches[0], self.my_switches[2])

	# 	self.addLink(self.my_switches[1], self.my_switches[3])	
	# 	self.addLink(self.my_switches[1], self.my_switches[4])
		
	# 	self.addLink(self.my_switches[2], self.my_switches[5])	
	# 	self.addLink(self.my_switches[2], self.my_switches[6])

	# 	self.addLink(self.my_switches[3], self.my_switches[7])	
	# 	self.addLink(self.my_switches[4], self.my_switches[7])

	# 	self.addLink(self.my_switches[5], self.my_switches[8])	
	# 	self.addLink(self.my_switches[6], self.my_switches[8])

	# 	self.addLink(self.my_switches[7], self.my_switches[9])	
	# 	self.addLink(self.my_switches[8], self.my_switches[9])
			



topos = { 'customTopo': MyTopo }
