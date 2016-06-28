% Function for Simulating Langevin Equations for miRNA Regulation for Gene Expression
function LS_miRNA(mi, p, r, K_r, K_p, K_mi,  K_t, Y_r, Y_p, Y_mi, h, n)
	
	R(0) = r
	P(0) = p
	Mi(0) = mi
	for i = 0:n
		% Simulating over the step 
		% Generating Random Noise for various noise terms in Langevin Simulations
		X = randn(3)
		R(i+h)  =  R(i) + h(K_r - K_p*R(i) - K_t*R(i)*Mi(i) - Y_r*R(i) + sqrt(K_p*R(i))X(0) + sqrt(K_t*R(i)*Mi(i))* X(1) + sqrt(Y_r*R(i))* X(2) ) 
		P(i+h)  =  P(i) + h(K_p*R(i) - Y_p*P(i)	+ sqrt(K_p*R(i))X(0) + 	sqrt(Y_p*P(i))	)
		Mi(i+h) =  M(i) + h(K_mi  - K_t*R(i)*Mi(i)	- Y_mi* Mi(i) + sqrt(K_t*R(i)*Mi(i))* X(1)	+ sqrt(Y_mi*Mi(i))*X(2)	) 
	
	end
% Time Axis for plotting	
	t = 0 :h:n*h

	
%	plot()
%	xlabel()
%	ylabel()
	
%	plot()
%	xlabel()
%	ylabel()

end

% Function for simulating Gillespie Algorithm for miRNA Regulation for Gene Expression

%function GS_miRNA(mi, p, r, K_r, K_p, K_t, Y_r, Y_p, Y_mi, h, n)



