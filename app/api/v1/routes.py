from io import StringIO

import pandas as pd
from fastapi import APIRouter, File, HTTPException, UploadFile, status

from app.core.config import settings
from app.schema.response import AnalysisResponse
from app.services.analysis_service import AnalysisService
from app.utils.json_utils import make_json_serializable



router = APIRouter()


@router.get("/health", tags=["Health"])
def health():
    return {
        "status": "ok",
        "app": settings.APP_NAME,
        "version": settings.APP_VERSION,
    }


@router.post(
    "/analyze",
    response_model=AnalysisResponse,
    tags=["Analysis"],
)
async def analyze(file: UploadFile = File(...)):
    # Validate file type
    if not file.filename.lower().endswith(".csv"):
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Only CSV files are supported.",
        )

    try:
        # Read uploaded file
        contents = await file.read()
        df = pd.read_csv(StringIO(contents.decode("utf-8")))

        if df.empty:
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail="Uploaded CSV is empty.",
            )

        # Run analysis
        result = AnalysisService.analyze(df)
        result = make_json_serializable(result)

        return AnalysisResponse(
    status="success",
    summary=result["summary"],
    executive_report=result["executive_report"],
    metrics=result["metrics"],
)

    except HTTPException:
        raise

    except pd.errors.ParserError:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Invalid CSV format.",
        )

    except UnicodeDecodeError:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Unable to decode CSV. Please upload a UTF-8 encoded file.",
        )

    except Exception as e:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=f"Analysis failed: {str(e)}",
        )
