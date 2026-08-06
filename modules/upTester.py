import os, sys, socket
from concurrent.futures import ThreadPoolExecutor, as_completed
from host import host


class upTester:
    def _isUp(address):
        try:
            with socket.create_connection((address['ip'], address['port']), timeout=5) as client:
                client.sendall(b"GET /HTTP/1.1\r\nhost: google.com\r\n\r\n")
                client.recv(4096)
            return True
        except OSError:
            return False

    def Tcp(self):
        print("[+]Loading all host...")
        path = os.path.abspath(os.path.dirname(sys.argv[0]))
        lines = open(path + '/host/host.txt', 'r').read().splitlines()
        addresses = []
        for line in lines:
            if not line.strip():
                continue
            try:
                addresses.append(host.Host.addressRegex(line))
            except AttributeError:
                continue
        total = len(addresses)
        upHosts = []
        try:
            with ThreadPoolExecutor(max_workers=50) as executor:
                futures = {executor.submit(upTester._isUp, address): address for address in addresses}
                done = 0
                for future in as_completed(futures):
                    done += 1
                    percentage = (done / total) * 100 if total else 100
                    progressBar = int(percentage) / 5
                    sys.stdout.write("\r" + "[...] Loading   [%-20s] %.2f%%" % ('█' * int(progressBar), percentage))
                    sys.stdout.flush()
                    if future.result():
                        address = futures[future]
                        upHosts.append(address['ip'] + ":" + str(address['port']))
        except KeyboardInterrupt:
            print("\n[---]exiting now[---]")
        finally:
            sys.stdout.write("\r" + "[!!!] Complete [%-20s] %.2f%%\n" % ('█' * 20, 100.00))
            if upHosts:
                with open(path + '/host/up_host.txt', "a") as host_up:
                    host_up.write("\n".join(upHosts) + "\n")
