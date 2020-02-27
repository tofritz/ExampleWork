def grandfather_clock some_proc
    current_hour = Time.now.hour
    if current_hour == 0
        current_hour += 12
    elsif current_hour > 12
        current_hour -= 12
    end
    current_hour.times {some_proc.call}
end

dong = Proc.new do
    puts "DONG!"
end

grandfather_clock dong