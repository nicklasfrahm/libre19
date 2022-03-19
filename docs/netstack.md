# Network stack 📡

One part of the project is a network stack, which provides a top of rack L3 router, network switches and power. Below, you may find a list of all final components and a picture of the current state.

- [x] Rack mount chassis
  - [x] Appliance layout and size constraints
  - [x] Compatibility concept with 10-inch half-rack
  - [ ] Splitting into 3D-printable components
- [x] Power supply
  - [x] Compatibile with [YOUMILE AC-DC 12V6A][amazon-psu-youmile] or [ANGEEK AC-DC 12V6A][amazon-psu-angeek]
  - [ ] Case for **DIY AC-DC 12V5A** power supply
  - [ ] Case for **X115-Y65-Z40** power supplies
- [ ] Network switches
  - [ ] Compatibility with TP-LINK SG108E and NETGEAR GS308E
  - [ ] Case for any 8-port switch
- [ ] Chassis management
  - [ ] Schematic for WT32-ETH01
  - [ ] [Veroboard][wikipedia-veroboard] layout
  - [ ] Firmware for WT32-ETH01
  - [ ] Case for chassis management unit
- [x] Router and firewall
  - [x] Traffic management via [nftables][wiki-nftables]
  - [ ] Case for [Seeed compute module router][seeed-cm4router]

![Network stack CAD preview][img-netstack]

[img-netstack]: ./netstack_v0_assembly.png
