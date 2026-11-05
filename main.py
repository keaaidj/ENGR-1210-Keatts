# =============================================================================
# ENGR 1210 - Morse Optical Comms
# =============================================================================
# GOAL
#   Blink a Morse message on an LED - first on your LAPTOP, then, with the SAME
#   file and no changes, on a real Pico 2 in Wokwi. That "it just works on the
#   board too" moment is the whole idea of a HAL (Hardware Abstraction Layer).
#
# =============================================================================
 
import hal_pc as hw
#import hal_pico as hw  # uncomment this line to run on the real Pico 2
from morse_code import WORD_GAP_MS, DOT_MS, DASH_MS, SYMBOL_GAP_MS, LETTER_GAP_MS, encode_message
 
 
def blink_pattern(pattern):
 
    # pattern is one letter, like '...'
    for i, symbol in enumerate(pattern):
        if i > 0:
            hw.set_led_timed(False, SYMBOL_GAP_MS)      
        if symbol == '.':
            hw.set_led_timed(True, DOT_MS)               
        elif symbol == '-':
            hw.set_led_timed(True, DASH_MS)              
 

print("Board:", hw.board_info())     
print("Type a message and watch it blink once.")
 
message = input("\nMessage to blink: ").strip()
if message:
    patterns = encode_message(message)            
    print("Morse:", patterns)
    for i, pattern in enumerate(patterns):
        if pattern == ' ':
            hw.set_led_timed(False, WORD_GAP_MS) 
        else:
            if i > 0 and patterns[i - 1] != ' ':
                hw.set_led_timed(False, LETTER_GAP_MS) 
            blink_pattern(pattern)
    hw.set_led(False)                               
    print("...done")