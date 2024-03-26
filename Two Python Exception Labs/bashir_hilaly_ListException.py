"""
----------------------------------------------------
-- CMPSC_132, Spring 2024, Bashir Hilaly
-- Lab 2 – Detecting integer exception
----------------------------------------------------
"""

def main():
    names = ['Ryley', 'Edan', 'Reagan', 'Henry', 'Caius', 'Jane', 'Guto', 'Sonya', 'Tyrese', 'Johnny']
    index = int(input('Index: '))
    try:
        print(names[index])
    except IndexError as e:
        if index > len(names):
            print(f'Exception! {e}\nthe closest name is: {names[-1]}')
        if index < -1*len(names):
            print(f'Exception! {e}\nthe closest name is: {names[0]}')

if __name__ == '__main__':
    main()