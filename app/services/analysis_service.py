from app.analytics.metrics_engine import compute_advanced_metrics
from app.services.summary_service import summarize_business

from app.reports.executive_report import generate_executive_report

from app.schema.detector import detect_schema
from app.schema.mapper import validate_mapping
from app.preprocessing.normalize import normalize_columns


class AnalysisService:
    @staticmethod
    def analyze(df):

        # Normalize FIRST
        df = normalize_columns(df)

        mapping = detect_schema(df.columns.tolist())
        mapping = validate_mapping(
            mapping,
            df.columns.tolist(),
        )

        metrics = compute_advanced_metrics(
            df,
            mapping,
        )
        print("\n=== DISCOUNT ANALYSIS ===")
        print(metrics["discount_analysis"].columns)
        print(metrics["discount_analysis"].head())
        print("\n=== STRUCTURAL INEFFICIENCY ===")
        print(metrics["structural_inefficiency_by_category"].columns)
        print(metrics["structural_inefficiency_by_category"].head())

        print("\n=== STRUCTURAL COLLAPSE ===")
        print(metrics["structural_collapse_by_category"].columns)
        print(metrics["structural_collapse_by_category"].head())

        summary = summarize_business(metrics)
        executive_report = generate_executive_report(metrics)

        return {
            "metrics": metrics,
            "summary": summary,
            "executive_report": executive_report,
        }
