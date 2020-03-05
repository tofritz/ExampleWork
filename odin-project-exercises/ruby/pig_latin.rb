#write your code here
def translate s
    result = []
    s.split.map do |word|
        case word
        when /^[aeiou]/ then result << word + 'ay'
        when /^([^aeiou])([qu]+)(.*)$/ then result << $3 + $1 + $2 + 'ay'
        when /^([^aeiou]+)(.*)$/ then result << $2 + $1 + 'ay'
        end
    end
    result.join(' ')
end