# LuxeMart Streamlit

Complete single-file Streamlit storefront + Supabase backend workflow.

## Streamlit Secrets
In your Streamlit app: **Settings → Secrets** and add:

```toml
SUPABASE_URL = "https://lszdnrkasvaheowrtmjf.supabase.co"
SUPABASE_KEY = "YOUR_SUPABASE_PUBLISHABLE_KEY"
```

Use the publishable/anon key, never a service-role/secret key.

## Deploy
1. Upload `app.py` and `requirements.txt` to GitHub.
2. Open Streamlit Community Cloud.
3. Create a new app.
4. Select the GitHub repository and `app.py`.
5. Deploy.
6. Add the two Supabase secrets.
7. Reboot the app.

The Admin tab uses the Supabase Auth email/password you created for LuxeMart.
