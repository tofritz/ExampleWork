#write your code here
def add a, b
    a + b
end

def subtract a, b
    a - b
end

def sum array
    sum = 0
    array.each {|x| sum += x}
    sum
end

def multiply *nums
    prod = 1
    nums.each { |n| prod *= n }
    prod
end

def power a, b
    a ** b
end

def factorial a
    prod = 1
    a.downto(1) { |n| prod *= n }
    prod
end