import random

def generate_target():
    a = random.randint(0, 255)
    b = random.randint(0, 255)
    c = random.randint(0, 255)
    d = random.randint(0, 255)
    return f"{a}.{b}.{c}.{d}"

if __name__ == "__main__":
    for i in range(5):
        print(generate_target())
