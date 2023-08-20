#!/usr/bin/python3

def practice():
    switch = dict(
            first = 'single',
            second = 'twins',
            third = 'triplets',
            fourth = 'quadruplets'
    )

    position = 'fourth'
    print(switch.get(position, "Does not exist"))

if __name__ == "__main__": practice()
