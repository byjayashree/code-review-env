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

## 👁️ Observation Space

The environment provides:
- `code`: Python code snippet that the agent must review

---

## ⚙️ Action Space

Agent outputs:
- `issues`: list of detected problems
- `quality_score`: score between 0 and 1
- `suggestion`: improvement advice

---

## 🧮 Reward Function

Weighted scoring:
- Issues match → 50%
- Quality score → 20%
- Suggestion relevance → 30%

Provides partial rewards for incremental progress.

---

## ⚙️ OpenEnv Compliance

This environment follows the OpenEnv interface:
- `reset()` → returns initial observation
- `step(action)` → returns observation, reward, done, info
- `state()` → returns current environment state

---

## 🤖 Inference

The environment supports LLM-based agents via OpenAI-compatible API.

Fallback logic ensures reproducible outputs even when API fails.

---

## 🐳 Setup

```bash
pip install -r requirements.txt
python inference.py
```
---

## 📊 Baseline Results

- Easy: ~0.96
- Medium: ~0.67
- Hard: ~0.65

These scores demonstrate the environment's ability to provide meaningful, non-binary reward signals across different difficulty levels.

---

## ✨ Personal Note

- This project was built under strict time constraints alongside ongoing exams, which made the process both challenging yet extremely fulfilling.

- While working on this environment, I gained a deeper understanding of how reinforcement learning environments are structured — especially how agents interact through `step()` and `reset()` functions, and how meaningful reward systems are designed.

- This project also gave me hands-on exposure to real-world workflows such as environment design, debugging, structured evaluation, and deployment practices. It was my first experience building something that closely resembles how AI systems are tested and evaluated in practice.

- Overall, this was not just a submission, but a strong learning experience that pushed me to understand both the *concepts* and the *implementation* side of RL systems.