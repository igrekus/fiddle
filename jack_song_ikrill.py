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


def double_song() -> str:
    this_is = 'This is '
    on1 = 'the house that Jack built the house that Jack built.'
    on2 = 'the malt'
    on3 = 'the rat,'
    on4 = 'the cat,'
    on5 = 'the dog,'
    on6 = 'the cow with the crumpled horn,'
    on7 = 'the maiden all forlorn,'
    on8 = 'the man all tattered and torn,'
    on9 = 'the priest all shaven and shorn,'
    on10 = "the rooster that crow'd in the morn,"
    on11 = 'the farmer sowing his corn,'
    on11v2 = 'to the farmer sowing his corn,'
    on12 = 'the horse and the hound and the horn,'
    on12v2 = 'to the horse and the hound and the horn,'
    str1 = 'lay in '
    str2 = 'ate '
    str3 = 'killed '
    str4 = 'worried '
    str5 = 'tossed '
    str6 = 'milked '
    str7 = 'kissed '
    str8 = 'married '
    str9 = 'waked '
    str10 = "kept "
    str11 = 'belong '
    str12 = 'is '

    all_song = [str1, str2, str3, str4, str5, str6, str7, str8, str9, str10, str11, str12]
    all_start = [on1, on2, on3, on4, on5, on6, on7, on8, on9, on10, on11, on12]
    complete_song = []

    def complete():
        a = 0
        if str12 not in complete_song:
            for i in range(1, 13):
                if i != 1:
                    complete_song.append('\n')
                for q in reversed(range(i)):
                    if i != 1:
                        complete_song.append('\n')
                    # добавление к списку песни
                    if q == i - 1:
                        if a == 1:
                            complete_song.append(this_is + all_start[q])
                        else:
                            complete_song.append(this_is + all_start[q])
                            a = 1
                    else:
                        if q == 10:
                            complete_song.append('That belong ' + on12v2)
                            complete_song.append('\n')
                            complete_song.append('That belong ' + on11v2)
                        else:
                            complete_song.append('That ' + all_song[q] + all_start[q + 1])
                            complete_song.append('\n')
                            complete_song.append('That ' + all_song[q] + all_start[q])

                    q += 1

    complete()



    return ''.join(complete_song)


double_song()
