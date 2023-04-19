melodies_replace = {"A#": "H", "C#": "I", "D#": "J", "F#": "K", "G#": "L"}


def transform_melody(melody):
    for k, v in melodies_replace.items():
        melody = melody.replace(k, v)
    return melody


def solution(m, musicinfos):
    melody_list = []
    m = transform_melody(m)

    for idx, musicinfo in enumerate(musicinfos):
        start, end, title, melody = musicinfo.split(",")
        melody = transform_melody(melody)
        startHH, startMM = list(map(int, start.split(":")))
        endHH, endMM = list(map(int, end.split(":")))

        # 재생 시간 구하기
        time = (endHH * 60 + endMM) - (startHH * 60 + startMM)
        q, r = divmod(time, len(melody))
        total_melody = melody * q + melody[:r]
        print(q, r, total_melody)

        if m in total_melody:
            melody_list.append([idx, time, title])  # 순서, 재생시간, 음악 제목
        # 1. 조건이 일치하는 음악이 여러 개일 때는 재생시간이 제일 긴 음악 제목 반환 (재생시간 내림차순)
        # 2. 재생 시간도 같을 경우 먼저 입력된 음악 제목 반환

    if not melody_list:
        return "(None)"
    if len(melody_list) == 1:
        return melody_list[0][2]
    return sorted(melody_list, key=lambda x: (-x[1], x[0]))[0][2]