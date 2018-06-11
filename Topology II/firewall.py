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
		packet = event.parsed.find('ipv4')
		if not packet: return
		if packet.protocol != pkt.ipv4.ICMP_PROTOCOL and packet.payload.dstport == 80:
			log.debug(packet)
			log.debug('Blocked ICMP packet with destinationPort = 80!')
			event.halt = True
		elif packet.protocol == pkt.ipv4.UDP_PROTOCOL and packet.payload.dstport == 5001:		
			eth_packet = event.parsed
			host_1 = '00:00:00:00:00:02'
			addr = EthAddr(host_1)
			if eth_packet.src == addr:
				log.debug(packet)
				log.debug('Blocked udp datagram with destination port of 5001 coming from host 1!')
				event.halt = True
				
def launch():
	'''
	Starting the Firewall module
	'''
	log.debug('Launching')
	core.registerNew(Firewall)
