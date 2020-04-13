from netaddr import IPNetwork


def main():
    network = input('Enter a network: ')

    ip = IPNetwork(network)
    print(f"The network is: {ip.network}\n"
          f"The broadcast is: {ip.broadcast}\n"
          f"The first usable address is: {ip[1]}\n"
          f"The last usable address is: {ip[-2]}\n"
          f"Network is private: {ip.is_private()}")


if __name__ == "__main__":
    main()
