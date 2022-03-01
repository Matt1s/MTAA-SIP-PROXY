import sipfullproxy as SIP
import socket
def main():
    # moved these 2 variables as they are no longer needed in sipfullproxy.py file
    HOST = '0.0.0.0'
    PORT = 5060

    # edited filename
    SIP.logging.basicConfig(format='%(asctime)s:%(levelname)s:%(message)s',filename='zaznam.log',level=SIP.logging.INFO,datefmt='%H:%M:%S')
    SIP.logging.info(SIP.time.strftime("%a, %d %b %Y %H:%M:%S ", SIP.time.localtime()))

    #selecting specific IP address
    ipaddress = socket.gethostbyname_ex(socket.gethostname())[2][0]
    if ipaddress == "127.0.0.1":
        ipaddress = SIP.sys.argv[1]
    SIP.logging.info(ipaddress)
    SIP.recordroute = "Record-Route: <sip:%s:%d;lr>" % (ipaddress,PORT)
    SIP.topvia = "Via: SIP/2.0/UDP %s:%d" % (ipaddress,PORT)

    # setting up server
    server = SIP.socketserver.UDPServer((HOST, PORT), SIP.UDPHandler)
    try:
        print('Server starting at ' + ipaddress) 
        server.serve_forever()
    except:
        server.server_close()
        print('Server stopped, closing program...')
main()