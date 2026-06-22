from collections import Counter

def maxNumberOfBalloons(text):
    cnt = Counter(text)

    return min(
        cnt['b'],
        cnt['a'],
        cnt['l'] // 2,
        cnt['o'] // 2,
        cnt['n']
    )

text = input("Enter text: ")
print("Maximum balloons:", maxNumberOfBalloons(text))