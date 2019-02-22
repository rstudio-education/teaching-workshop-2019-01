#!/usr/bin/env python

import sys

for filename in sys.argv[1:]:
    with open(filename, 'r') as reader:
        data = reader.read()
    with open(filename, 'w') as writer:
        writer.write(data)
