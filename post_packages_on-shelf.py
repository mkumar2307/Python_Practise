'''
N clients are waiting in line to collect their package at post office. Package arrives at the post office one by one. for simplicity we will number the packages from 1 to N in order in which they arrive. Each client wants to collect a single package, the K-th client in the line (for K from 0 to N-1) wants to collect package number client[K].
After a package arrives one of the following events happens:   If the first client in the line wants to collect the package they pick it up and leave the line; Otherwise the package is put on the shelf.
If the first client wants to collect a package from the shelf they will leave the line and collect package. please note only the first client from the line can collect their package. How many packages will be stored on the shelf at the same time?
write a function : def solution(client)
which gives an array client returns the maximum number of packages that will be sorted on the shelf at same time.
'''

def solution(clients):
    packages_on_shelf = set()
    max_packages_on_shelf = 0

    for i, package in enumerate(clients):
        packages_on_shelf.add(package)

        # Check if the first client in line can collect the package
        if min(packages_on_shelf) == i + 1:
            packages_on_shelf.remove(i + 1)

        # Check if any other clients can collect a package from the shelf
        for j in range(i + 1, len(clients)):
            if clients[j] in packages_on_shelf:
                packages_on_shelf.remove(clients[j])

        max_packages_on_shelf = max(max_packages_on_shelf, len(packages_on_shelf))

    return max_packages_on_shelf
clients = [3, 2, 4, 5, 1]
print(solution(clients))

clients = [1, 2, 3, 4, 5]
print(solution(clients))

clients = [3, 2, 7, 5, 4, 1, 6]
print(solution(clients))