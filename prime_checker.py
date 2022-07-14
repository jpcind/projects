def prime_checker(num):
    if num == 1 or num == 0 or num < 0:
        return False
    for i in range(2, num):
        if num % i == 0:
            return False
    return True

def main():
    print(prime_checker(7))

if __name__ == '__main__':
    main()
