from app.analytics.metrics_engine import compute_advanced_metrics
from app.services.summary_service import summarize_business
from app.llm.summary_chain import generate_ai_summary

from app.schema.detector import detect_schema
from app.schema.mapper import validate_mapping


class AnalysisService:
    @staticmethod
    def analyze(df):

        mapping = detect_schema(df.columns.tolist())
        mapping = validate_mapping(
            mapping,
            df.columns.tolist(),
        )

        metrics = compute_advanced_metrics(
            df,
            mapping,
        )

        summary = summarize_business(metrics)
        ai_summary = generate_ai_summary(summary)

        return {
            "metrics": metrics,
            "summary": summary,
            "ai_summary": ai_summary,
        }
