#!/usr/bin/env bash
# Launch the LeetCode Tutor website locally.
cd "$(dirname "$0")"
PORT="${1:-8765}"
echo "🎓 Starting LeetCode Tutor on http://localhost:$PORT"
echo "   Press Ctrl+C to stop."
echo ""
python3 -m http.server "$PORT"
