'''
# 베스트앨범

## 문제 설명
스트리밍 사이트에서 장르 별로 가장 많이 재생된 노래를 두 개씩 모아 베스트 앨범을 출시하려 합니다. 노래는 고유 번호로 구분하며, 노래를 수록하는 기준은 다음과 같습니다.

1. 속한 노래가 많이 재생된 장르를 먼저 수록합니다.
2. 장르 내에서 많이 재생된 노래를 먼저 수록합니다.
3. 장르 내에서 재생 횟수가 같은 노래 중에서는 고유 번호가 낮은 노래를 먼저 수록합니다.
노래의 장르를 나타내는 문자열 배열 genres와 노래별 재생 횟수를 나타내는 정수 배열 plays가 주어질 때, 베스트 앨범에 들어갈 노래의 고유 번호를 순서대로 return 하도록 solution 함수를 완성하세요.

## 제한사항
genres[i]는 고유번호가 i인 노래의 장르입니다.
plays[i]는 고유번호가 i인 노래가 재생된 횟수입니다.
genres와 plays의 길이는 같으며, 이는 1 이상 10,000 이하입니다.
장르 종류는 100개 미만입니다.
장르에 속한 곡이 하나라면, 하나의 곡만 선택합니다.
모든 장르는 재생된 횟수가 다릅니다.
'''


def solution(genres, plays):
    answer = []
    music_dict = {}
    music_dict2 = {}
    for i in range(len(plays)):
        genre = genres[i]
        if genre in music_dict:
            music_dict[genre].append((i, plays[i]))
        else:
            music_dict[genre] = [(i, plays[i])]

        if genre in music_dict2:
            music_dict2[genre] += plays[i]
        else:
            music_dict2[genre] = plays[i]

    for key in music_dict.keys():
        music_dict[key] = sorted(
            music_dict[key], key=lambda x: x[1], reverse=True)

    genre_rank = sorted(music_dict2.items(), key=lambda x: x[1], reverse=True)

    for genre in genre_rank:
        cnt = 0
        for music in music_dict[genre[0]]:
            answer.append(music[0])
            cnt += 1
            if cnt == 2:
                break

    return answer
