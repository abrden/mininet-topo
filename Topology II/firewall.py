'''
Coursera :
- Software Defined Networking ( SDN ) course
-- Programming Assignment : Layer -2 Firewall Application
Professor : Nick Feamster
Teaching Assistant : Arpit Gupta
'''

from pox.core import core
import pox.openflow.libopenflow_01 as of
from pox.lib.revent import *
from pox.lib.util import dpidToStr
from pox.lib.addresses import EthAddr
from collections import namedtuple
import os
''' Add your imports here ... '''
import pox.lib.packet as pkt

log = core.getLogger ()

''' Add your global variables here ... '''
rules = [['00:00:00:00:00:01', '00:00:00:00:00:03']]

class Firewall(EventMixin):

	def __init__(self):
		self.listenTo(core.openflow)
		log.debug("Enabling Firewall Module")
		
	def _handle_ConnectionUp(self, event):
		for rule in rules:
			block = of.ofp_match()
			block.dl_src = EthAddr(rule[0])
			block.dl_dst = EthAddr(rule[1])
			flow_mod = of.ofp_flow_mod()
			flow_mod.match = block
			event.connection.send(flow_mod)

	def _handle_PacketIn (self, event):
		packet = event.parsed
		if packet.type == packet.ARP_TYPE:
			log.debug(packet)
			log.debug('Blocked!')
			event.halt = True

def launch():
	'''
	Starting the Firewall module
	'''
	core.registerNew(Firewall)
