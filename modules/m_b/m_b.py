import sys


class ModuleB:
    def __init__(self, sdk):
        self.sdk = sdk

    def print_hello(self):
        print("Hello from Module B")

    def print_token(self):
        print(sys.modules["__main__"].YUNHU_TOKEN)
