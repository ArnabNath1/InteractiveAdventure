# Quick Deployment Guide

## 🐳 Docker Deployment (Easiest)

### Prerequisites
- Docker and Docker Compose installed

### Steps

1. **Create `.env` file in project root:**
   ```env
   GEMINI_API_KEY=your_gemini_api_key_here
   DATABASE_PATH=databse.db
   API_PREFIX=/api
   DEBUG=False
   ALLOWED_ORIGINS=http://localhost:3000,http://localhost:5173
   VITE_API_URL=/api
   ```

2. **Deploy:**
   ```bash
   docker-compose up -d --build
   ```

3. **Access:**
   - Frontend: http://localhost:3000
   - Backend API: http://localhost:8000
   - API Docs: http://localhost:8000/docs

4. **Stop:**
   ```bash
   docker-compose down
   ```

---

## ☁️ Platform Deployments

### Railway (Full Stack)

1. **Connect GitHub repo to Railway**
2. **Deploy Backend:**
   - New Project → Deploy from GitHub
   - Root Directory: `backend`
   - Build Command: `pip install -r requirements.txt`
   - Start Command: `uvicorn main:app --host 0.0.0.0 --port $PORT`
   - Add environment variables (see below)

3. **Deploy Frontend:**
   - New Project → Static Site
   - Root Directory: `frontend`
   - Build Command: `npm install && npm run build`
   - Output Directory: `dist`
   - Add `VITE_API_URL` = your backend URL

### Render

1. **Deploy Backend:**
   - New Web Service
   - Connect GitHub repo
   - Root Directory: `backend`
   - Build: `pip install -r requirements.txt`
   - Start: `uvicorn main:app --host 0.0.0.0 --port $PORT`
   - Add environment variables

2. **Deploy Frontend:**
   - New Static Site
   - Connect GitHub repo
   - Root Directory: `frontend`
   - Build: `npm install && npm run build`
   - Publish Directory: `dist`

### Vercel (Frontend) + Any Backend Host

1. **Deploy Frontend to Vercel:**
   - Import GitHub repo
   - Framework Preset: Vite
   - Build Command: `npm run build`
   - Output Directory: `dist`
   - Environment Variable: `VITE_API_URL` = your backend URL

2. **Deploy Backend separately:**
   - Use Railway, Render, Fly.io, or any Python host
   - Update `ALLOWED_ORIGINS` with Vercel URL

---

## 🔧 Environment Variables

### Backend
```env
GEMINI_API_KEY=your_key_here
DATABASE_PATH=databse.db
API_PREFIX=/api
DEBUG=False
ALLOWED_ORIGINS=https://your-frontend-domain.com
```

### Frontend
```env
VITE_API_URL=https://your-backend-api.com/api
```

---

## 📝 Production Checklist

- [ ] Set `DEBUG=False`
- [ ] Configure `ALLOWED_ORIGINS` with production URLs
- [ ] Set `VITE_API_URL` in frontend
- [ ] Use HTTPS in production
- [ ] Secure your `.env` file (never commit)
- [ ] Test CORS configuration
- [ ] Monitor logs and errors

---

## 🚀 One-Command Docker Deploy

```bash
# Make sure .env file exists in project root, then:
docker-compose up -d --build && echo "✅ Deployed! Frontend: http://localhost:3000, Backend: http://localhost:8000"
```

For detailed instructions, see [DEPLOYMENT.md](./DEPLOYMENT.md)

