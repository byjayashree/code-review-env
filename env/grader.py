def grade(action, task):
    predicted_issues = action.get("issues", [])
    true_issues = task["issues"]

    #  Issue matching (core logic)
    match_count = sum(1 for issue in predicted_issues if issue in true_issues)
    issue_score = match_count / len(true_issues)

    #  Quality score (agent gives rating 0–1)
    predicted_quality = action.get("quality_score", 0)
    quality_score = min(max(predicted_quality, 0), 1)  # clamp between 0–1

    #  Suggestion scoring (simple keyword check)
    suggestion = action.get("suggestion", "").lower()

    keywords = ["secure", "avoid", "fix", "improve"]
    suggestion_score = 1.0 if any(word in suggestion for word in keywords) else 0.0

    #  FINAL WEIGHTED SCORE
    final_score = (
        0.5 * issue_score +
        0.2 * quality_score +
        0.3 * suggestion_score
    )

    return round(final_score, 2)