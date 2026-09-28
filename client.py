"""Smith-Waterman Local Sequence Alignment Algorithm.
100% Python Standard Library.
"""

class SmithWatermanAligner:
    """Performs optimal local alignment between two nucleotide or protein sequences."""
    @staticmethod
    def align(seq1, seq2, match_score=2, mismatch_penalty=-1, gap_penalty=-1):
        m, n = len(seq1), len(seq2)
        H = [[0] * (n + 1) for _ in range(m + 1)]
        max_score = 0
        max_pos = (0, 0)
        
        for i in range(1, m + 1):
            for j in range(1, n + 1):
                match = H[i-1][j-1] + (match_score if seq1[i-1] == seq2[j-1] else mismatch_penalty)
                delete = H[i-1][j] + gap_penalty
                insert = H[i][j-1] + gap_penalty
                score = max(0, match, delete, insert)
                H[i][j] = score
                if score > max_score:
                    max_score = score
                    max_pos = (i, j)
                    
        align1, align2 = [], []
        i, j = max_pos
        while i > 0 and j > 0 and H[i][j] > 0:
            current = H[i][j]
            match_val = match_score if seq1[i-1] == seq2[j-1] else mismatch_penalty
            if current == H[i-1][j-1] + match_val:
                align1.append(seq1[i-1])
                align2.append(seq2[j-1])
                i -= 1
                j -= 1
            elif current == H[i-1][j] + gap_penalty:
                align1.append(seq1[i-1])
                align2.append('-')
                i -= 1
            else:
                align1.append('-')
                align2.append(seq2[j-1])
                j -= 1
                
        return {
            "score": max_score,
            "align1": "".join(reversed(align1)),
            "align2": "".join(reversed(align2)),
            "start_pos": (i, j),
            "end_pos": max_pos
        }
