# possible to use scapy for the scanning purposes
# need to take in user input from the command line so use sys module (sys.argv)
# sys.argv splits based on the space delimiter
# create logic to pull up the interactive console if no inputs are given (or may just be the base case)
'''
General Logic (MVP):
1. call script from command line with ip & ports want to scan
1a. have capability where user can input -p & -i for indicating ip and port
1ab. look for -i index & -p index & increment +1 to get the corresponding value

2. if correct input supplied then conduct scan by crafting scapy syn packet and sending to ip:port
2a. if incorrect input, trigger fail route

3. If syn-ack gotten back then save port state as 'open'
3a. else save port state as closed, if rst gotten back save as 'filtered'

4. Print to console the following:
    1) which ip was scanned
    2) which ports were opened/filtered/closed
'''

'''
Enhancements:
1. Possibly build interactive console
2. Build functionality to include different scan types and based on the input, craft a specific scapy packet for it
3. possibly call another function to do something else to the data after it's been received.
4. add in a possibility to save to a specific location in the system (use context function "with" to write into a file)
'''