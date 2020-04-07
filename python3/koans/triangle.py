#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Triangle Project Code.

# Triangle analyzes the lengths of the sides of a triangle
# (represented by a, b and c) and returns the type of triangle.
#
# It returns:
#   'equilateral'  if all sides are equal
#   'isosceles'    if exactly 2 sides are equal
#   'scalene'      if no sides are equal
#
# The tests for this method can be found in
#   about_triangle_project.py
# and
#   about_triangle_project_2.py
#
def triangle(*sides):
    if any(s <= 0 for s in sides):
        raise TriangleError

    ordered = sorted(sides)
    if ordered[0] + ordered[1] <= ordered[2]:
        raise TriangleError

    l = len(set(sides))
    if (l == 1):
        return 'equilateral'
    elif (l == 2):
        return 'isosceles'
    else:
        return 'scalene'

# Error class used in part 2.  No need to change this code.
class TriangleError(Exception):
    pass
