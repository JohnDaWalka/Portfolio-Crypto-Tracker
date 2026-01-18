# GitHub Copilot Instructions

## Project Context

This is the **Portfolio Crypto Tracker** repository - a professional-grade cryptocurrency portfolio tracking application with smart contract audit capabilities.

### Technology Stack
- **Frontend**: React with Vite build tool
- **Styling**: Tailwind CSS
- **APIs**: CoinGecko API (crypto prices), Etherscan API (on-chain data), Sag3.AI (trading signals)
- **Backend/Scripts**: Python 3.7+ for smart contract audit pipeline
- **Security Tools**: Slither, Mythril, Echidna, Certora, MythX

### Repository Structure
- `/src/` - React application source code (when present)
  - `components/` - React components
  - `services/` - API integrations and business logic
  - `hooks/` - Custom React hooks
  - `styles/` - CSS and styling files
- `audit_pipeline.py` - Smart contract security audit tool
- `README.md` - Main project documentation
- `AUDIT_PIPELINE.md` - Audit pipeline documentation

## Coding Standards

### Python Code
- Use Python 3.7+ compatible syntax
- Follow PEP 8 style guide
- Use type hints for function parameters and return values
- Use dataclasses for structured data
- Prefer f-strings for string formatting
- Use docstrings for all functions and classes
- Handle exceptions gracefully with try-except blocks
- Use the `requests` library for HTTP API calls
- Use `subprocess` for running external tools
- Maintain backward compatibility with existing API structure

### JavaScript/React Code
- Use functional components with hooks (not class components)
- Use camelCase for variable and function names
- Use PascalCase for component names
- Prefer async/await over promise chains
- Use 2 spaces for indentation
- Add PropTypes or TypeScript types when available
- Extract reusable logic into custom hooks
- Keep components focused and small

### General Standards
- Write clear, self-documenting code
- Add comments for complex logic or business rules
- Follow existing patterns in the codebase
- Maintain consistency with surrounding code
- Write comprehensive documentation in markdown files

## API Integration Guidelines

### Required Environment Variables
- `ETHERSCAN_API_KEY` - Optional but recommended for real on-chain data
- `VITE_COINGECKO_API_KEY` - Optional for CoinGecko API
- `VITE_REFRESH_INTERVAL` - Default 60000ms for price updates
- `VITE_ENABLE_SAG3_INTEGRATION` - Boolean flag for Sag3.ai features

### API Best Practices
- Always handle API failures gracefully
- Provide fallback data when APIs are unavailable
- Log informative messages about API usage
- Respect rate limits (CoinGecko: 10-50 calls/min)
- Never expose API keys in logs or error messages
- Use timeouts for all HTTP requests (default: 10 seconds)

## Security Requirements

### Critical Security Rules
- **NEVER** store or log API keys in code
- **NEVER** store private keys, seed phrases, or wallet passwords
- **NEVER** make cryptocurrency transactions
- **NEVER** connect to external wallet applications
- Always validate and sanitize user inputs
- Use HTTPS for all external API calls
- Keep dependencies up to date for security patches
- Handle sensitive data with care

### Audit Pipeline Security
- Validate contract paths before processing
- Use timeouts for all tool executions
- Sanitize JSON output before logging
- Verify tool installations before running
- Handle subprocess failures safely

## Build, Run, and Test Commands

### Python Scripts
```bash
# Run the audit pipeline
python audit_pipeline.py --contract <path> --level quick

# With Etherscan integration
export ETHERSCAN_API_KEY="your_key"
python audit_pipeline.py --contract <path> --level standard --address 0x...

# Save output to file
python audit_pipeline.py --contract <path> --output report.json
```

### React Application (when present)
```bash
# Install dependencies
npm install

# Run development server
npm run dev

# Build for production
npm run build

# Preview production build
npm run preview

# Run linting
npm run lint

# Format code
npm run format

# Run tests
npm test
```

## GitHub Copilot Agent Boundaries

### What Copilot SHOULD Do
- Fix bugs with minimal changes
- Add new features that match existing patterns
- Improve documentation and add examples
- Add type hints and improve code quality
- Optimize performance within existing architecture
- Add unit tests for new functionality
- Update configuration files appropriately

### What Copilot SHOULD NOT Do
- Refactor working code unless explicitly requested
- Remove or modify working features
- Change the overall architecture without discussion
- Add dependencies without justification
- Modify security-critical code without review
- Change API contracts that may break users
- Delete tests or reduce test coverage
- Make changes unrelated to the assigned task

