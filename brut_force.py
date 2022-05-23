import heapq
from itertools import combinations


def closest_subset(target_kcal, meal_list, num_meals):
    # Wygeneruj plan jedzenia na jeden dzień
    # target_kcal - docelowa liczba kalorii
    # meal_list - lista posiłków z których zostanie wygenerowany jadłospis
    # num_meals - ile posiłków użytkownik chce zjeść
    return (min((
        c
        for i in range(num_meals, num_meals+1)
        for c in combinations(meal_list, i)
    ), key=lambda x: abs(target_kcal - sum(meal['kcal'] for meal in x))))


def top_n_closest_subset(target_kcal, meal_list, num_meals, num_days=7):
    # Wygeneruj plan jedzenia na kilka dni
    # target_kcal - docelowa liczba kalorii
    # meal_list - lista posiłków z których zostanie wygenerowany jadłospis
    # num_meals - ile posiłków użytkownik chce zjeść
    # num_days - na ile dni wygernerować jadłospis
    return (heapq.nsmallest(num_days, (
        c
        for i in range(num_meals, num_meals+1)
        for c in combinations(meal_list, i)
    ), key=lambda x: abs(target_kcal - sum(meal['kcal'] for meal in x))))

def brute_force(target_kcal, meal_list, num_meals):
    ans = []
    for m in top_n_closest_subset(target_kcal, meal_list, num_meals):
        ans.append([i["id"] for i in m])
    return ans