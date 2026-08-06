import sys, os
class fileDelete:
    def deleteFileContent(self):
        path = os.path.abspath(os.path.dirname(sys.argv[0]))
        open(path + '/host/host.txt', 'w').close()
        open(path + '/host/up_host.txt', 'w').close()
        open(path + '/host/vuln_host.txt', 'w').close()
        print("[+] Host lists cleared")
