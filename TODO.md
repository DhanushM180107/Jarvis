# Jarvis Error Fix Plan

## Steps:
1. [ ] Upgrade packages: requests, urllib3, certifi, openai
2. [x] Edit internet_check.py: Add verify=False, broad exception handling, debug print, fallback URL
3. [ ] Test internet_check.py standalone
4. [ ] Run jarvis.py and check for new errors
5. [ ] Fix any remaining issues (e.g. openai import, threads)
6. [ ] Mark complete and run error-free

Current progress: Starting fixes.
