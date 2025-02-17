import os

# Accessing environment variable
app_name = os.getenv('APP_NAME', 'Default App')
print(f"Running {app_name}")
