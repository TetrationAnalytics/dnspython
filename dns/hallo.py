import dns.resolver


def hallo_world():

    resolver = dns.resolver.Resolver()
    response = resolver.query("cisco.com", "A")
    print ("Hallo World from cisco.com on ", str(response[0]))
