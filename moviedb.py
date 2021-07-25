from imdb import IMDb
ia = IMDb()
name = input('Enter movie name: ')
search = ia.search_movie(name)
if (len(search) != 0):
    ser_flag = 0
    loc = -1
    for v in search:
        if (name == str(v).lower()):
            ser_flag = ser_flag + 1
    if (ser_flag > 1):
        print('\n**INFO: There are more than one movies with this same title. Details of most popular movie on IMDb is displayed**')
    for v in search:
        if (name == str(v).lower()):
            loc = search.index(v)
            break
    if (loc != -1):    
        id = search[loc].movieID
        movie = ia.get_movie(id)
        curr = movie.current_info
        print('\nMovie: ' + movie['title'] + ' (' + str(movie['year']) + ')')
        print('\nIMDb Rating: ',movie.data['rating'])
        plot = movie['plot']
        pi = ''
        for k in plot:
            if '::' in k:
                ind = k.index('::')
                k = k[0:ind]
            pi = pi + k
        print('\nSynopsis: ',pi)
        cast1 = movie['cast']
        cast_var = ''
        cast_flag = 0
        for h in cast1:
            cast_flag = cast_flag + 1
            cast_var = cast_var + str(h['name'] + ',')
            if (cast_flag > 9):
                break
        print('\nCast: ',cast_var[0:len(cast_var)-1])
        di = ''
        for director in movie['directors']:
            di = di + str(director) + '-'
        print('\nDirector: ' + di[0:len(di)-1])
        gi = ''
        for genre in movie['genres']:
            gi = gi + genre + ','
        print('\nGenre: ' + gi[0:len(gi)-1])
        print('\nCountry: ',movie.data['countries'][0])
    else:
        print("\nNo such movie exist in database!")
else:
        print("\nNo such movie exist in database!")