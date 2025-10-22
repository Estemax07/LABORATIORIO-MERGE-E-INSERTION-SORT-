import random, time, statistics, sys
sys.setrecursionlimit(1_000_000)

def randomized_quicksort(a): _rqs(a, 0, len(a) - 1)
def _rqs(a, lo, hi):
    if lo < hi:
        k = random.randint(lo, hi)
        a[k], a[hi] = a[hi], a[k] 
        p = _lomuto(a, lo, hi)
        _rqs(a, lo, p - 1)
        _rqs(a, p + 1, hi)
def _lomuto(a, lo, hi):
    p = a[hi]; i = lo
    for j in range(lo, hi):
        if a[j] <= p:
            a[i], a[j] = a[j], a[i]; i += 1
    a[i], a[hi] = a[hi], a[i]
    return i


sizes = [10000000]  #Cambia los tamaños aquí (p. ej. [100, 1_000, 10_000])
REPS = 100     #Número de repeticiones
VAL_MAX = 10_000_000
random.seed(42)

def print_five_cols(times, n, alg, cols=5, per_col=20):
    columns = [times[i*per_col:(i+1)*per_col] for i in range(cols)]
    rows = max(len(c) for c in columns)
    print(f"\n=== n={n} — {alg} — {len(times)} ejecuciones ===")
    headers = "    ".join([f"exp#{i+1:>2}   time_s" for i in range(cols)])
    print(headers)
    for r in range(rows):
        row_str = []
        for c, col in enumerate(columns):
            if r < len(col):
                exp_idx = c*per_col + r + 1
                row_str.append(f"{exp_idx:>4} {col[r]:>10.6f}")
            else:
                row_str.append(" " * 15)
        print("    ".join(row_str))
    print(f"\nPROMEDIO ({len(times)}) {alg} n={n}: {statistics.mean(times):.6f} s\n")

print("Salida en 5 columnas (20 + 20 + 20 + 20 + 20)\n")
for n in sizes:
    base = [random.randint(0, VAL_MAX) for _ in range(n)]
    tiempos = []
    for _ in range(REPS):
        arr = base.copy()
        t0 = time.perf_counter(); randomized_quicksort(arr); t1 = time.perf_counter()
        tiempos.append(t1 - t0)
    print_five_cols(tiempos, n, "RandomizedQuickSort", cols=5, per_col=20)

