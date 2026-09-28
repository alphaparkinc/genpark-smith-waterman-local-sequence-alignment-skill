"""MCP stdio server for Smith-Waterman Local Alignment."""
import sys
import json

if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8")

from client import SmithWatermanAligner

def handle_rpc(request):
    req_id = request.get("id")
    method = request.get("method")
    params = request.get("params", {})

    if method == "tools/list":
        return {
            "jsonrpc": "2.0",
            "id": req_id,
            "result": {
                "tools": [
                    {
                        "name": "smith_waterman_align",
                        "description": "Perform local genomic sequence alignment using Smith-Waterman DP",
                        "inputSchema": {
                            "type": "object",
                            "properties": {
                                "seq1": {"type": "string"},
                                "seq2": {"type": "string"},
                                "match_score": {"type": "integer", "default": 2},
                                "mismatch_penalty": {"type": "integer", "default": -1},
                                "gap_penalty": {"type": "integer", "default": -1}
                            },
                            "required": ["seq1", "seq2"]
                        }
                    }
                ]
            }
        }
    elif method == "tools/call":
        name = params.get("name")
        args = params.get("arguments", {})
        if name == "smith_waterman_align":
            s1 = args.get("seq1", "")
            s2 = args.get("seq2", "")
            match = int(args.get("match_score", 2))
            mismatch = int(args.get("mismatch_penalty", -1))
            gap = int(args.get("gap_penalty", -1))
            res = SmithWatermanAligner.align(s1, s2, match, mismatch, gap)
            return {"jsonrpc": "2.0", "id": req_id, "result": res}
        return {"jsonrpc": "2.0", "id": req_id, "error": {"code": -32601, "message": f"Method {name} not found"}}
    return {"jsonrpc": "2.0", "id": req_id, "error": {"code": -32600, "message": "Invalid request"}}

def main():
    for line in sys.stdin:
        if not line.strip():
            continue
        try:
            req = json.loads(line)
            res = handle_rpc(req)
            sys.stdout.write(json.dumps(res) + "\n")
            sys.stdout.flush()
        except Exception as e:
            sys.stdout.write(json.dumps({"jsonrpc": "2.0", "error": {"code": -32700, "message": str(e)}}) + "\n")
            sys.stdout.flush()

if __name__ == "__main__":
    main()
