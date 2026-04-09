"""
Main entry point for the Real-Time Chat Analytics System.
"""

import subprocess
import os
import time
import sys

def main():
    """Launches the Streamlit dashboard and API server."""
    print("🚀 Starting Real-Time Chat Analytics System...")
    
    # Path to the dashboard and api scripts
    project_root = os.path.dirname(os.path.abspath(__file__))
    dashboard_path = os.path.join(project_root, "dashboard", "dashboard.py")
    api_path = os.path.join(project_root, "api", "main.py")
    
    # Environment with project root in PYTHONPATH
    env = os.environ.copy()
    if "PYTHONPATH" in env:
        env["PYTHONPATH"] = project_root + os.pathsep + env["PYTHONPATH"]
    else:
        env["PYTHONPATH"] = project_root

    processes = []
    try:
        # 1. Start FastAPI server
        print("🌐 Starting API Server...")
        api_proc = subprocess.Popen(
            [sys.executable, "-m", "uvicorn", "api.main:app", "--reload"],
            env=env,
            cwd=project_root
        )
        processes.append(api_proc)
        
        # Give API some time to start
        time.sleep(2)
        
        # 2. Start Streamlit dashboard
        print("📊 Starting Dashboard...")
        streamlit_proc = subprocess.Popen(
            ["python", "-m", "streamlit", "run", dashboard_path],
            env=env
        )
        processes.append(streamlit_proc)
        
        # Wait for processes
        for p in processes:
            p.wait()
            
    except KeyboardInterrupt:
        print("\n👋 System shut down.")
        for p in processes:
            p.terminate()

if __name__ == "__main__":
    main()
