# Write your MySQL query statement below
with borrowing_record as (
    select 
        book_id, 
        count(*) as borrowing_number
    from borrowing_records
    WHERE return_date IS NULL
    GROUP BY book_id
)

select 
    library_books.book_id, 
    library_books.title,
    library_books.author,
    library_books.genre,
    library_books.publication_year, 
    library_books.total_copies as current_borrowers
    from library_books
    join borrowing_record
    on borrowing_record.book_id = library_books.book_id and borrowing_record.borrowing_number = library_books.total_copies
    order by library_books.total_copies DESC, library_books.title ASC;
 