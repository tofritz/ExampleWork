class Timer
  
  attr_accessor :seconds

  def initialize
    @seconds = 0
  end

  def time_string
    hours = @seconds / 3600
    s_rem = @seconds % 3600
    padded(hours) + ':' + padded(s_rem / 60) + ':' + padded(s_rem % 60)
  end

  def padded(num)
    '%02i' % num
  end

end