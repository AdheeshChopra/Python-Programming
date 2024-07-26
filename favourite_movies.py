movies = []

# METHOD 1
movie1 = input("Enter the first movie: ")
movie2 = input("Enter the second movie: ")
movie3 = input("Enter the third movie: ")

movies.append(movie1)
movies.append(movie2)
movies.append(movie3)

# METHOD 2
movie = input("Enter the first movie: ")
movies.append(movie)
movie = input("Enter the second movie: ")
movies.append(movie)
movie = input("Enter the third movie: ")
movies.append(movie)

#METHOD 3
movies.append(input("Enter the first movie: "))
movies.append(input("Enter the second movie: "))
movies.append(input("Enter the third movie: "))

# PRINT STATEMENT
print(movies)