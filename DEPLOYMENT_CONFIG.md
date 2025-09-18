# Deployment Configuration

## Backend Deployment
- **Platform**: AWS Lambda
- **URL**: https://pkrqj46pfieplghllqkeyjiptm0rqdpv.lambda-url.ap-south-1.on.aws
- **Type**: Serverless deployment
- **Region**: ap-south-1 (Asia Pacific - Mumbai)

## Frontend Configuration
- **API Base URL**: Configured in `src/services/api.js`
- **Build Tool**: Vite
- **Deployment**: Ready for static hosting (Netlify, Vercel, S3, etc.)

## API Endpoints
All API calls now point to the deployed Lambda function:
- `/chat` - Chat with AI assistant
- `/save-form` - Save form data
- `/check-user-status` - Check user status
- `/chat-history/{user_id}` - Get chat history
- `/chapters/{exam}` - Get exam chapters

## Testing
- No local backend setup required
- Frontend can be tested with: `npm run dev`
- All API calls will hit the deployed Lambda function

## Environment
- Production-ready deployment
- HTTPS enabled by default
- CORS configured for cross-origin requests