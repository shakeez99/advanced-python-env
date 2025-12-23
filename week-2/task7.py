items = input().split()
counts = {}
for item in items:
    if item in counts:
        counts[item] += 1
    else:
        counts[item] = 1

#Частота покупок
print("Purchase frequency:")
for item in counts:
    print(f"{item}: {counts[item]}")

#Самый популярный товар
max_count = 0
most_popular = ""
for item in counts:
    if counts[item] > max_count:
        max_count = counts[item]
        most_popular = item
print(f"Most popular item: {most_popular}")

#Товары, купленные один раз
once_items = []
for item in counts:
    if counts[item] == 1:
        once_items.append(item)
print("Purchased once:", " ".join(once_items))

#Сортировка по убыванию частоты
sorted_items = sorted(counts.items(), key=lambda x: -x[1])
print("Sorted by frequency:")
for item, count in sorted_items:
    print(item, count)