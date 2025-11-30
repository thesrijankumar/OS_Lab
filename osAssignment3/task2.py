def best_fit(block_size, process_size):
    allocation = [-1] * len(process_size)

    for i in range(len(process_size)):
        best_index = -1
        for j in range(len(block_size)):
            if block_size[j] >= process_size[i]:
                if best_index == -1 or block_size[j] < block_size[best_index]:
                    best_index = j

        if best_index != -1:
            allocation[i] = best_index
            block_size[best_index] -= process_size[i]

    print("\n=== BEST FIT ALLOCATION ===")
    print("Process No.\tProcess Size\tBlock No.")
    for i in range(len(process_size)):
        block = allocation[i] + 1 if allocation[i] != -1 else "Not Allocated"
        print(f"{i+1}\t\t{process_size[i]}\t\t{block}")


def worst_fit(block_size, process_size):
    allocation = [-1] * len(process_size)

    for i in range(len(process_size)):
        worst_index = -1
        for j in range(len(block_size)):
            if block_size[j] >= process_size[i]:
                if worst_index == -1 or block_size[j] > block_size[worst_index]:
                    worst_index = j

        if worst_index != -1:
            allocation[i] = worst_index
            block_size[worst_index] -= process_size[i]

    print("\n=== WORST FIT ALLOCATION ===")
    print("Process No.\tProcess Size\tBlock No.")
    for i in range(len(process_size)):
        block = allocation[i] + 1 if allocation[i] != -1 else "Not Allocated"
        print(f"{i+1}\t\t{process_size[i]}\t\t{block}")


if __name__ == "__main__":
    block_size = [100, 500, 200, 300, 600]
    process_size = [212, 417, 112, 426]

    print("Initial Block Sizes:", block_size)
    print("Process Sizes:", process_size)

    best_fit(block_size.copy(), process_size)
    worst_fit(block_size.copy(), process_size)
