#!/bin/bash

chmod u+x my_ep.py
./my_ep.py -a entrada
./my_ep.py -u entrada
chmod u+x my_ep_test.py
./my_ep_test.py a_output
./my_ep_test.py u_output