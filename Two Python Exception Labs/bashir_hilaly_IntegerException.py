"""
----------------------------------------------------
-- CMPSC_132, Spring 2024, Bashir Hilaly
-- Lab 1 – Detecting integer exception
----------------------------------------------------
"""


def main():
    parts = input().split()
    name = parts[0]
    output = []
    while name != '-1':
        # FIXME: The following line will throw ValueError exception.
        # Insert try/except blocks to catch the exception.
        try:
            age = int(parts[1]) + 1
            output.append(f'{name} {age}')
        except ValueError:
            output.append(f'{name} 0')
        # Get next line
        parts = input().split()
        name = parts[0]

    for name in output:
        print(name)


if __name__ == '__main__':
    main()