### Decision-Making Guidelines
- When in doubt, ask for clarification in PR comments
- Prefer minimal changes over comprehensive refactoring
- Keep existing behavior unless explicitly changing it
- Match the style and patterns of surrounding code
- Write tests that match existing test patterns
- Document why complex changes were made

## Documentation Standards

### README.md Guidelines
- Use clear, descriptive section headers
- Provide step-by-step instructions for setup
- Include code examples for common use cases
- Explain WHY features exist, not just WHAT they do
- Keep examples up-to-date with the code
- Use comments within markdown examples to explain concepts

### Code Comments
- Explain the "why" not the "what"
- Use docstrings for all public functions and classes
- Add inline comments for non-obvious logic
- Document assumptions and limitations
- Reference external documentation when relevant

## Issue and PR Guidelines

### Creating Issues
- Use descriptive titles that summarize the problem
- Provide clear steps to reproduce bugs
- Include expected vs actual behavior
- Add relevant code snippets or error messages
- Label appropriately (bug, enhancement, documentation)
- Break down large features into smaller tasks

### Pull Request Requirements
- Reference the issue being fixed
- Describe what changed and why
- List any breaking changes
- Include test coverage for new code
- Update documentation if needed
- Keep PRs focused on a single concern
- Respond to review comments promptly

## Dependencies and Tools

### Python Dependencies
- `requests` - HTTP API calls (install with: pip install requests)
- Standard library modules preferred when possible
- Avoid adding heavy dependencies

### JavaScript Dependencies (when applicable)
- Minimize new dependencies
- Prefer well-maintained packages
- Check for security vulnerabilities before adding
- Document why each dependency is needed

### Security Tools (Optional)
- Slither - `pip install slither-analyzer`
- Mythril - `pip install mythril`
- Echidna - Haskell-based fuzzer
- Certora - Formal verification tool

## Testing Philosophy

### Test Coverage
- Write tests for new functionality
- Maintain existing test coverage
- Test edge cases and error conditions
- Mock external API calls in tests
- Use descriptive test names

### Test Organization
- Place tests near the code they test
- Use consistent naming conventions
- Group related tests together
- Make tests independent and repeatable

## Version Control

### Commit Messages
- Use clear, descriptive commit messages
- Start with a verb (Add, Fix, Update, Remove)
- Keep the first line under 72 characters
- Add details in the body if needed
- Reference issue numbers when applicable

### Branch Naming
- Use prefixes: `feature/`, `bugfix/`, `docs/`, `refactor/`
- Be descriptive: `feature/add-eth-balance-check`
- Use lowercase with hyphens
- Keep branch names concise

## Common Patterns in This Repository

### Error Handling Pattern
```python
try:
    # Attempt operation
    result = risky_operation()
    Logger.success("Operation succeeded")
    return result
except SpecificError as e:
    Logger.error(f"Specific error: {str(e)}")
    return fallback_value
except Exception as e:
    Logger.error(f"Unexpected error: {str(e)}")
    return None
```

### API Integration Pattern
```python
import requests

def fetch_data(url: str, timeout: int = 10) -> Dict:
    """Fetch data from API with error handling"""
    try:
        response = requests.get(url, timeout=timeout)
        response.raise_for_status()
        return response.json()
    except requests.RequestException as e:
        Logger.error(f"API request failed: {str(e)}")
        return {"error": str(e)}
```

### Configuration Pattern
```python
# Check environment variable with fallback
api_key = os.getenv("API_KEY")
if not api_key:
    Logger.info("API_KEY not set. Using fallback behavior.")
    return default_data()
```

## Performance Considerations

- Cache API responses when appropriate
- Use pagination for large data sets
- Set reasonable timeouts for external calls
- Avoid unnecessary file I/O operations
- Profile code before optimizing
- Document performance characteristics

## Accessibility and Usability

- Provide clear error messages
- Log informative status updates
- Support both CLI and programmatic usage
- Make configuration optional with sensible defaults
- Document all command-line options
- Provide examples for common use cases

## Future Considerations

This repository is evolving. Keep these future directions in mind:
- Advanced charting integration (TradingView)
- Direct Sag3.ai API integration
- Multi-wallet support
- Tax reporting features
- Machine learning price predictions
- Mobile app development

When making changes, ensure they don't block these future enhancements.
