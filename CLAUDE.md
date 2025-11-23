# CLAUDE.md - CTFd Development Guide for AI Assistants

## Project Overview

**CTFd** is a Capture The Flag (CTF) framework focusing on ease of use and customizability. It provides a complete platform for running cybersecurity competitions with features like challenges, scoring, teams, hints, flags, and comprehensive administration.

- **Version**: 3.8.1
- **Channel**: OSS (Open Source)
- **Primary Language**: Python (Flask)
- **Frontend**: Jinja2 templates with JavaScript
- **Database**: SQLAlchemy (supports MySQL/MariaDB)
- **Cache**: Redis
- **Web Server**: Gunicorn with Nginx reverse proxy

## Repository Structure

```
CTFd-Range/
├── CTFd/                       # Main application directory
│   ├── __init__.py            # Flask app factory and initialization
│   ├── config.py              # Configuration management
│   ├── models/                # SQLAlchemy database models
│   ├── schemas/               # Marshmallow serialization schemas
│   ├── api/                   # RESTful API endpoints
│   │   └── v1/               # API version 1 (challenges, users, teams, etc.)
│   ├── plugins/               # Plugin system for extensibility
│   │   ├── challenges/       # Challenge type plugins
│   │   ├── dynamic_challenges/
│   │   └── flags/            # Flag validation plugins
│   ├── themes/                # Frontend themes
│   │   ├── admin/           # Admin panel theme
│   │   └── core/            # Default user-facing theme
│   ├── utils/                 # Utility functions (32+ modules)
│   │   ├── config/           # Configuration helpers
│   │   ├── decorators/       # Flask route decorators
│   │   ├── email/            # Email functionality
│   │   ├── security/         # Security utilities
│   │   └── ...               # Many more utility modules
│   ├── admin/                # Admin panel views
│   ├── cache/                # Cache management
│   ├── cli/                  # CLI commands
│   ├── constants/            # Application constants
│   ├── events/               # Event system
│   ├── exceptions/           # Custom exceptions
│   ├── forms/                # WTForms definitions
│   └── translations/         # i18n translations
├── tests/                     # Test suite
│   ├── helpers.py            # Test helpers and fixtures
│   └── */                    # Test modules by feature
├── migrations/                # Database migrations
├── conf/                     # Configuration files (nginx, etc.)
├── scripts/                  # Build and maintenance scripts
├── Docs/                     # Documentation
├── requirements.txt          # Python dependencies
├── docker-compose.yml        # Docker orchestration
├── Dockerfile                # Container definition
├── Makefile                  # Common development tasks
├── serve.py                  # Development server
└── wsgi.py                   # Production WSGI entry point
```

## Core Architecture

### Application Factory Pattern

CTFd uses the Flask application factory pattern defined in `CTFd/__init__.py`:

```python
from CTFd import create_app

app = create_app()
```

The `create_app()` function:
1. Creates a custom `CTFdFlask` instance with sandboxed Jinja2 environment
2. Loads configuration from `config.ini` and environment variables
3. Initializes database, cache, and session management
4. Registers blueprints, plugins, and themes
5. Sets up request processors, template filters, and event handlers

### Custom Flask Classes

- **CTFdFlask**: Custom Flask class with sandboxed Jinja2 environment and caching session interface
- **CTFdRequest**: Custom request class that accounts for subdirectory deployments
- **SandboxedBaseEnvironment**: Secure Jinja2 environment for rendering user content

### Database Models

All models are defined in `CTFd/models/__init__.py`:

**Core Models**:
- `Users`: User accounts with authentication
- `Teams`: Team management for group competitions
- `Challenges`: Challenge definitions (polymorphic by type)
- `Flags`: Challenge solutions
- `Hints`: Optional challenge hints
- `Submissions`: User/team challenge attempts
- `Solves`: Successful challenge completions
- `Fails`: Failed challenge attempts
- `Awards`: Manual score adjustments
- `Pages`: Custom CMS pages
- `Notifications`: User/team notifications
- `Files`: File uploads (challenges, pages)
- `Tokens`: API tokens and authentication

**Key Patterns**:
- Polymorphic models for extensibility (Challenges, Flags)
- Relationships with lazy loading
- Hybrid properties for computed values
- Custom validators via `@validates` decorator

### API Structure

RESTful API in `CTFd/api/v1/`:
- **Endpoints**: awards, brackets, challenges, comments, config, exports, files, flags, hints, notifications, pages, scoreboard, solutions, submissions, tags, teams, tokens, topics, unlocks, users
- **Format**: JSON responses using Marshmallow schemas
- **Authentication**: Session-based with CSRF protection or API tokens
- **Pagination**: Built-in pagination support
- **Versioning**: API versioned under `/api/v1/`

### Plugin System

Located in `CTFd/plugins/`, plugins extend CTFd functionality:

**Plugin Structure**:
```python
def load(app):
    """Called during app initialization with the CTFd app instance"""
    # Register routes, templates, assets, etc.
    pass
```

