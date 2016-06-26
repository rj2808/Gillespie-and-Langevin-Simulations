% Function for Simulating Langevin Equations for miRNA Regulation for Gene Expression
function LS_miRNA(mi, p, r, K_r, K_p, K_mi,  K_t, Y_r, Y_p, Y_mi, h, n)
	R(1) = r;
	P(1) = p;
	Mi(1) = mi;
	for i = 1:n+1
        X = randn()
        Y = randn()
        Z = randn() 
		% Simulating over the step 
		% Generating Random Noise for various noise terms in Langevin Simulations
		R(i+1)  =  R(i) + h*(K_r - (K_p*R(i)) - (K_t*(R(i))*(Mi(i))) - (Y_r*(R(i))) + (sqrt(K_p*(R(i)))*(X)) + (sqrt(K_t*(R(1))*(Mi(1)))*Y) + (sqrt(Y_r*(R(1)))* Z) ); 
		P(i+1)  =  P(i) + h*(K_p*R(i) - Y_p*P(i)	+ sqrt(K_p*R(i))*X + 	sqrt(Y_p*P(i))*Z	);
		Mi(i+1) =  Mi(i) + h*(K_mi  - K_t*R(i)*Mi(i)	- Y_mi* Mi(i) + sqrt(K_t*R(i)*Mi(i))* Y	+ sqrt(Y_mi*Mi(i))*Z	); 
	
    end
% Time Axis for plotting	
	t = 0 :h:(n+1)*h
    plot(t,P)
    
	xlabel('Time')
	ylabel('Protien Concerntration')
    figure()
 
	plot(t,R)
   
	xlabel('Time')
	ylabel('mRNA Concerntration') 
    figure()

    plot(t,Mi)
    xlabel('Time')
    ylabel('miRNA Concerntration')







end

% Function for simulating Gillespie Algorithm for miRNA Regulation for Gene Expression

%function GS_miRNA(mi, p, r, K_r, K_p, K_t, Y_r, Y_p, Y_mi, h, n)



