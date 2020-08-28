from tkinter import *
import bookshop


def Main_view():

	window = Tk()
	window.title("Book Manager")
	window.geometry("500x250")

	def add_book():
		if(len(book_name.get()) != 0):
			list = [book_name.get(), author.get(), year.get(), ISBN.get()]
			for i in range(len(list)):
				if list[i] == None:
					list[i] = Unknown
			bookshop.add_book(book_name.get(), author.get(), year.get(), ISBN.get())
		else:
			pass

	def view_all():
		listbox.delete(0,END)
		for i in bookshop.view_all():
			listbox.insert(END, i)

	def search_book():
		listbox.delete(0,END)
		for i in bookshop.search_book(book_name.get(), author.get(), year.get(), ISBN.get()):
			listbox.insert(END, i)


	def delete_book():
		clicked_item = listbox.curselection()
		bookshop.delete_book(clicked_item[0])

	def clear():
		book_name.delete(0,END)
		year.delete(0,END)
		author.delete(0,END)
		ISBN.delete(0,END)


	def close():
		window.destroy()

	



	# Config entry and labels
	book_name = Entry(window, textvariable = StringVar())
	book_name.grid(row = 1, column = 1)
	book_name_label = Label(window, text="Book Title")
	book_name_label.grid(row = 1, column = 0)


	author = Entry(window, textvariable = StringVar())
	author.grid(row = 1, column = 3)
	author_label = Label(window, text="Author")
	author_label.grid(row = 1, column = 2)

	year = Entry(window, textvariable = IntVar())
	year.grid(row = 2, column = 1)
	year_label = Label(window, text="Year")
	year_label.grid(row = 2, column = 0)

	ISBN = Entry(window, textvariable = IntVar())
	ISBN.grid(row = 2, column = 3)
	ISBN_label = Label(window, text="ISBN")
	ISBN_label.grid(row = 2, column = 2)


	# Config buttons and functionalities

	view_all_button = Button(window, text="View All", width = 14,
		relief = RAISED, command = view_all)
	view_all_button.grid(row=3,column=3)


	add_book_button = Button(window, text="Add a new book", width = 14, relief = RAISED, command = add_book)
	add_book_button.grid(row=4, column = 3)

	search_book_button = Button(window, text = "Search Book", width = 14, relief = RAISED, command = search_book)
	search_book_button.grid(row=5, column = 3)

	remove_book_button = Button(window, text = "Remove Selected Book", width = 14, relief = RAISED, command = delete_book)
	remove_book_button.grid(row=6, column = 3)

	# clear_book = Button(window, text = "Remove Book", width = 14, relief = RAISED, command = remove_book)
	# clear_book_button.grid(row=7, column = 3)

	close_button = Button(window, text = "Close", width = 14, relief = RAISED, command = close)
	close_button.grid(row=7, column = 3)




	# Config listing of books 
	listbox = Listbox(window)
	listbox.grid(row = 3, column =1, rowspan = 5)
	scroll_bar = Scrollbar(window)
	value = str(listbox.get(ANCHOR))
	print(value)




	window.mainloop()

if __name__ == "__main__":
	Main_view()














