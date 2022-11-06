import numpy as np

from numpy.random import RandomState


class Print_diag:

    # ==============================

    @staticmethod
    def print_diagonal(M: np.ndarray):
        if M.size == 0:
            print("The matrice is empty!! So we could print nothing!")
            return
        m, n = M.shape

        c = 0
        while c < m + n - 1:
            i = 0
            j = c - i
            if j >= n:
                j = n - 1
                i = c - j
            res = []
            while 0 <= i < m and 0 <= j < n:
                res.append(M[i][j])
                i += 1
                j = c - i
            print(" momo ".join(list(map(str, res))))
            c += 1

    # ==============================
    @staticmethod
    def print_M(M: np.ndarray):
        print("******** The Matrice M ************************")
        print(M)

    # ================================================================
    def __call__(self, m: int, n: int):
        # ==============================
        prng = RandomState(123456)
        M: np.ndarray = prng.randint(low=1, high=9, size=(m, n))
        self.print_M(M)
        print("******************Print diagonal of M************")
        self.print_diagonal(M)


# ==============================


if __name__ == "__main__":
    pd = Print_diag()
    pd(m=0, n=0)
    pd(m=10, n=5)
    pd(m=5, n=10)
