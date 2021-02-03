import sys, os
class fileDelete:
    def deleteFileContent(self):
        path = os.path.abspath(os.path.dirname(sys.argv[0]))
        open(path + '/host/host.txt', 'w')
        open(path + '/host/up_host.txt', 'w')
        open(path + '/host/vuln_host.txt', 'w')


