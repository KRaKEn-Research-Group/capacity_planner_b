0.1::store_size(very_small);0.2::store_size(small);0.4::store_size(medium);0.2::store_size(big);0.1::store_size(very_big).

0.5::tourism(low) ; 0.35::tourism(medium) ; 0.15::tourism(high) :- store_size(very_small).
0.6::tourism(low) ; 0.25::tourism(medium) ; 0.15::tourism(high) :- store_size(small).
0.7::tourism(low) ; 0.20::tourism(medium) ; 0.10::tourism(high) :- store_size(medium).
0.85::tourism(low) ; 0.10::tourism(medium) ; 0.05::tourism(high) :- store_size(big).
0.95::tourism(low) ; 0.05::tourism(medium) ; 0::tourism(high) :- store_size(very_big).

0.2::parking_spot ; 0.8::no_parking_spot :- store_size(very_small).
0.3::parking_spot ; 0.7::no_parking_spot :- store_size(small).
0.6::parking_spot ; 0.4::no_parking_spot :- store_size(medium).
0.8::parking_spot ; 0.2::no_parking_spot :- store_size(big).
1::parking_spot ; 0::no_parking_spot :- store_size(very_big).

normal(500, 100)::customer_base :- store_size(very_small).
normal(1000, 200)::customer_base :- store_size(small).
normal(5000, 100)::customer_base :- store_size(medium).
normal(15000, 5000)::customer_base :- store_size(big).
normal(30000, 10000)::customer_base :- store_size(very_big).

output([ very_small, parking, low_tourism, CB]) :-  store_size(very_small), parking_spot, tourism(low), value(customer_base, CB).
output([ very_small, no_parking, low_tourism, CB]) :-  store_size(very_small), no_parking_spot, tourism(low), value(customer_base, CB).
output([ very_small, parking, medium_tourism, CB]) :-  store_size(very_small), parking_spot, tourism(medium), value(customer_base, CB).
output([ very_small, no_parking, medium_tourism, CB]) :-  store_size(very_small), no_parking_spot, tourism(medium), value(customer_base, CB).
output([ very_small, parking, high_tourism, CB]) :-  store_size(very_small), parking_spot, tourism(high), value(customer_base, CB).
output([ very_small, no_parking, high_tourism, CB]) :-  store_size(very_small), no_parking_spot, tourism(high), value(customer_base, CB).

output([ small, parking, low_tourism, CB]) :-  store_size(small), parking_spot, tourism(low), value(customer_base, CB).
output([ small, no_parking, low_tourism, CB]) :-  store_size(small), no_parking_spot, tourism(low), value(customer_base, CB).
output([ small, parking, medium_tourism, CB]) :-  store_size(small), parking_spot, tourism(medium), value(customer_base, CB).
output([ small, no_parking, medium_tourism, CB]) :-  store_size(small), no_parking_spot, tourism(medium), value(customer_base, CB).
output([ small, parking, high_tourism, CB]) :-  store_size(small), parking_spot, tourism(high), value(customer_base, CB).
output([ small, no_parking, high_tourism, CB]) :-  store_size(small), no_parking_spot, tourism(high), value(customer_base, CB).

output([ medium, parking, low_tourism, CB]) :-  store_size(medium), parking_spot, tourism(low), value(customer_base, CB).
output([ medium, no_parking, low_tourism, CB]) :-  store_size(medium), no_parking_spot, tourism(low), value(customer_base, CB).
output([ medium, parking, medium_tourism, CB]) :-  store_size(medium), parking_spot, tourism(medium), value(customer_base, CB).
output([ medium, no_parking, medium_tourism, CB]) :-  store_size(medium), no_parking_spot, tourism(medium), value(customer_base, CB).
output([ medium, parking, high_tourism, CB]) :-  store_size(medium), parking_spot, tourism(high), value(customer_base, CB).
output([ medium, no_parking, high_tourism, CB]) :-  store_size(medium), no_parking_spot, tourism(high), value(customer_base, CB).

output([ big, parking, low_tourism, CB]) :-  store_size(big), parking_spot, tourism(low), value(customer_base, CB).
output([ big, no_parking, low_tourism, CB]) :-  store_size(big), no_parking_spot, tourism(low), value(customer_base, CB).
output([ big, parking, medium_tourism, CB]) :-  store_size(big), parking_spot, tourism(medium), value(customer_base, CB).
output([ big, no_parking, medium_tourism, CB]) :-  store_size(big), no_parking_spot, tourism(medium), value(customer_base, CB).
output([ big, parking, high_tourism, CB]) :-  store_size(big), parking_spot, tourism(high), value(customer_base, CB).
output([ big, no_parking, high_tourism, CB]) :-  store_size(big), no_parking_spot, tourism(high), value(customer_base, CB).

output([ very_big, parking, low_tourism, CB]) :-  store_size(very_big), parking_spot, tourism(low), value(customer_base, CB).
output([ very_big, no_parking, low_tourism, CB]) :-  store_size(very_big), no_parking_spot, tourism(low), value(customer_base, CB).
output([ very_big, parking, medium_tourism, CB]) :-  store_size(very_big), parking_spot, tourism(medium), value(customer_base, CB).
output([ very_big, no_parking, medium_tourism, CB]) :-  store_size(very_big), no_parking_spot, tourism(medium), value(customer_base, CB).
output([ very_big, parking, high_tourism, CB]) :-  store_size(very_big), parking_spot, tourism(high), value(customer_base, CB).
output([ very_big, no_parking, high_tourism, CB]) :-  store_size(very_big), no_parking_spot, tourism(high), value(customer_base, CB).


query(output(_)).