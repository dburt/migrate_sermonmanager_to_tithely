#!/usr/bin/env ruby

require 'json'
require 'csv'

data = JSON.parse(ARGF.read)

fields = data.map(&:keys).flatten.uniq

CSV(STDOUT) do |csv|
  csv << fields
  data.each do |record|
    csv << fields.map {|field| record[field] }
  end
end
