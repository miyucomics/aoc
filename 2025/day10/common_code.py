def gosper_hack(x):
    smallest = x & -x
    ripple = x + smallest
    new_smallest = ripple & -ripple
    ones = ((new_smallest // smallest) >> 1) - 1
    return ripple | ones

def select(array, mask):
    m = mask
    i = 0
    while m:
        if m & 1:
            yield array[i]
        m >>= 1
        i += 1

def bits_to_indices(mask):
    return [i for i in range(mask.bit_length()) if mask & (1 << i)]

def compute_state(mask, buttons):
    result = 0
    for button in select(buttons, mask):
        result ^= button
    return result

def find_button_presses(target, buttons):
    n = len(buttons)
    for bit_count in range(1, n + 1):
        mask = (1 << bit_count) - 1
        while mask < (1 << n):
            if compute_state(mask, buttons) == target:
                yield mask
            mask = gosper_hack(mask)
