import csv
from datetime import datetime

all_authors = []
all_genres = []
all_start_dates = []

item_authors = {}
item_genres = {}

# Parse and clean items
with open('csv/items.csv', newline='', encoding='utf-8') as csvfile,\
        open("csv/items_clean.csv", mode="w", newline="", encoding="utf-8") as outfile:
    reader = csv.DictReader(csvfile)
    writer = csv.DictWriter(outfile, fieldnames=['item_id', 'title', "year"])

    writer.writeheader()

    for row in reader:
        item_id = row["id"]
        authors = row['authors'].split(",")
        genres = row['genres'].split(',')
        title = row["title"]
        year = row["year"]

        # Write clean CSV
        wrow = {
                "item_id": item_id,
                "title": title,
                "year": year,
                }
        writer.writerow(wrow)

        # Process authors and genres
        item_authors[item_id] = []
        item_genres[item_id] = []

        for author in authors:
            author = author.strip()
            if not author:
                continue
            if author not in all_authors:
                author_id = len(all_authors)
                all_authors.append(author)
            else:
                author_id = all_authors.index(author)
            item_authors[item_id].append(author_id)

        for genre in genres:
            genre = genre.strip()
            if not genre:
                continue
            if genre not in all_genres:
                genre_id = len(all_genres)
                all_genres.append(genre)
            else:
                genre_id = all_genres.index(genre)

            item_genres[item_id].append(genre_id)

# Create authors
with open('csv/authors.csv', mode='w', newline='') as csvfile:
    writer = csv.DictWriter(csvfile, fieldnames=['author_id', 'name'])

    writer.writeheader()

    for i, author in enumerate(all_authors):
        row = {"author_id": i, "name": author}
        writer.writerow(row)

# Create genres
with open('csv/genres.csv', mode='w', newline='') as csvfile:
    writer = csv.DictWriter(csvfile, fieldnames=['genre_id', 'name'])

    writer.writeheader()

    for i, genre in enumerate(all_genres):
        row = {"genre_id": i, "name": genre}
        writer.writerow(row)

# Create items_authors
with open('csv/items_authors.csv', mode='w', newline='') as csvfile:
    writer = csv.DictWriter(csvfile, fieldnames=['item_id', 'author_id'])

    writer.writeheader()

    for item_id, authors in item_authors.items():
        for author_id in authors:
            row = {"item_id": item_id, "author_id": author_id}
            writer.writerow(row)

# Create items_authors
with open('csv/items_genres.csv', mode='w', newline='') as csvfile:
    writer = csv.DictWriter(csvfile, fieldnames=['item_id', 'genre_id'])

    writer.writeheader()

    for item_id, genres in item_genres.items():
        for genre_id in genres:
            row = {"item_id": item_id, "genre_id": genre_id}
            writer.writerow(row)

# Parse interactions and split time dim
with open('csv/interactions.csv', newline='', encoding='utf-8') as csvfile,\
        open("csv/interactions_new.csv", mode="w", newline="", encoding="utf-8") as outfile:
    reader = csv.DictReader(csvfile)
    writer = csv.DictWriter(outfile, fieldnames=['user_id', 'item_id',
                                                 "start_date_id",
                                                 "progress", "rating"])

    writer.writeheader()

    for row in reader:
        user_id = row["user_id"]
        item_id = row["item_id"]
        progress = row["progress"]
        rating = row["rating"]
        start_date = row["start_date"]

        if start_date not in all_start_dates:
            start_date_id = len(all_start_dates)
            all_start_dates.append(start_date)
        else:
            start_date_id = all_start_dates.index(start_date)

        wrow = {
                "user_id": user_id,
                "item_id": item_id,
                "start_date_id": start_date_id,
                "progress": progress,
                "rating": rating,
                }
        writer.writerow(wrow)

# Create start_dates
with open('csv/start_dates.csv', mode='w', newline='') as csvfile:
    writer = csv.DictWriter(csvfile, fieldnames=['date_id', 'date',
                                                 "year", "month", "day",
                                                 "day_of_week",
                                                 "day_of_year"])

    writer.writeheader()

    for i, start_date in enumerate(all_start_dates):
        date_obj = datetime.strptime(start_date, '%Y-%m-%d').date()
        day_of_week = date_obj.strftime('%A')
        day_of_year = date_obj.strftime('%j')

        row = {
                "date_id": i,
                "date": start_date,
                "year": date_obj.year,
                "month": date_obj.month,
                "day": date_obj.day,
                "day_of_week": day_of_week,
                "day_of_year": day_of_year,
                }

        writer.writerow(row)

# Parse and process users
with open('csv/users.csv', newline='', encoding='utf-8') as csvfile,\
        open("csv/users_new.csv", mode="w", newline="", encoding="utf-8") as outfile:
    reader = csv.DictReader(csvfile)
    writer = csv.DictWriter(outfile, fieldnames=['user_id', "age_group",
                                                 'age', "sex"])

    writer.writeheader()

    for row in reader:
        user_id = row["user_id"]
        age_group = row["age"]
        sex = row["sex"]

        if age_group:
            # Centric age of age group
            age = int(age_group.split("_")[0]) + 5
        else:
            age = None

        wrow = {
                "user_id": user_id,
                "age_group": age_group,
                "age": age,
                "sex": sex,
                }
        writer.writerow(wrow)

