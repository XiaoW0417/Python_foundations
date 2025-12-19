import sys

def main():
    print("Hello from python-foundations!")

    print(f"full list: {sys.argv}")

    print(f"script_name: {sys.argv[0]}")

    if len(sys.argv) > 1:
        print("You have passed extra args")
        print(f"arg_1:{sys.argv[1]}")
    else:
        print("No extra arg")



if __name__ == "__main__":
    main()
