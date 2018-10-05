#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author: john
# @Date:   2016-08-25 14:33:10
# @Last Modified by:   john
# @Last Modified time: 2016-12-03 11:16:39

from Crypto.Util.number import getPrime, isPrime
import binascii
import primefac
import itertools

'''
This Python code tries to illustrate how RSA is done at a basic level.
'''

e = 65537
n = 128299637852747781491257187842028484364103855748297296704808405762229741626342194440837748106022068295635777844830831811978557490708404900063082674039252789841829590381008343327258960595508204744589399243877556198799438322881052857422197506822302290812621883700357890208069551876513290323124813780520689585503
c = 43160414063424128744492209010823042660025171642991046645158489731385945722740307002278661617111192557638773493117905684302084789590107080892369738949935010170735247383608959796206619491522997896941432858113478736544386518678449541064813172833593755715667806740002726487780692635238838746604939551393627585159


p = 11326943005628119672694629821649856331564947811949928186125208046290130000912120768861173564277210907403841603312764378561200102283658817695884193223692869
q = 11326943005628119672694629821649856331564947811949928186125208046290130000912216246378177299696220728414241927034282796937320547048361486068608744598351187

phi = ( q - 1 ) * ( p - 1 )


# Now, we can kind of unravel that modular arithmetic that was done during the
# ENCRYPTION formula. We can find the private key, d, with the MODULAR INVERSE,
# of e and phi.  
# I use a module to do this that is reworked to use Trey's function
#     https://github.com/JohnHammond/primefac_fork
d = primefac.modinv( e, phi )

# Now, we can do a similar thing like before, but this time for DECRYPTION.
#        m = ( c ^ d ) % n
# This time we raise to our private key as an exponent, but still take the modulus.
# And we have successfully decrypted RSA!
m = pow( c, d, n )
print repr(binascii.unhexlify(hex(m)[2:-1]))