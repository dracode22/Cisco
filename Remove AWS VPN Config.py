from ciscoconfparse import CiscoConfParse

cisco_file = 'Router.txt'

cisco_cfg = CiscoConfParse(cisco_file)

all_ints = cisco_cfg.find_objects(r"^interface")
all_preflists = cisco_cfg.find_objects(r"^ip prefix-list")
all_rtmps = cisco_cfg.find_objects(r"^route-map")

VRF_LIST = ["Default"]

AWS_INTF = list()
IPSEC_PROF = str()

for VRF in VRF_LIST:
    print
    print "!############## REMOVING ALL CONFIG RELATED TO  VRF [- " + VRF + " -]#############"
    for int in all_ints:
        pattern = r"forwarding.*" + VRF
        if int.re_search_children(pattern) and int.re_search_children(r"ipsec profile") and \
                int.re_search_children(r"shutdown"):
            print "!--->Removing VRF parameters used on interface " + int.text
            print "!"
            print int.text
            print "no tunnel protection ipsec profile ipsec" + int.children[9].text.strip(
                'tunnel protection ipsec profile\s')
            print "exit"
            print "no crypto isakmp profile isakmp" + int.children[9].text.strip('tunnel protection ipsec profile\s')
            print "no crypto keyring keyring" + int.children[9].text.strip(
                'tunnel protection ipsec profile\s') + " vrf " + VRF
            print "no crypto ipsec profile ipsec" + int.children[9].text.strip('tunnel protection ipsec profile\s')
            print "no crypto ipsec transform-set ipsec-prop" + int.children[9].text.strip(
                'tunnel protection ipsec profile\s')
            print "!"
            print "!--->Parameters removed for " + int.text
            print "\n"
        elif int.re_search_children(pattern) and int.re_search_children(r"ipsec profile"):
            print "!--->Removing VRF parameters used on interface " + int.text
            print "!"
            print int.text
            print "no tunnel protection ipsec profile ipsec" + int.children[8].text.strip(
                'tunnel protection ipsec profile\s')
            print "exit"
            print "no crypto isakmp profile isakmp" + int.children[8].text.strip('tunnel protection ipsec profile\s')
            print "no crypto keyring keyring" + int.children[8].text.strip(
                'tunnel protection ipsec profile\s') + " vrf " + VRF
            print "no crypto ipsec profile ipsec" + int.children[8].text.strip('tunnel protection ipsec profile\s')
            print "no crypto ipsec transform-set ipsec-prop" + int.children[8].text.strip(
                'tunnel protection ipsec profile\s')
            print "!"
            print "!--->Parameters removed for " + int.text
            print "\n"

        if int.re_search_children(pattern):
            print "!--->removing " + int.text
            print "!"
            print "no " + int.text
            print "!"
            print "!--->interface removed " + int.text
            print "\n"

    for VRF2 in cisco_cfg.find_objects(r"^ip vrf"):
        if VRF == VRF2.text.strip('ip vrf'):
            print "!--->Removing address family for VRF " + VRF
            print "!"
            print "router bgp 65xxx"
            print "no address-family ipv4 vrf " + VRF
            print "!"
            print "!--->Address family removed for VRF " + VRF
            print "\n"

            print "!--->Removing actual VRF for " + VRF
            print "!"
            print "no ip vrf " + VRF
            print "!"
            print "!--->VRF removed " + VRF
            print "\n"

            print "!--->removing route-map used in VRF " + VRF
            for rtmap in all_rtmps:
                pattern = r"" + VRF
                if rtmap.re_search(pattern):
                    print "no " + rtmap.text

            print "!--->Route-map  removed " + VRF
            print "\n"

            print "!--->removing Prefix-List used in VRF " + VRF
            print "!"
            for preflist in all_preflists:
                pattern = r"" + VRF
                if preflist.re_search(pattern):
                    print "no " + preflist.text
            print "!"
            print "!--->Prefix_list  removed " + VRF
            print "\n"
    print "!##############ALL CONFIG RELATED TO VRF [- " + VRF + " -] REMOVED #############"
    print "\n"
