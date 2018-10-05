#!/bin/bash

ltrace -s 1024 ./412108f24d79f657ca3ff30fdf436ffa73d1e14a5d9ea0de63e917b8c1dc1528_flagcheck `python -c "print 'a'*43"` 2>&1|grep "strcmp"|cut -d '"' -f2
