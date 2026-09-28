"""Example demonstrating Smith-Waterman local sequence alignment."""
from client import SmithWatermanAligner

def main():
    seq1 = "ACACACTA"
    seq2 = "AGCACACA"
    res = SmithWatermanAligner.align(seq1, seq2)
    print("Local Alignment Results:")
    print("  Score:", res["score"])
    print("  Align 1:", res["align1"])
    print("  Align 2:", res["align2"])

if __name__ == "__main__":
    main()
