#!/usr/bin/env python


from PIL import Image

filename = '3675a1345da00ecb4b7eee40e0d8a6c028d28b7acfff34739432d1576356e2bd_output.png'
image = Image.open(filename)

img = image.load()
imgbytes = image.tobytes()

width, height = image.size

# print [ bin(ord(x)) for x in contents[:8] ] 
print width*height
# exit()
n = []

# WE DON'T KNOW HOW TO CALCULATE N???
# for x in range(8):
    
#     n.append( bin(img[x,0][0])[-2:]) # R
#     n.append( bin(img[x,0][1])[-2:])  # G
#     n.append(bin(img[x,0][2])[-2:]) # B

# N = int("".join(n),2)
# even parity??


bits = "".join(n)

for N in range(0,480000):
    bits = bin(N)[2:]
    print bits

    number_of_one_bits = bits.count('1') 
    parity = 'odd' if number_of_one_bits % 2 else 'even'
    print parity, " parity"

    # Blue is channel 1, Green is Channel 2

    # print float(N) / 8.0

    print "N", N
                
    message = []          
    for position in range(width, width*height):
        row =  position % width
        col =  position / width
        
        data = img[row, col]
        red, green, blue = data

        red_indicator =  bin(red)[-2:]
        if parity == 'odd':
            channel_one = bin(green)[-2:]
            channel_two = bin(blue)[-2:]
        elif parity == 'even':
            channel_one = bin(blue)[-2:]
            channel_two = bin(green)[-2:]
        # print "position", position, 
        if ( red_indicator == '00' ):
            continue
        elif ( red_indicator == '01' ):
            message.append(channel_two)
            # print "found channel two"
        elif ( red_indicator == '10' ):
            message.append(channel_one)
            # print "found channel one"
        elif ( red_indicator == '11' ):
            # print "found both channels"
            message.append(channel_one)
            message.append(channel_two)

        print "length", len("".join(message)), "versus", N
        if len("".join(message)) >= N:
            break

    print "Found data:", "".join(message)
    try:
        print "Decoded data:", hex(int("".join(message),2))[2:].replace('L','').decode('hex')
    except:
        print "Decoded data:", str('0'+hex(int("".join(message),2))[2:].replace('L','')).decode('hex')
    open('saved_data%d.txt' % N, 'w').write("".join(message))
    try:
        open('decoded_data%d.txt' % N, 'w').write(hex(int("".join(message),2))[2:].replace('L','').decode('hex'))
    except:
        open('decoded_data%d.txt' % N, 'w').write(str('0'+hex(int("".join(message),2))[2:].replace('L','')).decode('hex'))
        


    # XOR method...
    # 0000000000011110
    # 00000000
    # 00011110
    # now = 0b00000000 ^ 0b00011110
    # print bin(now)
    # ... still tells us Even Parity




    # for i in range(8):
        # print bin(ord(imgbytes[i]))

    # 0 - 255 (R)
    # 0 - 255 (G)
    # 0 - 255 (B)

    # image.close()