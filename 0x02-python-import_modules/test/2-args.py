#!/usr/bin/python3
if __name__ == "__main__":
    import sys

    argv = sys.argv[1:]
    num_arguments = len(argv)

    print(f"{num_arguments} argument{'s' if num_arguments != 1 else ''}:")
    for i, arg in enumerate(argv, start=1):
        print(f"{i}: {arg}")
