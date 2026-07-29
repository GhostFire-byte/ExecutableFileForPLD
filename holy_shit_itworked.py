import os
import shutil
import subprocess

# Replace with the exact path to your portable notepad++.exe
source_exe = r"C:\Users\T1112784Z\OneDrive - Ministry of Education (M365 T&L)\Desktop\cmder_mini\Cmder.exe"
alt_dir = r"C:\Windows\Tasks"
target_exe = os.path.join(alt_dir, "run.exe")

try:
    # Attempt to copy and run from the hidden system tasks folder
    shutil.copy(source_exe, target_exe)
    print("Successfully copied to C:\\Windows\\Tasks!")
    
    subprocess.Popen([target_exe])
    print("Success: Launched from Tasks directory!")
except Exception as e:
    print(f"Tasks path approach failed: {e}")