**Plugin Capabilities**:
- `register_plugin_assets_directory()`: Serve static assets
- `override_template()`: Replace default templates
- `register_plugin_script()`: Add JavaScript to base template
- `register_plugin_stylesheet()`: Add CSS to base template
- `register_admin_plugin_menu_bar()`: Add admin menu items
- `register_user_page_menu_bar()`: Add user menu items
- `bypass_csrf_protection()`: Decorator for CSRF exemption

**Built-in Plugin Types**:
- Challenge types (standard, dynamic)
- Flag types (static, regex)

### Theme System

Themes in `CTFd/themes/`:
- **admin/**: Admin panel (React-based, webpack build)
- **core/**: Default user theme (Jinja2 templates, Sass/JS assets)
- **core-deprecated/**: Legacy theme

Themes can be customized or completely replaced without modifying core code.

## Configuration

### Configuration Files

1. **CTFd/config.ini**: Default configuration (checked into git)
2. **Environment variables**: Override config.ini values
3. **config.py**: Python configuration classes

### Key Configuration Classes

- `ServerConfig`: Server settings (SECRET_KEY, SESSION_COOKIE_NAME)
- `DatabaseConfig`: Database connection (DATABASE_URL)
- `SecurityConfig`: Security settings (SESSION_COOKIE_HTTPONLY, TRUSTED_HOSTS)
- `SessionConfig`: Session management
- `EmailConfig`: Email/SMTP settings
- `UploadConfig`: File upload configuration
- `TestingConfig`: Test-specific settings

### Environment Variable Pattern

Configuration uses `EnvInterpolation` to read from environment:
```bash
DATABASE_URL=mysql+pymysql://user:pass@localhost/ctfd
REDIS_URL=redis://localhost:6379
SECRET_KEY=your-secret-key
```

## Development Workflows

### Local Development Setup

```bash
# Install Python dependencies
pip install -r requirements.txt

# Run development server
python serve.py
# OR
flask run
# OR
make serve

# Access at http://localhost:4000
```

### Docker Development

```bash
# Build and start all services
docker compose up

# Access at http://localhost:80 (nginx) or http://localhost:8000 (direct)
```

**Docker Services**:
- `ctfd`: Main application (Gunicorn)
- `nginx`: Reverse proxy
- `db`: MariaDB database
- `cache`: Redis cache

### Database Migrations

CTFd uses Flask-Migrate (Alembic):

```bash
# Create migration
flask db migrate -m "Description"

# Apply migrations
flask db upgrade

# Downgrade
flask db downgrade
```

Migrations are in `migrations/` directory.

### Testing

```bash
# Run all tests with coverage
make test

# Run specific test file
pytest tests/test_challenges.py

# Run with verbose output
pytest -v tests/
```

**Test Helpers** (`tests/helpers.py`):
- `CTFdTestClient`: Custom test client with CSRF handling
- `create_ctfd()`: App factory for tests
- `register_user()`: Create test users
- `login_as_user()`: Authenticate in tests
- `gen_challenge()`: Generate test challenges
- `ctftime`: Context managers for CTF time manipulation

### Code Quality

```bash
# Run all linting
make lint

# Auto-format code
make format
```

**Linting Tools**:
- **ruff**: Fast Python linter (E, F, W, B, C4, I rules)
- **isort**: Import sorting (black profile)
- **black**: Code formatting
- **prettier**: JavaScript/Markdown formatting
- **bandit**: Security linting (in tests)

**Linting Exclusions**:
- Ignore: E402, E501, E712, B904, B905, I001
- Exclude: `CTFd/uploads`, `node_modules`

### Building Frontend Assets

Admin theme uses webpack:

```bash
cd CTFd/themes/admin
yarn install
yarn build        # Production build
yarn dev          # Development build with watch
```

Core theme uses asset pipeline defined in theme.

## Key Conventions

### Code Style

1. **Python**:
   - Follow Black formatting (line length 88)
   - Use isort with Black profile for imports
   - Type hints encouraged but not required
   - Docstrings for public functions

2. **JavaScript**:
   - ESLint configuration in `.eslintrc.js`
   - Prettier for formatting
   - Modern ES6+ syntax

3. **Templates**:
   - Jinja2 templates in theme directories
   - Use template inheritance
   - Escape user content (auto-escaping enabled)

### Security Practices

1. **CSRF Protection**: All POST/PUT/DELETE requests require CSRF tokens
2. **SQL Injection**: Use SQLAlchemy ORM, never raw SQL with user input
3. **XSS Prevention**: Auto-escaping in Jinja2, use `markup()` for trusted HTML
4. **Authentication**: Session-based with secure cookies
5. **File Uploads**: Validated and stored in configured location
6. **Secrets**: Use environment variables, never commit secrets

### Database Patterns

1. **Query Patterns**:
   ```python
   from CTFd.models import db, Users

   # Create
   user = Users(name="test", email="test@example.com")
   db.session.add(user)
   db.session.commit()

   # Read
   user = Users.query.filter_by(name="test").first()
   users = Users.query.all()

   # Update
   user.email = "new@example.com"
   db.session.commit()

   # Delete
   db.session.delete(user)
   db.session.commit()
   ```

2. **Relationships**: Use lazy loading, avoid N+1 queries with `joinedload()`
3. **Transactions**: Wrap multi-step operations in try/except with rollback

### API Patterns

1. **Response Format**:
   ```python
   {"success": True, "data": {...}}
   {"success": False, "errors": {...}}
   ```

2. **Schema Validation**: Use Marshmallow schemas for serialization/deserialization
3. **Error Handling**: Return appropriate HTTP status codes
4. **Pagination**: Use `?page=1&per_page=50` parameters

### Cache Management

```python
from CTFd.cache import cache, clear_standings, clear_challenges

# Cache a value
cache.set("key", value, timeout=300)

# Get cached value
value = cache.get("key")

# Clear specific caches
clear_standings()
clear_challenges()
```

**Cache Keys**: Use descriptive prefixes (e.g., `standings`, `challenges`, `session`)

## Common Tasks for AI Assistants

### Adding a New Model

1. Define model in `CTFd/models/__init__.py`
2. Create Marshmallow schema in `CTFd/schemas/{model}.py`
3. Create migration: `flask db migrate -m "Add {model} table"`
4. Add API endpoint in `CTFd/api/v1/{models}.py`
5. Add admin views if needed
6. Write tests in `tests/models/` and `tests/api/`

### Creating a Plugin

1. Create directory in `CTFd/plugins/{plugin_name}/`
2. Create `__init__.py` with `load(app)` function
3. Register routes, assets, templates as needed
4. Add plugin-specific models/schemas if required
5. Test in SAFE_MODE=false environment

### Adding an API Endpoint

1. Create/modify file in `CTFd/api/v1/{resource}.py`
2. Define route with appropriate HTTP methods
3. Use Marshmallow schema for validation
4. Add authentication/authorization checks
5. Return JSON response with success/error format
6. Add tests in `tests/api/`

### Modifying Templates

1. Identify template in `CTFd/themes/{theme}/templates/`
2. Maintain template inheritance structure
3. Use Jinja2 template filters and globals
4. Test across different themes if applicable
5. Ensure mobile responsiveness

### Writing Tests

1. Import helpers from `tests/helpers`
2. Use `create_ctfd()` context manager
3. Use `CTFdTestClient` for API testing
4. Clean up test data (handled by fixtures)
5. Test both success and error cases
6. Mock external dependencies

## Important Files to Review Before Making Changes

| File | Purpose |
|------|---------|
| `CTFd/__init__.py` | App initialization, understand startup flow |
| `CTFd/models/__init__.py` | Database schema, relationships |
| `CTFd/config.py` | Configuration system |
| `CTFd/plugins/__init__.py` | Plugin loading mechanism |
| `tests/helpers.py` | Test utilities and patterns |
| `requirements.txt` | Python dependencies |
| `Makefile` | Common development commands |

## Debugging Tips

1. **Enable Debug Mode**: Set `FLASK_ENV=development` or use `python serve.py`
2. **Database Queries**: Use `SQLALCHEMY_ECHO=true` to log SQL
3. **Logs**: Check `CTFd/logs/` or Docker logs
4. **Cache Issues**: Clear cache with `cache.clear()`
5. **Plugin Issues**: Test with `SAFE_MODE=true` to disable plugins
6. **Frontend Issues**: Check browser console, rebuild assets

## Resources

- **Official Documentation**: https://docs.ctfd.io/
- **Community Forum**: https://community.majorleaguecyber.org/
- **GitHub Repository**: https://github.com/CTFd/CTFd
- **Live Demo**: https://demo.ctfd.io/

## Anti-Patterns to Avoid

1. ❌ Don't modify core files when a plugin can achieve the goal
2. ❌ Don't store secrets in code or config files
3. ❌ Don't use raw SQL queries (use SQLAlchemy ORM)
4. ❌ Don't bypass CSRF protection without security review
5. ❌ Don't commit `CTFd/uploads/` or `.data/` directories
6. ❌ Don't run migrations in production without backup
7. ❌ Don't modify `requirements.txt` directly (use `requirements.in` and pip-compile)
8. ❌ Don't skip writing tests for new features

## Notes for AI Assistants

- **Before modifying code**: Always read the relevant files to understand existing patterns
- **Plugin vs Core**: Prefer plugins for extensions, only modify core for essential changes
- **Testing**: Always write tests for new features and bug fixes
- **Security**: Be vigilant about CSRF, XSS, SQL injection, and authentication
- **Backwards Compatibility**: Consider impact on existing plugins and themes
- **Performance**: Consider caching and database query optimization
- **Documentation**: Update docstrings and comments for significant changes
- **Configuration**: Use environment variables for deployment-specific settings
- **Migrations**: Test both upgrade and downgrade paths

---

Last Updated: 2025-11-22 | CTFd Version: 3.8.1
