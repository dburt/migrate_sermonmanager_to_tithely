import pandas as pd
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import List, Dict, Any, Optional
import os

# Import the refactored TithelyManager
from tithely_manager import TithelyManager

# --- CONFIGURATION ---
# Assuming the server is run from the 'mcp_server' directory
SERMONS_CSV_PATH = "../sermons.csv"
TITHELY_EMAIL = os.environ.get("TITHELY_EMAIL")
TITHELY_PASSWORD = os.environ.get("TITHELY_PASSWORD")
BRAVE_EXECUTABLE_PATH = "/usr/bin/brave-browser"
# ---------------------

app = FastAPI(
    title="MCP Server",
    description="A server to provide an API for interacting with sermon data from Tithely and local files.",
    version="0.2.0",
)

# --- In-memory Data & Global Manager ---
sermons_df = None
manager = TithelyManager(
    email=TITHELY_EMAIL,
    password=TITHELY_PASSWORD,
    brave_executable_path=BRAVE_EXECUTABLE_PATH,
    headless=True  # Run headless for server
)

# --- Server Lifecycle Events ---
@app.on_event("startup")
def startup_event():
    """On server startup, load local data and start the browser."""
    global sermons_df
    # Load local CSV data
    try:
        sermons_df = pd.read_csv(SERMONS_CSV_PATH)
        sermons_df = sermons_df.where(pd.notnull(sermons_df), None)
        print(f"Successfully loaded {len(sermons_df)} sermons from {SERMONS_CSV_PATH}")
    except FileNotFoundError:
        print(f"ERROR: Sermons CSV file not found at {SERMONS_CSV_PATH}")
        sermons_df = pd.DataFrame()
    
    # Start browser and login to Tithely
    if TITHELY_EMAIL and TITHELY_PASSWORD:
        try:
            manager.start_browser()
            manager.login()
        except Exception as e:
            print(f"CRITICAL ERROR: Could not start browser or log in to Tithely. Error: {e}")
            # Note: The server will still run, but Tithely endpoints will fail.
    else:
        print("WARNING: Tithely credentials not found. Tithely-related endpoints will not be available.")


@app.on_event("shutdown")
def shutdown_event():
    """On server shutdown, stop the browser."""
    manager.stop_browser()

# --- Pydantic Models for API ---
class PlaywrightAction(BaseModel):
    action: str
    selector: Optional[str] = None
    text: Optional[str] = None

class ExploreRequest(BaseModel):
    url: str
    actions: List[PlaywrightAction]

# --- API Endpoints ---
@app.get("/")
def read_root():
    return {"message": "Welcome to the MCP Server"}

# --- Local Data Endpoints ---
@app.get("/local-sermons", response_model=List[Dict[str, Any]])
def get_local_sermons(skip: int = 0, limit: int = 50):
    """Get a list of sermons from the local sermons.csv file."""
    if sermons_df is None or sermons_df.empty:
        raise HTTPException(status_code=503, detail="Local sermon data not loaded.")
    paginated_df = sermons_df.iloc[skip : skip + limit]
    return paginated_df.to_dict(orient="records")

@app.get("/local-sermon/{post_id}", response_model=Dict[str, Any])
def get_local_sermon_by_id(post_id: int):
    """Get a single sermon by its post_id."""
    if sermons_df is None or sermons_df.empty:
        raise HTTPException(status_code=503, detail="Local sermon data not loaded.")
    sermon = sermons_df[sermons_df["post_id"] == post_id]
    if sermon.empty:
        raise HTTPException(status_code=404, detail=f"Sermon with post_id {post_id} not found.")
    return sermon.to_dict(orient="records")[0]

# --- Tithely Endpoints ---
@app.post("/explore", response_model=List[Any])
def explore_tithely(request: ExploreRequest):
    """
    Navigate to a URL and perform a series of Playwright actions for exploration.
    """
    if not manager.page:
        raise HTTPException(status_code=503, detail="Tithely manager not available. Check server logs.")
    
    results = manager.explore(url=request.url, actions=[action.dict() for action in request.actions])
    return results

@app.get("/tithely/sermons", response_model=List[Dict[str, Any]])
def get_tithely_sermons(page: int = 1):
    """
    Get a single page of sermons from the main Tithely listing.
    """
    if not manager.page:
        raise HTTPException(status_code=503, detail="Tithely manager not available. Check server logs.")
    
    try:
        sermons = manager.create_main_listing_index(start_page=page, end_page=page)
        return sermons
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"An error occurred while fetching sermons: {e}")

@app.get("/tithely/sermons/{sermon_slug}", response_model=Dict[str, Any])
def get_tithely_sermon_details(sermon_slug: str):
    """
    Get detailed information for a single sermon from its detail page.
    """
    if not manager.page:
        raise HTTPException(status_code=503, detail="Tithely manager not available. Check server logs.")
    
    sermon_url = f"/media/{sermon_slug}"
    try:
        details = manager.get_sermon_details(sermon_url=sermon_url, slug=sermon_slug)
        return details
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"An error occurred while fetching sermon details: {e}")
