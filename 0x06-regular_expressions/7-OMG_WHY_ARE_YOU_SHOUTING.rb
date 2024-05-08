#!/usr/bin/env ruby
# This script accepts one argument and passes it to a regular expression,

puts ARGV[0].scan(/(?<=from:|to:|flags:).+?(?=\])/).join(',')
