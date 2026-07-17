from app.analytics.metrics_engine import compute_advanced_metrics
from app.services.summary_service import summarize_business
from app.llm.summary_chain import generate_ai_summary

class AnalysisService:
    @staticmethod
    def analyze(df):
        metrics = compute_advanced_metrics(df)
        summary = summarize_business(metrics)
        ai_summary = generate_ai_summary(summary)

        return{
            "metrics": metrics,
            "summary": summary,
            "ai_summary" : ai_summary
        }


