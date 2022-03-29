import json
import uuid
import csv

#create authors, places, and topics lists
author_list = []
place_list = []
topic_list = []
with open('Meme Studies Index .xlsx - Sheet1.csv', newline='', encoding='utf-8') as csvfile:
	reader = csv.DictReader(csvfile)
	author_id = 0
	place_id = 0
	topic_id = 0
		
	with open('authors_table.csv', 'w', newline='', encoding='utf-8') as authors:
		writer3 = csv.writer(authors)

		with open('places_table.csv', 'w', newline='', encoding='utf-8') as places:
			writer4 = csv.writer(places)

			with open('topics_table.csv', 'w', newline='', encoding='utf-8') as topics:
				writer5 = csv.writer(topics)

				#iterate through every line of csv file
				for row in reader:
					#create authors list and authors table csv
					author_tuple = (row['Author1 Last name'], row['Author1 First name'])

					#check if author is not already added to list
					if author_tuple not in author_list:
						author_list.append(author_tuple)
						author_id = author_list.index(author_tuple)

						#add id (index of author in author list) and author last name and first name
						author_entry = [author_id] + list(author_tuple)
						writer3.writerow(author_entry)

					if row['Author2 Last name'] != "":
						author_tuple = (row['Author2 Last name'], row['Author2 First name'])

						if author_tuple not in author_list:
							author_list.append(author_tuple)
							author_id = author_list.index(author_tuple)
							
							author_entry = [author_id] + list(author_tuple)
							writer3.writerow(author_entry)

					if row['Author3 Last name'] != "":
						author_tuple = (row['Author3 Last name'], row['Author3 First name'])

						if author_tuple not in author_list:
							author_list.append(author_tuple)
							author_id = author_list.index(author_tuple)
							
							author_entry = [author_id] + list(author_tuple)
							writer3.writerow(author_entry)

					if row['Author4 Last name'] != "":
						author_tuple = (row['Author4 Last name'], row['Author4 First name'])

						if author_tuple not in author_list:
							author_list.append(author_tuple)
							author_id = author_list.index(author_tuple)
							
							author_entry = [author_id] + list(author_tuple)
							writer3.writerow(author_entry)

					if row['Author5 Last name'] != "":
						author_tuple = (row['Author5 Last name'], row['Author5 First name'])

						if author_tuple not in author_list:
							author_list.append(author_tuple)
							author_id = author_list.index(author_tuple)
					
							author_entry = [author_id] + list(author_tuple)
							writer3.writerow(author_entry)

					if row['Author6 Last name'] != "":
						author_tuple = (row['Author6 Last name'], row['Author6 First name'])

						if author_tuple not in author_list:
							author_list.append(author_tuple)
							author_id = author_list.index(author_tuple)
							
							author_entry = [author_id] + list(author_tuple)
							writer3.writerow(author_entry)

					if row['Author7 Last name'] != "":
						author_tuple = (row['Author7 Last name'], row['Author7 First name'])

						if author_tuple not in author_list:
							author_list.append(author_tuple)
							author_id = author_list.index(author_tuple)
							
							author_entry = [author_id] + list(author_tuple)
							writer3.writerow(author_entry)
					
					#create places list and places table csv
					if row['Place 1'] != "":
						if row['Place 1'] not in place_list:
							place_list.append(row['Place 1'])
							place_id = place_list.index(row['Place 1'])

							place_entry = [place_id, row['Place 1']]
							writer4.writerow(place_entry)

					if row['Place 2'] != "":
						if row['Place 2'] not in place_list:
							place_list.append(row['Place 2'])
							place_id = place_list.index(row['Place 2'])

							place_entry = [place_id, row['Place 2']]
							writer4.writerow(place_entry)

					#create topics list and topics table csv
					if row['Topic1*'] != "":
						if row['Topic1*'] not in topic_list:
							topic_list.append(row['Topic1*'])
							topic_id = topic_list.index(row['Topic1*'])

							topic_entry = [topic_id, row['Topic1*']]
							writer5.writerow(topic_entry)

					if row['Topic2*'] != "":
						if row['Topic2*'] not in topic_list:
							topic_list.append(row['Topic2*'])
							topic_id = topic_list.index(row['Topic2*'])

							topic_entry = [topic_id, row['Topic2*']]
							writer5.writerow(topic_entry)

					if row['Topic3'] != "":
						if row['Topic3'] not in topic_list:
							topic_list.append(row['Topic3'])
							topic_id = topic_list.index(row['Topic3'])

							topic_entry = [topic_id, row['Topic3']]
							writer5.writerow(topic_entry)

					if row['Topic4'] != "":
						if row['Topic4'] not in topic_list:
							topic_list.append(row['Topic4'])
							topic_id = topic_list.index(row['Topic4'])

							topic_entry = [topic_id, row['Topic4']]
							writer5.writerow(topic_entry)




