items = [
    ("Tali Karmantel", 6, 35),
    ("Senter Headlamp", 2, 22),
    ("Radio HT", 3, 28),
    ("Peta & Kompas", 1, 15),
    ("Kotak P3K", 4, 33),
    ("Jas Hujan", 2, 18),
    ("Pisau Lipat", 1, 14),
    ("Botol Air", 3, 20),
    ("Ransum Makanan", 5, 30),
    ("Selimut Darurat", 2, 19)
]

capacity = 15
best_value = 0
best_combo = []
current_combo = []

def bt(i, weight, value):
    global best_value, best_combo

    if weight > capacity:
        return  # PRUNING

    if i == len(items):
        if value > best_value:
            best_value = value
            best_combo = current_combo.copy()
        return

    # pilih item
    current_combo.append(items[i][0])
    bt(i+1, weight + items[i][1], value + items[i][2])
    current_combo.pop()

    # tidak pilih item
    bt(i+1, weight, value)

bt(0, 0, 0)

total_weight = sum(w for (name, w, v) in items if name in best_combo)

print("Nilai Maksimum:", best_value)
print("Item Terpilih:", best_combo)
print("Total Berat:", total_weight, "kg")
