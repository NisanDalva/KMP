from Utilities import Array, String


class KMP:
    def __init__(self, P=None, T=None, P_file_name=None, T_file_name=None,
                 m=None, n=None, print_occurrences=True) -> None:
        """
        :param P: the pattern as an argument, must be str
        :param T: all text as an argument, must be str

        :param P_file_name: reading the pattern from a txt file. default is None
        :param T_file_name: reading the text from a txt file. default is None

        :param m: optional, default is None. if None - the algorithm will use the whole pattern
                otherwise, the algorithm will use indexes 1 to m. m must be greater then 1 and less then the length of P

        :param n:optional, default is None. if None - the algorithm will use the whole text
                otherwise, the algorithm will use indexes 1 to n. n must be greater then 1 and less then the length of T

        :param print_occurrences: do print the indexes where the pattern occurs, default is True
        *NOTE that P and T has higher priority if they comes directly to the function than from a txt file
        """
        if P is None:
            if P_file_name is None:
                raise ValueError('you need to specify P in order to the KMP will work')
            else:
                with open(P_file_name, 'rt') as f:
                    P = String(f.read().replace('\n', '').replace(' ', ''))
        else:
            P = String(P)

        if T is None:
            if T_file_name is None:
                raise ValueError('you need to specify T in order to the KMP will work')
            else:
                with open(T_file_name, 'rt') as f:
                    T = String(f.read().replace('\n', '').replace(' ', ''))
        else:
            T = String(T)

        m = len(P) if m is None else m
        n = len(T) if n is None else n

        self.P = P
        self.T = T
        self.m = m
        self.n = n
        self.print_occurrences = print_occurrences
        self.prefixes = Array([0] * m)
        self.tau = Array([0] * n)

    def __compute_prefix_function(self) -> None:
        self.prefixes[1] = 0
        k = 0
        for q in range(2, self.m + 1):
            while k > 0 and self.P[k + 1] != self.P[q]:
                k = self.prefixes[k]
            if self.P[k + 1] == self.P[q]:
                k += 1
            self.prefixes[q] = k

    def __matcher(self) -> int:
        self.__compute_prefix_function()
        num_occurrences = 0
        q = 0
        for i in range(1, self.n + 1):
            while q > 0 and self.P[q + 1] != self.T[i]:
                q = self.prefixes[q]
            if self.P[q + 1] == self.T[i]:
                q += 1
            self.tau[i] = q
            if q == self.m:
                if self.print_occurrences:
                    print(f'pattern occurs at index {i - self.m + 1}')
                q = self.prefixes[q]
                num_occurrences += 1

        return num_occurrences

    def run(self) -> int:
        return self.__matcher()
