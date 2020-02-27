def sum_multiples_3_5 number
    sum = 0
    for i in 0..(number - 1)
        if i % 3 == 0 || i % 5 == 0
            sum += i
        end
    end
    return sum
end

puts sum_multiples_3_5(1000)