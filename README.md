#  Agentic Code Review Environment

## 🚀 Overview
This project implements a real-world reinforcement learning environment for automated code review using the OpenEnv framework.

The environment simulates how an AI agent evaluates code quality, detects issues, and provides improvement suggestions.

---

## 🎯 Tasks

### 🟢 Easy
Detect basic formatting issues (spacing, indentation)

### 🟡 Medium
Identify readability and structural problems

### 🔴 Hard
Detect security vulnerabilities and critical issues

---

## ⚙️ Action Space

Agent outputs:
- issues: list of detected problems
- quality_score: score between 0 and 1
- suggestion: improvement advice

---

## 🧮 Reward Function

Weighted scoring:
- Issues match → 50%
- Quality score → 20%
- Suggestion relevance → 30%

Provides partial rewards for incremental progress.

---

## 🤖 Inference

The environment supports LLM-based agents via OpenAI-compatible API.

Fallback logic ensures reproducible outputs even when API fails.

---

## 🐳 Setup

```bash
pip install -r requirements.txt
python inference.py