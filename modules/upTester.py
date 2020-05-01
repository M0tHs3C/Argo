from socket import error as socket_error
import re,os,sys,socket

class upTester:
    def Tcp(self):
        print("[+]Loading all host...")
        path = os.path.abspath(os.path.dirname(sys.argv[0]))
        host = open(path + '/Host/host.txt', 'r').read().splitlines()
        a = 0
        try:
            while a < len(host):
                pattern_1 = r'\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}'
                pattern_2 = r'(\:).*'
                res = host[a]
                match1 = re.search(pattern_1, res)
                match2 = re.search(pattern_2, res)
                target_host = match1.group()
                port_raw = match2.group()
                port = port_raw[1:]
                try:
                    percentage = (a / len(host)) * 100
                    progressBar = int(percentage)/5
                    sys.stdout.write("\r"+ "[%-20s] %.2f%%" % ('█' * int(progressBar),  percentage))
                    sys.stdout.flush()
                    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                    client.settimeout(5)
                    client.connect((target_host, int(port)))
                    client.sendall(b"GET /HTTP/1.1\r\nHost: google.com\r\n\r\n")
                    response = client.recv(4096)
                    x = True
                except socket_error:
                    x = False
                except KeyboardInterrupt:
                    print ("\n[---]exiting now[---]")
                if x == True:
                    with open(path + '/Host/up_host.txt', "a") as host_up:
                        host_up.write(target_host + ":" + port + "\n")
                elif x == False:
                    pass

                a += 1
        except KeyboardInterrupt:
            print ("\n[---]exiting now[---]")
        except AttributeError:
            pass
        finally:
            sys.stdout.write("\r" + "[%-20s] %.2f%%" % ('█' * 20, 100.00))