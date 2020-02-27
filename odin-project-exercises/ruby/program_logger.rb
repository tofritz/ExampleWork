def log description_of_block, &block
    puts 'Beginning "' + description_of_block + '"'
    returned = block.call
    puts '..."' + description_of_block + '" finished, returning: ' + returned
end

log('outer block') do
    log('some little block') do
        5.to_s
    end
    log('yet another block') do
        'I like Thai food!'
    end
    false.to_s
end