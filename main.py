import csv

def parse_row(row):
    return [row[0], row[1], row[2], int(row[3]), float(row[4])]

def get_books(file_path):
    with open(file_path, 'r', encoding='utf-8') as f:
        reader = csv.reader(f, delimiter='|')
        next(reader)
        return list(map(parse_row, reader))

def filtered_book(books, filter_name):
    return list(
        map(
            lambda book:[
              book[0],                              # isbn
              f"{book[1]}, {book[2]}",              # title, author
              book[3],                              # quantity
              book[4]
            ],
            filter(
                lambda book: filter_name.lower() in book[1].lower(),
                books
            )
        )
    )

def get_total_cost (filtered_books):
  return tuple(list(map(
      lambda book: (book[0], book[2] * book[3]),
      filtered_books
    )
  )
)

books = get_books("books.csv")
print(books)

print('----------------------------')

filter_books = filtered_book(books, "python")
print(filter_books)

print('----------------------------')

final = get_total_cost(filter_books)
print(final)

input("Нажмите Enter, чтобы выйти...")