#        HUYNH NHAT YEN DAN
#
# ~~~~~~~~~~ LIBRARY APP ~~~~~~~~~~~
#
#          Scan MEMBERID
#          Scan Book ISBN
#          If the book is on loan Return the book
#          else
#          get BorrowDate
#          calculate DueDate = BorrowDate +7 days
#          Add BorrowDate, DueDate, BookISBN and MemberID to the Loan Table

def Display_Member(MemberID, MemberName ) :
    print(f"User number {MemberID} goes by the name {MemberName}")

Display_Member(1123," The King ")     