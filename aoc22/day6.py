#!/usr/bin/env python3

def get_marker(datastream_buffer, window_size):
    for i in range(0, len(datastream_buffer) - window_size - 1):
        if len(set(datastream_buffer[i:i+window_size])) == window_size:
            return i+window_size


def main():

    f = open("inputs/day6.txt", "r")
    datastream_buffer = f.read()

    test_strings = ["mjqjpqmgbljsphdztnvjfqwrcgsmlb",
                    "bvwbjplbgvbhsrlpgdmjqwftvncz",
                    "nppdvjthqldpwncqszvftbrmjlhg",
                    "nznrnfrfntjfmvfwmzdfjlvtqnbhcprsg",
                    "zcfzfwzzqfrljwzlrfnpqdbhtmscgvjw"
                    ]

    for datastream in test_strings:
        print(datastream)
        print(f"Start of packet: {get_marker(datastream, 4)}")
        print(f"Start of message: {get_marker(datastream, 14)}\n")

    print(datastream_buffer)
    print(f"Start of packet: {get_marker(datastream_buffer, 4)}")
    print(f"Start of message: {get_marker(datastream_buffer, 14)}\n")


if __name__ == "__main__":
    main()
