# Mathematica code for calculating the 2-point Taylor expansion

This folder contains a file with the code and examples I used to calculate the 2-point Taylor expansion of 2n-1 order of a function f at points a and b.

For details please check [my blog post](https://underthemath.wordpress.com/2020/06/12/polynomial-division-revisited/)

The code is:

TwoPointTaylor[f_, a_, b_, 1] := 
 TwoPointTaylor[f, a, b, 1] = 
  Module[{coeffs, c1, d1, linf}, linf = c1 + d1 # &; 
   coeffs = Solve[{f[a] == linf[a], f[b] == linf[b]}, {c1, d1}]; 
   linf /. coeffs[[1]]]
TwoPointTaylor[f_, a_, b_, n_] := 
 TwoPointTaylor[f, a, b, n] = 
  Module[{coeff, dfnm1 = D[f[x], {x, n - 1}], newterm, d2pTnm1, c, d},
    newterm = (c + d #) ((# - a) (# - b))^(n - 1) &; 
   d2pTnm1 = 
    D[newterm[x] + TwoPointTaylor[f, a, b, n - 1][x], {x, n - 1}]; 
   coeff = Solve[{(dfnm1 == d2pTnm1) /. x -> a, (dfnm1 == d2pTnm1) /. 
       x -> b}, {c, 
      d}]; (newterm[#] + TwoPointTaylor[f, a, b, n - 1][#]) /. 
     coeff[[1]] &]
