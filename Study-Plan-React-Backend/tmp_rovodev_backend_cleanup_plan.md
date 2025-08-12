# Backend Cleanup and Standardization Plan

## Current Issues
- Too many duplicate/enhanced files
- Scattered functionality across multiple files
- Unclear file organization
- Mixed old and new implementations

## Target Structure
```
Study-Plan-React-Backend/
├── app/
│   ├── __init__.py
│   ├── main.py                          # Main FastAPI app
│   ├── core/                           # Core functionality
│   │   ├── __init__.py
│   │   ├── models.py                   # All data models
│   │   ├── database.py                 # Database connections
│   │   └── config.py                   # Configuration
│   ├── custom_plan/                    # Custom Plan functionality
│   │   ├── __init__.py
│   │   ├── endpoints.py                # Custom plan endpoints
│   │   ├── models.py                   # Custom plan models
│   │   ├── agents.py                   # Custom plan agents
│   │   ├── graph.py                    # Custom plan workflow
│   │   ├── tools.py                    # Custom plan tools
│   │   └── regeneration/               # Custom plan regeneration
│   │       ├── __init__.py
│   │       ├── endpoints.py
│   │       ├── models.py
│   │       ├── graph.py
│   │       └── tools.py
│   ├── new_score_oriented/             # New Score-Oriented functionality
│   │   ├── __init__.py
│   │   ├── endpoints.py                # NSO endpoints
│   │   ├── models.py                   # NSO models
│   │   ├── agents.py                   # NSO agents
│   │   ├── graph.py                    # NSO workflow
│   │   ├── tools.py                    # NSO tools
│   │   ├── json_generator.py           # Enhanced JSON generation
│   │   └── display.py                  # Terminal display
│   ├── shared/                         # Shared utilities
│   │   ├── __init__.py
│   │   ├── tools.py                    # Common tools
│   │   ├── utils.py                    # Utility functions
│   │   └── validators.py               # Common validators
│   └── api/                           # API layer
│       ├── __init__.py
│       └── routes.py                   # Route aggregation
├── requirements.txt
└── README.md
```

## Files to Keep (Core)
- main.py (cleaned)
- models.py (consolidated)
- tools.py (shared tools)
- utils.py
- graph.py (custom plan)
- regen_graph.py (custom regeneration)
- new_score_oriented_graph.py
- new_score_oriented_endpoints.py
- new_score_oriented_models.py
- new_score_oriented_tools.py
- enhanced_score_oriented_json_generator.py

## Files to Remove/Consolidate
- All "enhanced_" duplicates
- Old score-oriented files (non-new)
- Duplicate calendar files
- Unused dependency resolvers
- Multiple requirement extractors

## Migration Strategy
1. Create new directory structure
2. Consolidate models into core/models.py
3. Move custom plan files to custom_plan/
4. Move new score-oriented files to new_score_oriented/
5. Create shared utilities in shared/
6. Update imports across all files
7. Test functionality
8. Remove old files