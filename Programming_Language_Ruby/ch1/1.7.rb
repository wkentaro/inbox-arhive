def are_you_sure?
  while true
    print "Are you sure? [y/n]: "
    response = gets
    case response
    when /^[yY]/
      return true
    else
      return false
    end
  end
end

if are_you_sure?
  print "doing dangerous thing!!\n"
  sleep 3
  print "done!!!\n"
else
  print "aborted!!!!\n"
end