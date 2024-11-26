records = input(
"Enter borrowed books in the format 'Book Title - Days Borrowed' (separated by commas): ").split(", ")

book_dict = {}

for record in records:
    title, days = record.split(" - ")
    days = int(days)
    if title in book_dict:
        book_dict[title] += days
    else:
        book_dict[title] = days

most_borrowed = max(book_dict, key=book_dict.get)
least_borrowed = min(book_dict, key=book_dict.get)

average_days = sum(book_dict.values()) / len(book_dict)

unique_titles = set(book_dict.keys())

sorted_books = sorted(book_dict.items(), key=lambda item: item[1], reverse=True)

print("Most borrowed book:", most_borrowed)
print("Least borrowed book:", least_borrowed)
print("Average borrowing days:", average_days)
print("Unique book titles:", unique_titles)
print("Books sorted by borrowing duration:", sorted_books)
