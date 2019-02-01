#! /bin/bash
source /home/cquest/.virtualenvs/granddebile/bin/activate
twitter set "$(python granddebile.py)"
