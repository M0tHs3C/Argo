from socket import error as socket_error
import re,os,sys,socket
from host import host
class upTester:
    def Tcp(self):
        print("[+]Loading all host...")
        path = os.path.abspath(os.path.dirname(sys.argv[0]))
        hosts = open(path + '/host/host.txt', 'r').read().splitlines()
        a = 0
        try:
            while a < len(hosts):
                res = hosts[a]
                address = host.Host.addressRegex(res)
                try:
                    percentage = (a / len(hosts)) * 100
                    progressBar = int(percentage)/5
                    sys.stdout.write("\r"+ "[...] Loading   [%-20s] %.2f%%" % ('█' * int(progressBar),  percentage))
                    sys.stdout.flush()
                    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                    client.settimeout(5)
                    client.connect((address['ip'],address['port']))
                    client.sendall(b"GET /HTTP/1.1\r\nhost: google.com\r\n\r\n")
                    response = client.recv(4096)
                    x = True
                except socket_error:
                    x = False
                except KeyboardInterrupt:
                    print ("\n[---]exiting now[---]")
                if x == True:
                    with open(path + '/host/up_host.txt', "a") as host_up:
                        host_up.write(address['ip'] + ":" + str(address['port']) + "\n")
                elif x == False:
                    pass
                a += 1
        except KeyboardInterrupt:
            print ("\n[---]exiting now[---]")
        except AttributeError:
            pass
        finally:
            sys.stdout.write("\r" + "[!!!] Complete [%-20s] %.2f%%" % ('█' * 20, 100.00))