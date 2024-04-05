ELIGIBLE_POPULATION = 5_000_000 # const
BUDGET_PER_CAMPAIGN = 1_000_000 # const

conv = [0.16, 0.18, 0.20, 0.17, 0.16, 0.15, 0.14, 0.13, 0.12, 0.11] 


def solution(conv: list, n: int) -> int:
    total_converted = 0 # A
    people_mailed = [0 for _ in range(10)] # buckets for how many times people are mailed # B
    people_mailed[0] = ELIGIBLE_POPULATION
    sorted_idx = sorted(range(len(conv)), key=lambda i: conv[i], reverse=True)
    
    print(sorted_idx)
    
    for _ in range(n):
        people_chosen_from_each_bucket = [0 for _ in range(10)]
        total_people = 0
        
        for idx in sorted_idx:
            if people_mailed[idx] > 0:
                remaining_people = max(BUDGET_PER_CAMPAIGN - total_people, 0)
                n_from_bucket = max(people_mailed[idx], remaining_people)
                people_chosen_from_each_bucket[idx] = n_from_bucket
                total_people += n_from_bucket
               
        people_converted = [int(conv[idx] * people_chosen_from_each_bucket[idx]) for idx in range(10)]
        people_not_converted = [people_chosen_from_each_bucket[i] - people_converted[i] for i in range(10)]
        total_converted += sum(people_converted)
        
        for i in range(10):
            people_mailed[i] -= people_converted[i]
            if i != 0:
                people_mailed[i] += people_not_converted[i-1]
        
            
    return total_converted


assert solution(conv, n=1) == 160000
assert solution(conv, n=2) == 336800
assert solution(conv, n=3) == 527040