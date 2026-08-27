#!/usr/bin/env bash
#
# natalie_run.sh — one-command runner for the Natalie drug-comparison agent.
#
# Usage:
#   ./natalie_run.sh            # setup + run 2 example comparisons + launch app
#   ./natalie_run.sh setup      # create venv + install dependencies only
#   ./natalie_run.sh examples   # run the documented example comparisons only
#   ./natalie_run.sh app        # launch the Streamlit web app only
#   ./natalie_run.sh compare aspirin ibuprofen   # one-off CLI comparison
#
# The Gemini API key is read from the .env file in this folder.

set -euo pipefail

# Always operate from the directory this script lives in.
SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
cd "$SCRIPT_DIR"

VENV_DIR="$SCRIPT_DIR/natalie_venv"
PYTHON_BIN="${PYTHON_BIN:-python3}"

# ---------------------------------------------------------------------------
# Load .env
# ---------------------------------------------------------------------------
load_env() {
  if [[ ! -f .env ]]; then
    echo "❌ No .env file found. Create one with: GEMINI_API_KEY=your_key"
    exit 1
  fi
  # Export every non-comment line in .env.
  set -a
  # shellcheck disable=SC1091
  source .env
  set +a

  if [[ -z "${GEMINI_API_KEY:-}" || "${GEMINI_API_KEY}" == "PUT_YOUR_KEY_HERE" ]]; then
    echo "❌ GEMINI_API_KEY is not set in .env (still the placeholder)."
    echo "   Edit .env and paste your key from https://aistudio.google.com/apikey"
    exit 1
  fi
  echo "✅ Loaded Gemini API key from .env (…${GEMINI_API_KEY: -4})."
}

# ---------------------------------------------------------------------------
# Setup: venv + deps
# ---------------------------------------------------------------------------
do_setup() {
  if [[ ! -d "$VENV_DIR" ]]; then
    echo "🐍 Creating virtual environment (natalie_venv)…"
    "$PYTHON_BIN" -m venv "$VENV_DIR"
  fi
  # shellcheck disable=SC1091
  source "$VENV_DIR/bin/activate"
  echo "📦 Installing dependencies…"
  pip3 install --quiet --upgrade pip
  pip3 install --quiet -r requirements.txt
  echo "✅ Dependencies installed."
}

activate_venv() {
  if [[ ! -d "$VENV_DIR" ]]; then
    do_setup
  else
    # shellcheck disable=SC1091
    source "$VENV_DIR/bin/activate"
  fi
}

# ---------------------------------------------------------------------------
# Actions
# ---------------------------------------------------------------------------
do_examples() {
  echo "🔬 Running documented example comparisons…"
  python3 natalie_examples.py
  echo "📄 See natalie_examples.md for the written results."
}

do_app() {
  echo "🚀 Launching Streamlit app at http://localhost:8501 …"
  echo "   (Press Ctrl+C to stop.)"
  streamlit run natalie_app.py
}

do_compare() {
  local a="${1:-}"; local b="${2:-}"
  if [[ -z "$a" || -z "$b" ]]; then
    echo "Usage: ./natalie_run.sh compare <drug_a> <drug_b>"
    exit 1
  fi
  python3 natalie_agent.py "$a" "$b"
}

# ---------------------------------------------------------------------------
# Dispatch
# ---------------------------------------------------------------------------
CMD="${1:-all}"

case "$CMD" in
  setup)
    load_env
    do_setup
    ;;
  examples)
    load_env
    activate_venv
    do_examples
    ;;
  app)
    load_env
    activate_venv
    do_app
    ;;
  compare)
    load_env
    activate_venv
    shift
    do_compare "$@"
    ;;
  all)
    load_env
    do_setup
    do_examples
    echo ""
    echo "▶️  Now launching the web app. Open http://localhost:8501"
    do_app
    ;;
  *)
    echo "Unknown command: $CMD"
    echo "Usage: ./natalie_run.sh [setup|examples|app|compare <a> <b>]"
    exit 1
    ;;
esac
