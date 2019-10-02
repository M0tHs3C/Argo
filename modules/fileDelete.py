import sys, os
class fileDelete:
    def deleteFileContent(self):
        path = os.path.abspath(os.path.dirname(sys.argv[0]))
        open(path + '/Host/host.txt', 'w')
        open(path + '/Host/up_host.txt', 'w')
        open(path + '/Host/vuln_host.txt', 'w')


