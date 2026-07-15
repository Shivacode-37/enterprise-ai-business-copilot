from app.analytics.metrics_engine import compute_advanced_metrics
from app.services.summary_service import summarize_business

class AnalysisService:
    @staticmethod
    def analyze(df):
        metrics = compute_advanced_metrics(df)
        summary = summarize_business(metrics)

        return{
            "metrics": metrics,
            "summary": summary
        }


