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