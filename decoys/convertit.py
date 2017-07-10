#!/usr/bin/python

import os

files = ["zinc_10160738",
         "zinc_1016",
         "zinc_19571488",
         "zinc_3028",
         "zinc_32101",
         "zinc_666",
         "zinc_72436953",
         "zinc_7710",
         "zinc_9015347",
         "zinc_95076007"]

for line in files:
  command = "babel -isdf "+line+".sdf -opdb "+line+".pdb "
  os.system(command)


