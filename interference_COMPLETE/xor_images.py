#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author: john
# @Date:   2017-03-08 02:36:35
# @Last Modified by:   john
# @Last Modified time: 2017-03-08 02:52:11

from PIL import Image
import sys

if len(sys.argv) != 4:
	print "usage: ./xor_images.py <image1> <image1> <output>"
	exit()


image1 = Image.open(sys.argv[1])
image2 = Image.open(sys.argv[2])
image1 = image1.convert('RGB')


image1.convert('RGB')
w, h = image1.size

new_image = Image.new('RGBA', image1.size)
one = image1.load()
two = image2.load()
new = new_image.load()

for x in range(w):
	for y in range(h):


		new[x, y] =  tuple(( one[x, y][i] ^ two[x, y][i] for i in range(3) ))

new_image.save(sys.argv[3])