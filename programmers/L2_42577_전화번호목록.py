def solution(phone_book):
    phone_book.sort()  # 숫자가 앞에서 같으면 같을 수록 근처에 있음
    for p1, p2 in zip(phone_book, phone_book[1:]):
        if p2.startswith(p1):
            return False
    return True
