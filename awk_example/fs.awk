#!/usr/bin/env awk -f
# fs.awk
BEGIN {
  FS = ",";
}

/96\// {
  print $1, $3;
}