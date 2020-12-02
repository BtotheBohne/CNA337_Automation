# This is the template code for the CNA337 Final Project
# Zachary Rubin, zrubin@rtc.edu
# CNA 337 Fall 2020

def print_program_info():
    # TODO - Change your name
    print("Server Automator v0.1 by Ben Bohnen")

# This is the entry point to our program
# How to enable inbound ping AWS https://stackoverflow.com/questions/21981796/cannot-ping-aws-ec2-instance
if __name__ == '__main__':
    print_program_info()
    # TODO - Create a Server object
    import Server
    server1 = Server.Server("3.21.231.7")
    # TODO - Call Ping method and print the result
    print(server1.ping())