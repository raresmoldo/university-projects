import random 

def interpolation_search(arr, x):
    low, high = 0, len(arr) - 1
    while low <= high and x >= arr[low] and x <= arr[high]:
        if low == high:
            return low if arr[low] == x else -1
        pos = low + ((x - arr[low]) * (high - low) // (arr[high] - arr[low]))
        if arr[pos] == x:
            return pos
        elif arr[pos] < x:
            low = pos + 1
        else:
            high = pos - 1
    return -1
def is_sorted(arr):
    return all(arr[i] <= arr[i+1] for i in range(len(arr)-1))
def bogo_sort(arr, step):
    arr = arr[:]
    operations = 0
    while not is_sorted(arr):
        random.shuffle(arr)
        operations += 1
        if operations % step == 0:
            print(f"After {operations} shuffle(s): {arr}")
    return arr


def heapify(arr, n, i, operations, step):
    largest = i
    left = 2 * i + 1
    right = 2 * i + 2

    if left < n and arr[left] > arr[largest]:
        largest = left
    if right < n and arr[right] > arr[largest]:
        largest = right

    if largest != i:
        arr[i], arr[largest] = arr[largest], arr[i]
        operations[0] += 1
        if operations[0] % step == 0:
            print(f"After {operations[0]} swap(s): {arr}")
        heapify(arr, n, largest, operations, step)


def heap_sort(arr, step):
    arr = arr[:]
    n = len(arr)
    operations = [0]
    for i in range(n//2 - 1, -1, -1):
        heapify(arr, n, i, operations, step)

    for i in range(n-1, 0, -1):
        arr[i], arr[0] = arr[0], arr[i]
        operations[0] += 1
        if operations[0] % step == 0 or is_sorted(arr):
            print(f"After {operations[0]} swap(s): {arr}")
        heapify(arr, i, 0, operations, step)
    return arr
def main():
    arr = []
    is_list_sorted = False

    while True:
        print("\n=== MENU ===")
        print("1. Generate list")
        print("2. Bogo Sort")
        print("3. Heap Sort")
        print("4. Interpolation Search")
        print("5. Exit")
        
        choice = input("Choose an option: ")

        if choice == "1":
            n = int(input("Enter list size: "))
            arr = [random.randint(0, 1000) for _ in range(n)]
            print(f"Generated list: {arr}")
            is_list_sorted = False

        elif choice == "2":
            if not arr:
                print("You need to generate a list first.")
                continue
            step = int(input("Enter step interval: "))
            arr = bogo_sort(arr, step)
            print(f"Final sorted list: {arr}")
            is_list_sorted = True

        elif choice == "3":
            if not arr:
                print("You need to generate a list first.")
                continue
            step = int(input("Enter step interval: "))
            arr = heap_sort(arr, step)
            print(f"Final sorted list: {arr}")
            is_list_sorted = True
            
        elif choice == "4":
            if not arr:
                print("You need to generate a list first.")
                continue
            if not is_list_sorted:
                print("You must sort the list before searching.")
                continue
            x = int(input("Enter number to search: "))
            idx = interpolation_search(arr, x)
            if idx != -1:
                print(f"Found {x} at index {idx}")
            else:
                print(f"{x} not found in the list.")

        elif choice == "5":
            print("Exiting program...")
            break

        else:
            print("Invalid choice, please try again.")

if __name__ == "__main__":
    main()
