def log description_of_block, &block
    puts ('   ' * $nesting_depth) + 'Beginning "' + description_of_block + '"'
    $nesting_depth += 1
    returned = block.call
    $nesting_depth -= 1
    puts ('   ' * $nesting_depth) + '..."' + description_of_block + '" finished, returning: ' + returned.to_s
end

$nesting_depth = 0

log('outer block') do
    log('some little block') do
        log('tiny block') do
            'hi'
        end
        5
    end
    log('yet another block') do
        'I like Thai food!'
    end
    true
end