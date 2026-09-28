# Smith-Waterman Local Sequence Alignment Skill

Dynamic programming algorithm for optimal local sequence alignment between biological sequences.

```mermaid
flowchart TD
    Init["Initialize Score Matrix H(i, j) with 0"] --> Recurse["Compute max(0, Match, Del, Ins)"]
    Recurse --> MaxVal["Identify Global Max in Matrix"]
    MaxVal --> Traceback["Traceback to 0 Boundary"]
    Traceback --> Subseq["Optimal Local Homology Alignment"]
```

## Features
- **100% Python Standard Library**: No external dependencies.
- **Customizable Scoring**: Configurable match reward, mismatch, and linear gap penalties.
- **MCP Server Ready**: Direct stdio integration for computational genomics.
