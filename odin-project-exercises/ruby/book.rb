class Book
    attr_reader :title
    def title=(string)
        ignore = ['and', 'or', 'the', 'a', 'of', 'over', 'in', 'an']
        words = string.split
        words.each { |word| word.capitalize! unless ignore.include?(word) }
        words.first.capitalize!
        @title = words.join(' ')
    end
end