film_titles = ["Diuna","Back to the Future","Bladerunner 2047","Lightyear","Wall-E"]
f = open("film_titles.txt","w")
for i in film_titles:
	f.write(i + "\n")
f.close()