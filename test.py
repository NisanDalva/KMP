
from KMP import KMP

if __name__ == '__main__':
    print('-' * 50)
    kmp = KMP(P='aab', T='aababaabbaab', print_occurrences=True)

    print(f'P = {kmp.P}')
    print(f'T = {kmp.T}')
    print(f'm = {kmp.m}')
    print(f'n = {kmp.n}')

    num_of_occurrences = kmp.run()

    print(f'num_of_occurrences = {num_of_occurrences}')
    print(f'tau array: {kmp.tau}')
    print(f'prefixes array: {kmp.prefixes}')
    print('-' * 50)

    kmp = KMP(P='aa', T='aaaa', print_occurrences=True)

    print(f'P = {kmp.P}')
    print(f'T = {kmp.T}')
    print(f'm = {kmp.m}')
    print(f'n = {kmp.n}')

    num_of_occurrences = kmp.run()

    print(f'num_of_occurrences = {num_of_occurrences}')
    print(f'tau array: {kmp.tau}')
    print(f'prefixes array: {kmp.prefixes}')
    print('-' * 50)

    kmp = KMP(P_file_name='P_test.txt', T_file_name='T_test.txt', print_occurrences=True)

    print(f'P = {kmp.P}')
    print(f'T = {kmp.T}')
    print(f'm = {kmp.m}')
    print(f'n = {kmp.n}')

    num_of_occurrences = kmp.run()

    print(f'num_of_occurrences = {num_of_occurrences}')
    print(f'tau array: {kmp.tau}')
    print(f'prefixes array: {kmp.prefixes}')
    print('-' * 50)

    kmp = KMP(P='attcgtgtta', T_file_name='DNA.txt', print_occurrences=True)

    print(f'P = {kmp.P}')
    print(f'm = {kmp.m}')
    print(f'n = {kmp.n:,}')

    num_of_occurrences = kmp.run()

    print(f'num_of_occurrences = {num_of_occurrences}')
    print(f'prefixes array: {kmp.prefixes}')
    print('-' * 50)

