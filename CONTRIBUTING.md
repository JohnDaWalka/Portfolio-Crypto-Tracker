# Contributing to Portfolio Crypto Tracker

Thank you for your interest in contributing to the Portfolio Crypto Tracker! This document provides guidelines and instructions for contributing to this project.

## Table of Contents

- [Code of Conduct](#code-of-conduct)
- [Getting Started](#getting-started)
- [How to Contribute](#how-to-contribute)
- [Development Workflow](#development-workflow)
- [Coding Standards](#coding-standards)
- [Testing Guidelines](#testing-guidelines)
- [Pull Request Process](#pull-request-process)
- [AI-Assisted Development](#ai-assisted-development)
- [Issue Guidelines](#issue-guidelines)

## Code of Conduct

### Our Pledge

We are committed to providing a welcoming and inclusive environment for all contributors. We pledge to:

- Be respectful and considerate in all interactions
- Welcome diverse perspectives and experiences
- Accept constructive criticism gracefully
- Focus on what's best for the community
- Show empathy towards other community members

### Unacceptable Behavior

- Harassment, discrimination, or offensive comments
- Trolling or inflammatory remarks
- Publishing others' private information
- Any conduct that could reasonably be considered inappropriate in a professional setting

## Getting Started

### Prerequisites

Before contributing, ensure you have:

- **Python 3.7+** installed
- **Node.js 16+** installed (for React development)
- **Git** installed and configured
- A **GitHub account**
- Familiarity with the project (read the [README.md](README.md))

### Setting Up Your Development Environment

1. **Fork the repository** on GitHub
2. **Clone your fork** locally:
   ```bash
   git clone https://github.com/YOUR_USERNAME/Portfolio-Crypto-Tracker.git
   cd Portfolio-Crypto-Tracker
   ```
3. **Add the upstream remote**:
   ```bash
   git remote add upstream https://github.com/JohnDaWalka/Portfolio-Crypto-Tracker.git
   ```
4. **Install Python dependencies**:
   ```bash
   pip install requests
   # Optional: Install security tools
   pip install slither-analyzer mythril
   ```
5. **Install Node dependencies** (if working on React code):
   ```bash
   npm install
   ```

### Keeping Your Fork Updated

Regularly sync your fork with the upstream repository:

```bash
git fetch upstream
git checkout main
git merge upstream/main
git push origin main
```

## How to Contribute

### Types of Contributions

We welcome various types of contributions:

1. **Bug Fixes** - Fix issues in existing code
2. **New Features** - Add new functionality
3. **Documentation** - Improve or add documentation
4. **Tests** - Add or improve test coverage
5. **Performance** - Optimize existing code
6. **Security** - Fix security vulnerabilities
7. **Code Quality** - Refactor code for better maintainability

### What to Work On

- Check the [Issues](https://github.com/JohnDaWalka/Portfolio-Crypto-Tracker/issues) page
- Look for issues labeled `good first issue` for beginner-friendly tasks
- Issues labeled `help wanted` are great for community contributions
- You can also propose new features by creating an issue first

## Development Workflow

### 1. Create a Branch

Create a descriptive branch name:

```bash
git checkout -b feature/add-wallet-balance-checker
git checkout -b bugfix/fix-etherscan-timeout
git checkout -b docs/update-installation-guide
```

### 2. Make Your Changes

- Write clean, readable code
- Follow the coding standards (see below)
- Add comments for complex logic
- Update documentation as needed
- Write tests for new functionality

### 3. Test Your Changes

**For Python code:**
```bash
# Run the audit pipeline with test contracts
python audit_pipeline.py --contract test.sol --level quick

# Test with different parameters
python audit_pipeline.py --contract test.sol --level standard --address 0x...
```

**For React code:**
```bash
# Run the development server
npm run dev

# Run tests
npm test

# Run linting
npm run lint

# Check formatting
npm run format
```

### 4. Commit Your Changes

Write clear, descriptive commit messages:

```bash
git add .
git commit -m "Add wallet balance checking feature

- Implement Etherscan balance API integration
- Add error handling for API failures
- Update documentation with new feature
- Add unit tests for balance checking"
```

**Commit Message Guidelines:**
- Start with a verb in imperative mood (Add, Fix, Update, Remove)
- Keep the first line under 72 characters
- Add a blank line and detailed description if needed
- Reference issue numbers (e.g., "Fixes #123")

### 5. Push to Your Fork

```bash
git push origin feature/add-wallet-balance-checker
```

### 6. Create a Pull Request

- Go to the GitHub repository
- Click "New Pull Request"
- Select your branch
- Fill out the PR template completely
- Link to the related issue
- Request review from maintainers

## Coding Standards

### Python Code Standards

**Style Guide**: Follow PEP 8

- Use 4 spaces for indentation (no tabs)
- Maximum line length: 100 characters
- Use snake_case for functions and variables
- Use PascalCase for class names
- Add type hints for function parameters and returns

**Example:**
```python
def fetch_contract_data(contract_address: str, timeout: int = 10) -> Dict[str, Any]:
    """
    Fetch contract data from Etherscan API.
    
    Args:
        contract_address: Ethereum contract address (0x...)
        timeout: Request timeout in seconds
        
    Returns:
        Dictionary containing contract metadata
        
    Raises:
        RequestException: If API request fails
    """
    try:
        response = requests.get(url, timeout=timeout)
        response.raise_for_status()
        return response.json()
    except requests.RequestException as e:
        Logger.error(f"API request failed: {str(e)}")
        raise
```

### JavaScript/React Code Standards

**Style Guide**: Airbnb JavaScript Style Guide

- Use 2 spaces for indentation
- Use camelCase for variables and functions
- Use PascalCase for React components
- Prefer functional components with hooks
- Use async/await over promise chains

**Example:**
```javascript
import { useState, useEffect } from 'react';

export const PortfolioCard = ({ holdings, onUpdate }) => {
  const [loading, setLoading] = useState(false);
  const [error, setError] = useState(null);

  useEffect(() => {
    fetchPriceData();
  }, [holdings]);

  const fetchPriceData = async () => {
    setLoading(true);
    try {
      const data = await priceApi.fetch(holdings);
      onUpdate(data);
    } catch (err) {
      setError(err.message);
    } finally {
      setLoading(false);
    }
  };

  if (loading) return <Spinner />;
  if (error) return <ErrorMessage message={error} />;
  
  return (
    <div className="portfolio-card">
      {/* Component content */}
    </div>
  );
};
```

### Documentation Standards

- Add docstrings to all public functions and classes
- Use Google-style docstrings for Python
- Add JSDoc comments for complex JavaScript functions
- Update README.md for user-facing changes
- Include code examples in documentation
- Keep documentation up-to-date with code changes

### Security Standards

- **Never** commit API keys, secrets, or credentials
- **Never** log sensitive information
- **Always** validate and sanitize user input
- **Always** use HTTPS for external API calls
- **Always** set timeouts for network requests
- **Always** handle errors gracefully
- Review the [security issue template](.github/ISSUE_TEMPLATE/security.md) before reporting vulnerabilities

## Testing Guidelines

### Writing Tests

- Write tests for all new functionality
- Maintain or improve existing test coverage
- Test both success and failure cases
- Test edge cases and boundary conditions
- Use descriptive test names

### Python Testing

```python
def test_fetch_etherscan_data_success():
    """Test successful Etherscan data fetch"""
    pipeline = AuditPipeline("test.sol", AuditLevel.QUICK)
    pipeline.metadata["contract_address"] = "0x..."
    
    data = pipeline.fetch_etherscan_data("0x...")
    
    assert data["verification_status"] in ["verified", "not_verified"]
    assert "transaction_count" in data
```

### JavaScript Testing

```javascript
describe('usePriceData hook', () => {
  it('should fetch prices successfully', async () => {
    const { result } = renderHook(() => usePriceData(['bitcoin']));
    
    await waitFor(() => {
      expect(result.current.loading).toBe(false);
    });
    
    expect(result.current.prices.bitcoin).toBeDefined();
    expect(result.current.error).toBeNull();
  });
});
```

## Pull Request Process

### Before Submitting

- [ ] Code follows the style guidelines
- [ ] Self-review completed
- [ ] Comments added for complex code
- [ ] Documentation updated
- [ ] Tests added and passing
- [ ] No new warnings generated
- [ ] Related issues linked

### PR Template

When creating a PR, fill out the complete template:

1. **Description** - What does this PR do?
2. **Related Issue** - Link to issue (Fixes #123)
3. **Type of Change** - Bug fix, feature, docs, etc.
4. **Changes Made** - List specific changes
5. **Testing** - How did you test this?
6. **Security** - Any security implications?
7. **Documentation** - What docs need updating?
8. **Checklist** - Complete all applicable items

### Review Process

1. Maintainers will review your PR within 3-5 business days
2. Address any requested changes
3. Once approved, a maintainer will merge your PR
4. Your contribution will be credited in release notes

### After Your PR is Merged

- Delete your feature branch
- Update your local main branch
- Check if any follow-up issues need attention

## AI-Assisted Development

This project uses GitHub Copilot and Sourcery-AI. Here's how to work with these tools:

### GitHub Copilot

- Custom instructions are in `.github/copilot-instructions.md`
- Review Copilot suggestions before accepting
- Copilot follows our coding standards automatically
- You can use Copilot for code completion and generation

### Sourcery-AI

- Configuration is in `.sourcery.yaml`
- Sourcery will suggest Python code improvements
- Review and apply relevant suggestions
- Not all suggestions need to be accepted

### AI Tool Best Practices

- **Review AI output** - AI tools can make mistakes
- **Test thoroughly** - Always test AI-generated code
- **Maintain consistency** - Ensure AI suggestions match project style
- **Report issues** - If AI tools suggest something wrong, report it

## Issue Guidelines

### Creating Issues

Use the appropriate template:

- **Bug Report** - For reporting bugs
- **Feature Request** - For suggesting new features
- **Documentation** - For documentation improvements
- **Security Issue** - For security vulnerabilities (use responsibly!)

### Issue Best Practices

- Search existing issues first
- Use a clear, descriptive title
- Provide complete information
- Add relevant labels
- Be respectful and constructive

### Working on Issues

- Comment on the issue to claim it
- Ask questions if requirements are unclear
- Update the issue with progress
- Link your PR to the issue

## Getting Help

### Resources

- **Documentation**: Read the [README.md](README.md) and [AUDIT_PIPELINE.md](AUDIT_PIPELINE.md)
- **Issues**: Search existing issues for similar problems
- **Discussions**: Use GitHub Discussions for questions
- **Community**: Join our Discord (if available)

### Contact

- Create an issue for bugs or features
- Use discussions for questions
- Email maintainers for sensitive matters

## Recognition

All contributors are recognized in:

- GitHub Contributors page
- Release notes (for significant contributions)
- README acknowledgments (for major features)

Thank you for contributing to Portfolio Crypto Tracker! Your efforts help make this project better for everyone.

---

**Questions?** Feel free to ask in the issue tracker or discussions!
