#!/usr/bin/env ruby
log = ARGV[0]
#Define the regular expression pattern to match sender, receiver, and flags

pattern = /\[from:(.*?)\].*?\[to:(.*?)\].*?\[flags:(.*?)\]/

#Match the pattern in the log
match = log.match(pattern)

if match
  sender = match[1]
  receiver = match[2]
  flags = match[3]
  puts "#{sender},#{receiver},#{flags}"
else
  puts "No match found in the log."
end
#
