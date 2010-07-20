"""

This script define the different symbolic noise functions
The noise contract is simple: noise_lvl is a symbolic variable going from 0 to 1
0: no changement.
1: max noise.

"""
import theano
import theano.tensor as T

def binomial_noise(theano_rng,inp,noise_lvl):
    return theano_rng.binomial( size = inp.shape, n = 1, p =  1 - noise_lvl) * inp


def binomial_NLP_noise(theano_rng,inp,noise_lvl):
    return theano_rng.binomial( size = inp.shape, n = 1, p =  1 - noise_lvl[0]) * inp + (inp==0) * theano_rng.binomial( size = inp.shape, n = 1, p =  noise_lvl[1])
