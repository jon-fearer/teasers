from typing import List


def knows(a: str, b: str) -> bool:
    return True


# O(N^2) solution
def find_celebrity(people: List[str]) -> str:
    celebrity: str
    for person in people:
        is_celebrity = True
        for other_person in people:
            # Ignore comparison of person to themselves
            if person == other_person:
                continue
            # If the person knows someone else, they are not the celebrity
            if knows(person, other_person):
                is_celebrity = False
        if is_celebrity:
            celebrity = person
            break
    return celebrity


# O(N) solution
def find_celebrity_fast(people: List[str]) -> str:
    celebrity: str
    for index, person in enumerate(people):
        continue
    return celebrity
