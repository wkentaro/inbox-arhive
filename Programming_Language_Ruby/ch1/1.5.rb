x = 1
p x

x, y = 1, 2
p x
p y

y, x = x, y
p x
p y

def polar(x,y)
  theta = Math.atan2(y,x)  # angle
  r = Math.hypot(x,y)      # distance
  [r, theta]
end

distance, angle = polar(2, 2)