from scrolley.func import Scroller
import sys

def main():
    s = Scroller("""abcde""")
    # while True:
    print(s.scroll(0.1))
    # print(s.create_platform(), end="\r")
    # print(s.create_platform(), end="\r")
    # sys.stdout.write(s.create_platform())
    # # print(s.__split__())
    # scroll("my name is chigozie. How has your day been. Good i hope", 1)
    # s.scroll(1)

if __name__ == "__main__":
    main()