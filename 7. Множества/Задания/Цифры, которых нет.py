print(''.join(sorted(list(n), reverse=True)) if len(n := set("1234567890").difference(set(input()))) > 0 else "NO")
