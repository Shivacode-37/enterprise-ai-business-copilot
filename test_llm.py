from app.llm.summary_chain import generate_ai_summary

sample_metrics = {
    "health_score": 82,
    "profit_margin_pct": 18.4,
    "loss_order_pct": 9.5,
    "highest_risk_category": "Furniture",
    "highest_loss_ratio": 32.8,
    "risk_level": "Moderate"
}

response = generate_ai_summary(sample_metrics)

print(response)
