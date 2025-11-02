# Deployment Guide

This guide covers multiple deployment options for the Choose Your Own Adventure AI application.

## Table of Contents
1. [Docker Deployment](#docker-deployment)
2. [Platform-Specific Deployments](#platform-specific-deployments)
3. [Manual Deployment](#manual-deployment)
4. [Environment Variables](#environment-variables)

---

## Docker Deployment (Recommended)

### Prerequisites
- Docker and Docker Compose installed
- `.env` file configured (see [Environment Variables](#environment-variables))

### Quick Start

1. **Build and run with Docker Compose:**
   ```bash
   docker-compose up -d --build
   ```

2. **Access the application:**
   - Frontend: http://localhost:3000
   - Backend API: http://localhost:8000
   - API Docs: http://localhost:8000/docs

3. **View logs:**
   ```bash
   docker-compose logs -f
   ```

4. **Stop the services:**
   ```bash
   docker-compose down
   ```

---

## Platform-Specific Deployments

### Option 1: Vercel (Frontend) + Railway/Render (Backend)

#### Frontend on Vercel:
1. Push your code to GitHub
2. Import project in Vercel
3. Set build command: `npm run build`
4. Set output directory: `dist`
5. Add environment variable: `VITE_API_URL` (your backend URL)

#### Backend on Railway:
1. Connect your GitHub repo to Railway
2. Set root directory to `backend`
3. Add environment variables (see below)
4. Railway will auto-detect FastAPI and deploy

#### Backend on Render:
1. Create a new Web Service
2. Connect your GitHub repo
3. Build command: `cd backend && pip install -r requirements.txt`
4. Start command: `cd backend && uvicorn main:app --host 0.0.0.0 --port $PORT`
5. Add environment variables

### Option 2: Render (Full Stack)
1. Deploy backend as a Web Service
2. Deploy frontend as a Static Site (after building)
3. Configure CORS to allow your frontend domain

### Option 3: Fly.io
1. Install Fly CLI: `curl -L https://fly.io/install.sh | sh`
2. Run `fly launch` in the backend directory
3. Deploy frontend separately or serve from backend

---

## Manual Deployment

### Backend Deployment

1. **Set up server:**
   ```bash
   cd backend
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   pip install -r requirements.txt
   ```

2. **Configure environment:**
   - Copy `.env.example` to `.env`
   - Fill in all required variables

3. **Run with production server:**
   ```bash
   # Using Gunicorn (install: pip install gunicorn)
   gunicorn main:app -w 4 -k uvicorn.workers.UvicornWorker -b 0.0.0.0:8000
   
   # Or using uvicorn directly
   uvicorn main:app --host 0.0.0.0 --port 8000
   ```

4. **Set up process manager (PM2 or systemd):**
   ```bash
   # PM2 example
   pm2 start "uvicorn main:app --host 0.0.0.0 --port 8000" --name adventure-api
   ```

### Frontend Deployment

1. **Build the frontend:**
   ```bash
   cd frontend
   npm install
   npm run build
   ```

2. **Serve static files:**
   - Option A: Use a web server (Nginx, Apache)
   - Option B: Serve from backend (see below)
   - Option C: Use Vercel, Netlify, or Cloudflare Pages

3. **Serve frontend from backend (Optional):**
   Update `backend/main.py` to serve static files:
   ```python
   from fastapi.staticfiles import StaticFiles
   from fastapi.responses import FileResponse
   
   # Add after app creation
   app.mount("/static", StaticFiles(directory="../frontend/dist"), name="static")
   
   @app.get("/{full_path:path}")
   async def serve_spa(full_path: str):
       return FileResponse("../frontend/dist/index.html")
   ```

---

## Environment Variables

### Backend (.env)

Create `backend/.env` with:

```env
# API Configuration
GEMINI_API_KEY=your_gemini_api_key_here
API_PREFIX=/api
DEBUG=False

# Database
DATABASE_PATH=databse.db
# OR for PostgreSQL:
# DATABASE_URL=postgresql://user:password@host:port/dbname

# CORS (comma-separated URLs)
ALLOWED_ORIGINS=https://yourdomain.com,https://www.yourdomain.com
```

### Frontend Environment Variables

For production, set:
- `VITE_API_URL` - Your backend API URL (e.g., `https://api.yourdomain.com`)

Update `frontend/src/util.js`:
```javascript
export const API_BASE_URL = import.meta.env.VITE_API_URL || "/api"
```

---

## Production Checklist

- [ ] Set `DEBUG=False` in backend
- [ ] Configure proper `ALLOWED_ORIGINS`
- [ ] Use PostgreSQL for production (optional but recommended)
- [ ] Set up HTTPS/SSL certificates
- [ ] Configure environment variables securely
- [ ] Set up monitoring/logging
- [ ] Configure backup strategy for database
- [ ] Update frontend API URL for production
- [ ] Test CORS configuration
- [ ] Set up error tracking (Sentry, etc.)

---

## Troubleshooting

### CORS Issues
- Ensure `ALLOWED_ORIGINS` includes your frontend URL
- Check that credentials are properly configured

### Database Issues
- Ensure database file permissions are correct
- For PostgreSQL, verify connection string format

### API Key Issues
- Verify `GEMINI_API_KEY` is set correctly
- Check API key permissions and quotas

---

## Security Notes

⚠️ **Important:**
- Never commit `.env` files to version control
- Use environment variables for all secrets
- Enable HTTPS in production
- Regularly rotate API keys
- Use PostgreSQL for production (more secure than SQLite)

