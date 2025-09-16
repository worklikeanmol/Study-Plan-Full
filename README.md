# Study Plan React Frontend

A modern React frontend for the Study Plan Generator system, built with Vite and Tailwind CSS.

## Features

- **Smart Form Validation**: 
  - Target score required for Generic study plans
  - Minimum 3 months for Syllabus Coverage preparation type
  - Real-time validation with user-friendly error messages

- **Interactive Chat Interface**: 
  - Real-time communication with AI counselor
  - Auto-managed chat history
  - Support for both new and existing users

- **Study Plan Visualization**: 
  - Monthly breakdown with chapter coverage
  - Color-coded progress indicators
  - Responsive design for all devices

- **User Experience**:
  - Modern, clean interface with Tailwind CSS
  - Toast notifications for user feedback
  - Loading states and error handling

## Requirements

- Node.js 16+ 
- npm or yarn
- Study Plan Backend API running on `http://127.0.0.1:8000`

## Installation

1. **Install dependencies**:
   ```bash
   npm install
   ```

2. **Start development server**:
   ```bash
   npm run dev
   ```

3. **Build for production**:
   ```bash
   npm run build
   ```

## Form Validation Rules

### Study Plan Type
- **Generic**: Requires target score (1-300)
- **Custom**: Target score not required

### Preparation Type  
- **Syllabus Coverage**: Minimum 3 months required
- **Revision**: No minimum month restriction

### Syllabus Configuration
- At least one chapter required for each subject (Mathematics, Physics, Chemistry)
- Default syllabus can be loaded with one click
- Dynamic chapter addition/removal

## API Integration

The frontend integrates with the Study Plan Backend API:

- `POST /chat` - Interactive chat with AI counselor
- `POST /check-user-status` - Check if user is new or existing
- `GET /chat-history/{user_id}` - Retrieve chat history
- `DELETE /chat-history/{user_id}` - Clear chat history
- `GET /regeneration-info/{user_id}` - Get regeneration data for existing users

## Project Structure

```
src/
├── components/          # React components
│   ├── StudyPlanForm.jsx    # Main form with validation
│   ├── ChatInterface.jsx    # Chat UI component  
│   ├── StudyPlanView.jsx    # Study plan display
│   └── Sidebar.jsx          # Navigation sidebar
├── context/             # React context for state management
│   └── StudyPlanContext.jsx
├── services/            # API service functions
│   └── api.js
├── App.jsx             # Main app component
├── main.jsx            # App entry point
└── index.css           # Global styles with Tailwind

```

## Key Features Implementation

### Form Validation
- Real-time validation using React Hook Form
- Custom validation rules for study plan types
- Dynamic minimum month validation based on preparation type
- Syllabus validation ensuring at least one chapter per subject

### Chat Interface  
- Context-aware messaging with form data
- Auto-scroll to latest messages
- Loading states during API calls
- Error handling with user-friendly messages

### Study Plan Display
- Color-coded chapter coverage visualization
- Monthly breakdown with subject organization
- Responsive grid layout
- Progress indicators and insights display

## Development

### Available Scripts
- `npm run dev` - Start development server
- `npm run build` - Build for production  
- `npm run preview` - Preview production build
- `npm run lint` - Run ESLint

### Environment Configuration
The API base URL is configured in `src/services/api.js`. Update this if your backend runs on a different port or host.

## Deployment

1. Build the project: `npm run build`
2. Deploy the `dist` folder to your web server
3. Ensure the backend API is accessible from your deployment environment

## Browser Support

- Chrome 90+
- Firefox 88+  
- Safari 14+
- Edge 90+