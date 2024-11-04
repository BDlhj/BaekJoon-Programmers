def solution(genres, plays):
    answer = []
    
    genre_set = set(genres)
    genre_total_play = {genre: 0 for genre in genre_set}
    genre_play_idx = [(genre_play[0], genre_play[1], idx) for idx, genre_play in enumerate(zip(genres, plays))]

    for info in genre_play_idx:
        genre_total_play[info[0]] += info[1]
    
    genre_total_play_list = sorted(genre_total_play.items(), key=lambda x: x[1], reverse=True)
    genre_play_idx.sort(key=lambda x: (-genre_total_play[x[0]], -x[1], x[2]))

    answer_genre_count = {genre: 0 for genre in genre_set}
    for i in genre_play_idx:
        if answer_genre_count[i[0]] < 2:
            answer_genre_count[i[0]] += 1
            answer.append(i[2])
    
    return answer