def newline
  print "\n"
end

3.times { print "Ruby! " }

newline # ---------------------

1.upto(9) {|x| print x }

newline # ---------------------

a = [3, 2, 1]
a[3] = a[2] - 1
a.each do |elt|
  print elt+1
end

newline # ---------------------

a = [1,2,3,4]
b = a.map {|x| x*x }
c = a.select {|x| x%2==0 }
p a
p b
p c

newline # ---------------------

# a.inject do |sum,x|
#   sum + x
# end
p a.inject {|sum, n| sum + n}

newline # ---------------------

h = {
  :one => 1,
  :two => 2,
}
p h[:one]
h[:three] = 3
p h
h.each do |key, value|
  print "#{value}:#{key}; "
end

newline # ---------------------

x,y = 1001,999
minimum = if x < y then x else y end
p minimum