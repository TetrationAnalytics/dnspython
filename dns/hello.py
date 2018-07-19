import dns.resolver


def hello_world():

    resolver = dns.resolver.Resolver()
    response = resolver.query("cisco.com", "A")
    print ("Hello World from cisco.com on ", str(response[0]))
