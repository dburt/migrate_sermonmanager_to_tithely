import pandas as pd
from fastapi import FastAPI, HTTPException
from typing import List, Dict, Any

# Configuration
# Assuming the server is run from the 'mcp_server' directory
SERMONS_CSV_PATH = "../sermons.csv"

app = FastAPI(
    title="MCP Server",
    description="A server to provide an API for interacting with sermon data from Tithely and local files.",
    version="0.1.0",
)

# In-memory cache for the local data
sermons_df = None

@app.on_event("startup")
def load_local_data():
    """Load the sermons CSV into a pandas DataFrame at startup."""
    global sermons_df
    try:
        sermons_df = pd.read_csv(SERMONS_CSV_PATH)
        # Convert to a more JSON-friendly format, handling NaN values
        sermons_df = sermons_df.where(pd.notnull(sermons_df), None)
        print(f"Successfully loaded {len(sermons_df)} sermons from {SERMONS_CSV_PATH}")
    except FileNotFoundError:
        print(f"ERROR: Sermons CSV file not found at {SERMONS_CSV_PATH}")
        sermons_df = pd.DataFrame()


@app.get("/")
def read_root():
    return {"message": "Welcome to the MCP Server"}


@app.get("/local-sermons", response_model=List[Dict[str, Any]])
def get_local_sermons(skip: int = 0, limit: int = 50):
    """
    Get a list of sermons from the local sermons.csv file.
    Supports pagination using `skip` and `limit`.
    """
    if sermons_df is None or sermons_df.empty:
        raise HTTPException(status_code=503, detail="Local sermon data not loaded. Check server logs.")
    
    paginated_df = sermons_df.iloc[skip : skip + limit]
    return paginated_df.to_dict(orient="records")


@app.get("/local-sermon/{post_id}", response_model=Dict[str, Any])
def get_local_sermon_by_id(post_id: int):
    """
    Get a single sermon by its post_id.
    """
    if sermons_df is None or sermons_df.empty:
        raise HTTPException(status_code=503, detail="Local sermon data not loaded. Check server logs.")

    sermon = sermons_df[sermons_df["post_id"] == post_id]
    
    if sermon.empty:
        raise HTTPException(status_code=404, detail=f"Sermon with post_id {post_id} not found.")
        
    return sermon.to_dict(orient="records")[0]