def song() -> str:
    this_is = 'This is the '
    on1 = 'house that Jack built.'
    on2 = 'malt'
    on3 = 'rat,'
    on4 = 'cat,'
    on5 = 'dog,'
    on6 = 'cow with the crumpled horn,'
    on7 = 'maiden all forlorn,'
    on8 = 'man all tattered and torn,'
    on9 = 'priest all shaven and shorn,'
    on10 = "rooster that crow'd in the morn,"
    on11 = 'farmer sowing his corn,'
    on12 = 'horse and the hound and the horn,'
    str1 = 'lay in the house that Jack built.'
    str2 = 'ate the malt'
    str3 = 'killed the rat,'
    str4 = 'worried the cat,'
    str5 = 'tossed the dog,'
    str6 = 'milked the cow with the crumpled horn,'
    str7 = 'kissed the maiden all forlorn,'
    str8 = 'married the man all tattered and torn,'
    str9 = 'waked the priest all shaven and shorn,'
    str10 = "kept the rooster that crow'd in the morn,"
    str11 = 'belong to the farmer sowing his corn,'
    str12 = 'is the horse and the hound and the horn,'

    all_song = [str1, str2, str3, str4, str5, str6, str7, str8, str9, str10, str11, str12]
    all_start = [on1, on2, on3, on4, on5, on6, on7, on8, on9, on10, on11, on12]
    complete_song = []

    def complete():
        if str12 not in complete_song:
            for i in range(1, 13):
                if i != 1:
                    complete_song.append('\n')
                for q in reversed(range(i)):
                    if i != 1:
                        complete_song.append('\n')
                    if q == i - 1:
                        complete_song.append(this_is + all_start[q])
                    else:
                        complete_song.append('That ' + all_song[q])

                    q += 1

    complete()

    return ''.join(complete_song)



song()
