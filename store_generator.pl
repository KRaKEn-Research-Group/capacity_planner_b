normal(1, 2)::store_size.
normal(1, 2)::store_location.
normal(1, 2)::store_tourism.
normal(1, 2)::store_competition.
output([size:S, location:L, tourism:T, competition:C]) :- value(store_size, S), value(store_location, L), value(store_tourism, T), value(store_competition, C).
query(output(_)).