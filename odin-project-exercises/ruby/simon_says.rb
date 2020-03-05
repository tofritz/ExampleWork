#write your code here
def echo string
    string
end

def shout string
    string.upcase
end

def repeat string, num = 2
    result = ''
    num.times do
        result += string + ' '
    end
    result.rstrip
end

def start_of_word string, index
    string[0..(index - 1)]
end

def first_word string
    string.partition(' ')[0]
end

def titleize string
    ignore = ['and', 'or', 'the', 'a', 'of', 'over']
    words = string.split
    words.each { |word| word.capitalize! unless ignore.include?(word) }
    words.first.capitalize!
    words.join(' ')
end
