"""
Main entry point for the Real-Time Chat Analytics System.
"""

import subprocess
import os

def main():
    """Launches the Streamlit dashboard."""
    print("🚀 Starting Real-Time Chat Analytics System...")
    
    # Path to the dashboard script
    dashboard_path = os.path.join(os.path.dirname(__file__), "dashboard.py")
    
    # Run Streamlit dashboard
    # This will now also handle starting the background analytics engine
    try:
        subprocess.run(["streamlit", "run", dashboard_path], check=True)
    except KeyboardInterrupt:
        print("\n👋 System shut down.")

if __name__ == "__main__":
    main()
