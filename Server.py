#Ping found at https://stackoverflow.com/questions/2953462/pinging-servers-in-python

class Server:
    """ Server class for representing and manipulating servers. """

    def __init__(self, server_ip):
        # TODO -
        self.server_ip = server_ip

    def ping(self):
        # TODO - Use os module to ping the server
        import os
        host_ip = self.server_ip # example
        response = os.system("ping " + host_ip)