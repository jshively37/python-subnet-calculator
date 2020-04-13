from netaddr import IPNetwork


def main():
    program_run = True

    while program_run is True:
        network = input('Enter a network or q to exit: ')
        if network.lower() == 'q':
            print('Exiting program')
            program_run = False
        else:
            try:
                ip = IPNetwork(network)
                print(f"The network is: {ip.network}\n"
                      f"The broadcast is: {ip.broadcast}\n"
                      f"The first usable address is: {ip[1]}\n"
                      f"The last usable address is: {ip[-2]}\n"
                      f"Network is private: {ip.is_private()}")
            except:
                print(f"{network} is not a valid network.\n"
                      f"Allowed format are:\n"
                      f"network/cidr (192.168.1.1/24)\n"
                      f"network/subnet (192.168.1.1/255.255.255.0)")


if __name__ == "__main__":
    main()
