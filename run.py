from enigma import ROTOR_I, ROTOR_II, ROTOR_III, ROTOR_IV, ROTOR_V
from enigma import REFLECTOR_A, REFLECTOR_B, REFLECTOR_C
from enigma import Enigma
from enigma import Plugboard

EnigmaMachine = Enigma(reflector=REFLECTOR_B, 
                       left_rotor=ROTOR_III, 
                       middle_rotor=ROTOR_II, 
                       right_rotor=ROTOR_I, 
                       rotor_positions="16 10 1",
                       ring_positions="3 1 17",
                       plugboard=Plugboard("CE KL FP MD")
                       )

x=EnigmaMachine.encipher('Jeder Mensch sollte wissen, wie man Enigma-Maschine verwendet.')

print('Result is:')
print(x)
