def even_fibonacci_sum limit
    sum = 0
    previous_num = 1
    num = 2
    while num <= limit
        if num.even?
            sum += num
        end
        new_num = num + previous_num
        previous_num = num
        num = new_num
    end
    sum
end

puts even_fibonacci_sum(4_000_000)