#write sources & authors tables to csv file
with open('Meme Studies Index .xlsx - Sheet1.csv', newline='', encoding='utf-8') as csvfile:
	reader = csv.DictReader(csvfile)
	id = 1
	sources_have_authors_id = 1
	sources_have_places_id = 1
	sources_have_topics_id = 1

	with open('sources_have_authors_table.csv', 'w', newline='', encoding='utf-8') as sources_have_authors:
		writer2 = csv.writer(sources_have_authors)

		with open('sources_have_places_table.csv', 'w', newline='', encoding='utf-8') as sources_have_places:
			writer6 = csv.writer(sources_have_places)
	
			with open('sources_have_topics_table.csv', 'w', newline='', encoding='utf-8') as sources_have_topics:
				writer7 = csv.writer(sources_have_topics)

				# open the file in the write mode
				with open('sources_table.csv', 'w', newline='', encoding='utf-8') as sources:
				    # create the csv writer
					writer = csv.writer(sources)

					#iterate through every line of csv file
					for row in reader:
						isbn = row['ISBN']
						if isbn == "":
							isbn = "NULL"

						volume = row['Volume']
						if volume == "":
							volume = "NULL"

						number = row['Number']
						if number == "":
							number = "NULL"

						book = row['Book']
						if book == "":
							book = "NULL"

						book_edited = row['Book edited by']
						if book_edited == "":
							book_edited = "NULL"

						publisher = row['Publisher']
						if publisher == "":
							publisher = "NULL"

						book_city = row['City (if book)']
						if book_city == "":
							book_city = "NULL"

						pages = row['Pages']
						if pages == "":
							pages = "NULL"

						link = row['Link (Where Applicable)']
						if link == "":
							link = "NULL"

						platform = row['Platform']
						if platform == "":
							platform = "NULL"


						#create dictionary that holds all values for an entry
						index_entry = [id, row['Scholarly Article*'], row['Year*'], book, book_edited, publisher, isbn, book_city, volume, number, pages, link, platform, row['Resource Type*']]
						
						if(row['Year*'] != ""):
							#add entry to new csv
							writer.writerow(index_entry)

							#write to table that keeps track of authors for each source
							if row['Author1 Last name'] != "":
								target_author_tuple = [tup for tup in author_list if tup[0] == row['Author1 Last name'] and tup[1] == row['Author1 First name']]
								sources_have_authors_entry = [sources_have_authors_id, id, author_list.index(target_author_tuple[0])]
								writer2.writerow(sources_have_authors_entry)
								sources_have_authors_id = sources_have_authors_id + 1

							if row['Author2 Last name'] != "":
								target_author_tuple = [tup for tup in author_list if tup[0] == row['Author2 Last name'] and tup[1] == row['Author2 First name']]
								sources_have_authors_entry = [sources_have_authors_id, id, author_list.index(target_author_tuple[0])]
								writer2.writerow(sources_have_authors_entry)
								sources_have_authors_id = sources_have_authors_id + 1
							if row['Author3 Last name'] != "":
								target_author_tuple = [tup for tup in author_list if tup[0] == row['Author3 Last name'] and tup[1] == row['Author3 First name']]
								sources_have_authors_entry = [sources_have_authors_id, id, author_list.index(target_author_tuple[0])]
								writer2.writerow(sources_have_authors_entry)
								sources_have_authors_id = sources_have_authors_id + 1

							if row['Author4 Last name'] != "":
								target_author_tuple = [tup for tup in author_list if tup[0] == row['Author4 Last name'] and tup[1] == row['Author4 First name']]
								sources_have_authors_entry = [sources_have_authors_id, id, author_list.index(target_author_tuple[0])]
								writer2.writerow(sources_have_authors_entry)
								sources_have_authors_id = sources_have_authors_id + 1
							if row['Author5 Last name'] != "":
								target_author_tuple = [tup for tup in author_list if tup[0] == row['Author5 Last name'] and tup[1] == row['Author5 First name']]
								sources_have_authors_entry = [sources_have_authors_id, id, author_list.index(target_author_tuple[0])]
								writer2.writerow(sources_have_authors_entry)
								sources_have_authors_id = sources_have_authors_id + 1
							if row['Author6 Last name'] != "":
								target_author_tuple = [tup for tup in author_list if tup[0] == row['Author6 Last name'] and tup[1] == row['Author6 First name']]
								sources_have_authors_entry = [sources_have_authors_id, id, author_list.index(target_author_tuple[0])]
								writer2.writerow(sources_have_authors_entry)
								sources_have_authors_id = sources_have_authors_id + 1
							if row['Author7 Last name'] != "":
								target_author_tuple = [tup for tup in author_list if tup[0] == row['Author7 Last name'] and tup[1] == row['Author7 First name']]
								sources_have_authors_entry = [sources_have_authors_id, id, author_list.index(target_author_tuple[0])]
								writer2.writerow(sources_have_authors_entry)
								sources_have_authors_id = sources_have_authors_id + 1

							#write to table that keeps track of places for each source
							if row['Place 1'] != "":
								sources_have_places_entry = [sources_have_places_id, id, place_list.index(row['Place 1'])]
								writer6.writerow(sources_have_places_entry)
								sources_have_places_id = sources_have_places_id + 1
							if row['Place 2'] != "":
								sources_have_places_entry = [sources_have_places_id, id, place_list.index(row['Place 2'])]
								writer6.writerow(sources_have_places_entry)
								sources_have_places_id = sources_have_places_id + 1

							#write to table that keeps track of places for each source
							if row['Topic1*'] != "":
								sources_have_topics_entry = [sources_have_topics_id, id, topic_list.index(row['Topic1*'])]
								writer7.writerow(sources_have_topics_entry)
								sources_have_topics_id = sources_have_topics_id + 1
							if row['Topic2*'] != "":
								sources_have_topics_entry = [sources_have_topics_id, id, topic_list.index(row['Topic2*'])]
								writer7.writerow(sources_have_topics_entry)
								sources_have_topics_id = sources_have_topics_id + 1
							if row['Topic3'] != "":
								sources_have_topics_entry = [sources_have_topics_id, id, topic_list.index(row['Topic3'])]
								writer7.writerow(sources_have_topics_entry)
								sources_have_topics_id = sources_have_topics_id + 1
							if row['Topic4'] != "":
								sources_have_topics_entry = [sources_have_topics_id, id, topic_list.index(row['Topic4'])]
								writer7.writerow(sources_have_topics_entry)
								sources_have_topics_id = sources_have_topics_id + 1

							#increment id for each entry
							id= id+1