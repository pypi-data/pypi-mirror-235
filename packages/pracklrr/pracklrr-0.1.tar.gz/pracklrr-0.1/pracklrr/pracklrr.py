class Pracklrr:
    def avail_prog():
        avail_lx = r"""
        1. menu()
        
        2. ping2_cisco()
        
        3. dhcp()
        
        4. multi_switch()
        
        5. multicast()
        
        6. data_trans()
        
        7. calc_packet()
        
        
        """
        return avail_lx
    def menu():
        od = r"""
	clear
	cont=1
	while [ $cont -eq 1 ]
	do
	echo "NETWORK COMMANDS USING SHELL SCRIPT"
	echo "----------------------------------"
	echo "1.ping"
	echo "2.hostname"
	echo "3.route"
	echo "4.host"
	echo "5.netstat"
	echo "6.nslookup"
	echo "7.host version number"
	echo "8.finish"
	echo "Enter Your Option"
	read a
	case $a in 
	1)echo "ping"
	ping ww.google.com;;
	2)echo "hostname"
	hostname;;
	3)echo "route"
	route;;
	4)echo "host"
	host www.amazon.com;;
	5)echo "netstat"
	netstat -r;;
	6)echo "nslookup"
	nslookup www.google.com;;
	7)echo "host version number"
	host -v;;
	8)echo "successfully completed"
	exit;;
	esac;
	done
        
        """
        return od
        
    def ping2_cisco():
        ten = r""" 
	ping 192.168.0.1 -Second PC CMD PROMPT
	ping 192.168.0.2 -First PC CMD PROMPT
        """
        return ten
    def dhcp():
       ma = r"""
	"FIRST SWITCH CONNCETION"
	no
	en
	conf t
	int fa0/0
	ip address 192.168.0.1 255.255.255.0
	no shutdown
	do write memory
	ip dhcp pool net1
	network 192.168.0.1 255.255.255.0
	exit

	"SECOND SWICH CONNECTION"
	int fa0/1
	ip address 192.168.1.1 255.255.255.0
	no shutdown
	do write memory
	ip dhcp pool net2
	network 192.168.1.1 255.255.255.0
	exit

       """
       return ma
       
    def multi_switch():
        cp = r""" 
	enable
	configure terminal
	vlan 10
	name VLAN10
	vlan 20
	name VLAN20
	vlan 30
	name VLAN30
	end

	configure terminal
	interface FastEthernet0/1
	switchport mode access
	switchport access vlan 10
	interface FastEthernet0/2
	switchport mode access
	switchport access vlan 20
	interface FastEthernet0/3
	switchport mode access
	switchport access vlan 30
	end

	configure terminal
	interface vlan 10
	ip address 192.168.10.1 255.255.255.0
	interface vlan 20
	ip address 192.168.20.1 255.255.255.0
	interface vlan 30
	ip address 192.168.30.1 255.255.255.0
	end

	Configure Default Gateway on PCs:
	Configure the IP addresses and default gateways on each PC as follows:
	PC1: IP Address: 192.168.10.2, Default Gateway: 192.168.10.1
	PC2: IP Address: 192.168.20.2, Default Gateway: 192.168.20.1
	PC3: IP Address: 192.168.30.2, Default Gateway: 192.168.30.1

	conf t
	ip routing
        """
        return cp
        
    def multicast():
          sc = r""" 
	   MULTICAST NETWORKS USING NS2 (WIRED)

		set ns [new Simulator -multicast on] ;# enable multicast routing
		set trace [open test19.tr w]
		$ns trace-all $trace
		#$ns use-newtrace
		set namtrace [open test19.nam w]
		$ns namtrace-all $namtrace
		set group [Node allocaddr] ;# allocate a multicast address
		set node0 [$ns node] ;# create multicast capable nodes
		set node1 [$ns node]
		set node2 [$ns node]
		$ns duplex-link $node0 $node1 1.5Mb 10ms DropTail
		$ns duplex-link $node0 $node2 1.5Mb 10ms DropTail
		set mproto DM ;# configure multicast protocol
		set mrthandle [$ns mrtproto $mproto] ;# all nodes will contain multicast protocol agents
		set udp [new Agent/UDP] ;# create a source agent at node 0
		$ns attach-agent $node0 $udp
		set src [new Application/Traffic/CBR]
		$src attach-agent $udp
		$udp set dst_addr_ $group
		$udp set dst_port_ 0
		set rcvr [new Agent/LossMonitor] ;# create a receiver agent at node 1
		$ns attach-agent $node1 $rcvr
		$ns at 0.3 "$node1 join-group $rcvr $group" ;# join the group at simulation time 0.3 (sec)
		set rcvr2 [new Agent/LossMonitor] ;# create a receiver agent at node 1
		$ns attach-agent $node2 $rcvr2
		$ns at 0.3 "$node2 join-group $rcvr2 $group" ;# join the group at simulation time 0.3 (sec)
		$ns at 3.3 "$node2 leave-group $rcvr2 $group" ;# join the group at simulation time 0.3 (sec)
		$ns at 2.0 "$src start"
		$ns at 5.0 "$src stop"
		proc finish {} {
		global ns namtrace trace
		$ns flush-trace
		close $namtrace ; close $trace
		exec nam test19.nam &
		exit 0
		}
		$ns at 10.0 "finish"
		$ns run	
		
		
		
		Ns execution command 

		ns nsfilename.tcl

		Nam file display command 

		export DISPLAY="$(hostname).local:0"
		
		ns nsfilename.tcl
     
         """
          return sc
         
    def data_trans():
          ex_fam = r""" 
		set val(chan) Channel/WirelessChannel ;# channel type
		set val(prop) Propagation/TwoRayGround ;# radio-propagation model
		set val(netif) Phy/WirelessPhy ;# network interface type
		set val(mac) Mac/802_11 ;# MAC type
		set val(ifq) Queue/DropTail/PriQueue ;# interface queue type
		set val(ll) LL ;# link layer type
		set val(ant) Antenna/OmniAntenna ;# antenna model
		set val(ifqlen) 50 ;# max packet in ifq
		set val(nn) 2 ;# number of mobilenodes
		set val(rp) DSDV ;# routing protocol
		set val(x) 827 ;# X dimension of topography
		set val(y) 438 ;# Y dimension of topography
		set val(stop) 10.0 ;# time of simulation end
		set ns [new Simulator]
		set topo [new Topography]
		$topo load_flatgrid $val(x) $val(y)
		create-god $val(nn)
		set tracefile [open in.tr w]
		$ns trace-all $tracefile
		set namfile [open in.nam w]
		$ns namtrace-all $namfile
		$ns namtrace-all-wireless $namfile $val(x) $val(y)
		set chan [new $val(chan)];#Create wireless channel
		$ns node-config -adhocRouting $val(rp) \
		-llType $val(ll) \
		-macType $val(mac) \
		-ifqType $val(ifq) \
		-ifqLen $val(ifqlen) \
		-antType $val(ant) \
		-propType $val(prop) \
		-phyType $val(netif) \
		-channel $chan \
		-topoInstance $topo \
		-agentTrace ON \
		-routerTrace ON \
		-macTrace ON \
		-movementTrace ON
		set n0 [$ns node]
		$n0 set X_ 523
		$n0 set Y_ 338
		$n0 set Z_ 0.0
		$ns initial_node_pos $n0 20
		set n1 [$ns node]
		$n1 set X_ 727
		$n1 set Y_ 335
		$n1 set Z_ 0.0
		$ns initial_node_pos $n1 20
		set tcp0 [new Agent/TCP]
		$ns attach-agent $n0 $tcp0
		set sink1 [new Agent/TCPSink]
		$ns attach-agent $n1 $sink1
		$ns connect $tcp0 $sink1
		$tcp0 set packetSize_ 1500
		set ftp0 [new Application/FTP]
		$ftp0 attach-agent $tcp0
		$ns at 1.0 "$ftp0 start"
		$ns at 2.0 "$ftp0 stop"
		proc finish {} {
		global ns tracefile namfile
		$ns flush-trace
		close $tracefile
		close $namfile
		exec nam in.nam &
		exit 0
		}
		for {set i 0} {$i < $val(nn) } { incr i } {
		$ns at $val(stop) "\$n$i reset"
		}
		$ns at $val(stop) "$ns nam-end-wireless $val(stop)"
		$ns at $val(stop) "finish"
		$ns at $val(stop) "puts \"done\" ; $ns halt"
		$ns run
		
		
		Ns execution command--

		ns nsfilename.tcl

		Nam file display command--

		export DISPLAY="$(hostname).local:0"
		
		ns nsfilename.tcl
		
		
          """
          return ex_fam   
    def calc_packet():
          cld = r""" 
		set val(chan) Channel/WirelessChannel ;# channel type
		set val(prop) Propagation/TwoRayGround ;# radio-propagation model
		set val(netif) Phy/WirelessPhy ;# network interface type
		set val(mac) Mac/802_11 ;# MAC type
		set val(ifq) Queue/DropTail/PriQueue ;# interface queue type
		set val(ll) LL ;# link layer type
		set val(ant) Antenna/OmniAntenna ;# antenna model
		set val(ifqlen) 50 ;# max packet in ifq
		set val(nn) 2 ;# number of mobilenodes
		set val(rp) AODV ;# routing protocol
		set val(x) 827 ;# X dimension of topography
		set val(y) 438 ;# Y dimension of topography
		set val(stop) 10.0 ;# time of simulation end
		set ns [new Simulator]
		set topo [new Topography]
		$topo load_flatgrid $val(x) $val(y)
		create-god $val(nn)
		set tracefile [open in.tr w]
		$ns trace-all $tracefile
		set namfile [open out.nam w]
		$ns namtrace-all $namfile
		$ns namtrace-all-wireless $namfile $val(x) $val(y)
		set chan [new $val(chan)];#Create wireless channel
		$ns node-config -adhocRouting $val(rp) \
		-llType $val(ll) \
		-macType $val(mac) \
		-ifqType $val(ifq) \
		-ifqLen $val(ifqlen) \
		-antType $val(ant) \
		-propType $val(prop) \
		-phyType $val(netif) \
		-channel $chan \
		-topoInstance $topo \
		-agentTrace ON \
		-routerTrace ON \
		-macTrace ON \
		-movementTrace ON
		set n0 [$ns node]    
		$n0 set X_ 523
		$n0 set Y_ 338
		$n0 set Z_ 0.0
		$ns initial_node_pos $n0 20
		set n1 [$ns node]
		$n1 set X_ 727
		$n1 set Y_ 335
		$n1 set Z_ 0.0
		$ns initial_node_pos $n1 20
		set tcp0 [new Agent/TCP]
		$ns attach-agent $n0 $tcp0
		set sink1 [new Agent/TCPSink]
		$ns attach-agent $n1 $sink1

		$ns connect $tcp0 $sink1
		$tcp0 set packetSize_ 1500
		set ftp0 [new Application/FTP]
		$ftp0 attach-agent $tcp0
		$ns at 1.0 "$ftp0 start"
		$ns at 2.0 "$ftp0 stop"
		proc finish {} {
		global ns tracefile namfile
		$ns flush-trace
		close $tracefile
		close $namfile
		exec nam out.nam &
		exit 0
		}
		for {set i 0} {$i<$val(nn) } { incr i } {
		$ns at $val(stop) "\$n$i reset"
		}
		$ns at $val(stop) "$ns nam-end-wireless $val(stop)"
		$ns at $val(stop) "finish"
		$ns at $val(stop) "puts \"done\" ; $ns halt"
		$ns run

		 
		AWK FILE
		
		
		BEGIN {
		sent=0;
		received=0;
		pdr = 0;
		}
		{
		if($1=="r"&& ($4 == "AGT" || $4 == "MAC" ||$4 == "RTR"))
		{
		received++;
		}
		if($1=="s"&& ($4 == "AGT" || $4 == "RTR" || $4 == "MAC"))
		{
		sent++;
		}
		}
		END{
		pdr = (received/sent)*100;
		printf "\n To calculate PDR using AODV Protocol\n";
		printf "\n Packet Sent:%d",sent;
		printf "\n Packet Received:%d",received;
		printf "\n Packet Delivery Ratio:%.2f%%\n",pdr;
		}
		
		
		Ns execution command --

		ns nsfilename.tcl

		Nam file display command --

		export DISPLAY="$(hostname).local:0"
		
		ns nsfilename.tcl
		
		
		awk -f awkfilename.awk in.tr
		
          """
          return cld

