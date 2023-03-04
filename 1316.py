
n = int(input())
answer = 0

for _ in range(n):
    word = input()
    w_list = list(word)
    word_bank = [] 

    for w in word: # a c a
        if w not in word_bank: # 없으면
            word_bank.append(w)
            continue
        else: #있으면
            if not word_bank[-1] == w:
                answer += 1
                break

print(n - answer)

        
        
'''
입력
3
happy
new
year

4
aba
abab
abcabc
a

5
ab
aa
aca
ba
bb
'''