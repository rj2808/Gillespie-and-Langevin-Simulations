function Gillespie_miRNA(  )
% Function to be used for Gillespie Simulations of the miRNA gene regulations
% Make a_0 as the sum of all possible a_k's
Mi(1) = mi;
R(1) = r;
P(1) = p;
while
a_1 = K_p*(R(i)(t));
a_2 = K_r
a_3 = K_mi
a_4 = K_t*(R(i)(t)*Mi(i)(t))
a_5 = Y_r*R(i)(t)
a_6 = Y_mi*Mi(i)(t)
a_7 = Y_p*(P(i)(t))

a_0 = K_p*(R(i)(t)) + K_r + K_mi + K_t*(R(i)(t)*Mi(i)(t)) + Y_r*R(i)(t) + Y_mi*Mi(i)(t) + Y_p*(P(i)(t));
% Choosing a Exponential Random variable to choose after what time reaction should take place
Tau = exprand(1/(a_0));
% Chossing a Random Variable between 0 and 1 in order to choose which reaction
%should take place

A =  rand;

if ( 0=<A < a_1/a_0)


elseif()

elseif()
