def largest_prime_factor number
    if number < 1  
        puts 'enter a number greater than 1' 
    end
    factors = [1, ]
    while number % 2 == 0
        factors.push(2)
        number /= 2
    end
    for i in (3..Math.sqrt(number)).step(2) do
        while number % i == 0
            factors.push(i)
            number /= i
        end
    end
    factors
end

puts largest_prime_factor(600851475143).last
