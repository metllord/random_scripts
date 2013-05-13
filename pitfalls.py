#!local/bin/python
#-*- coding: utf-8 -*-

# Don't do this in Python


def mutable_list(var=[]):
    """ This takes a list for a default argument. Var should be local to the function. Since lists
    are mutable and a bit quirky in python, the global new_var gets appended to."""
    var.append('Wrong')
    print var

new_var = ['Previous']
mutable_list(new_var)

print new_var  # new_var should not change.
