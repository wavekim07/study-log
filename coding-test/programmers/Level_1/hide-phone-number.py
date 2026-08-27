def solution(phone_number):
    last_number = phone_number[-4:]
    star_count = len(phone_number) - 4
    stars = "*" * star_count
    answer = stars + last_number
    return answer