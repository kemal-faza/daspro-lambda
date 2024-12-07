LuasSegitiga = lambda a, t: int((a * t) / 2)
print(LuasSegitiga(2, 3))

max2 = lambda a, b: a if a > b else (b if b > a else "sama")
print(max2(1, 5))

TitikBeku = lambda suhu: "Beku" if suhu <= 0 else ("Cari" if 0 < suhu < 100 else "Uap")
print(TitikBeku(0))
print(TitikBeku(30))
print(TitikBeku(100))
