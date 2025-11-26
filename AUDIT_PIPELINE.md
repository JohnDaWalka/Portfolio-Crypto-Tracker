# Smart Contract Audit Pipeline

A comprehensive smart contract security audit tool that integrates multiple analysis tools with real-time on-chain data from Etherscan.

## Features

- **Multi-Tool Integration**: Supports Slither, Mythril, Echidna, Certora, and MythX
- **Real Etherscan Data**: Fetches actual on-chain metrics when API key is configured
- **Flexible Audit Levels**: Choose from quick, standard, deep, or forensic audits
- **Live Crypto Data**: Integrates with CoinGecko API and Sag3.AI

## Installation

### Prerequisites

- Python 3.7+
- Solidity compiler (solc)
- Security tools (Slither, Mythril, etc.)

### Install Dependencies

```bash
pip install requests
```

### Install Security Tools (Optional)

```bash
# Install Slither
pip install slither-analyzer

# Install Mythril
pip install mythril

# Install Echidna (requires Haskell)
# See: https://github.com/crytic/echidna
```

## Configuration

### Etherscan API Key

To fetch real on-chain data, you need a free Etherscan API key:

1. Visit https://etherscan.io/apis
2. Sign up for a free account
3. Generate an API key
4. Set the environment variable:

```bash
export ETHERSCAN_API_KEY="your_api_key_here"
```

**What data is fetched from Etherscan:**
- Transaction count (actual number from on-chain data)
- Contract verification status (verified/not_verified)
- Deployer address (from contract creation transaction)
- Creation date (timestamp from the oldest transaction)

**Fallback behavior:**
- Without API key: Returns simulated data with informative notes
- Without contract address: Returns info message explaining what's needed
- Network errors: Gracefully handles failures and returns error details

## Usage

### Basic Audit

```bash
python audit_pipeline.py --contract MyToken.sol --level quick
```

### Audit with On-Chain Data

```bash
# Set your Etherscan API key
export ETHERSCAN_API_KEY="your_api_key_here"

# Run audit with contract address
python audit_pipeline.py \
    --contract MyToken.sol \
    --level comprehensive \
    --address 0xdac17f958d2ee523a2206206994597c13d831ec7
```

### Save Audit Report

```bash
python audit_pipeline.py \
    --contract MyToken.sol \
    --level standard \
    --address 0x1234... \
    --output report.json
```

## Audit Levels

- **quick**: Slither only - 2-5 minutes
- **standard**: Slither + Mythril - 10-15 minutes
- **deep**: All tools including Certora - 30+ minutes
- **forensic**: Everything + continuous monitoring

## Output Format

The audit report is generated in JSON format:

```json
{
  "contract": "MyToken.sol",
  "audit_level": "quick",
  "timestamp": "2024-01-01T12:00:00",
  "results": [
    {
      "tool": "Slither",
      "passed": true,
      "severity_count": {
        "critical": 0,
        "high": 0,
        "medium": 2,
        "low": 5,
        "informational": 10
      },
      "execution_time": 3.45
    }
  ],
  "metadata": {
    "contract_address": "0xdac17f958d2ee523a2206206994597c13d831ec7",
    "etherscan_data": {
      "verification_status": "verified",
      "transaction_count": 12345,
      "deployer_address": "0x...",
      "creation_date": "2024-01-01T12:00:00",
      "api_endpoint": "https://api.etherscan.io/api?..."
    }
  }
}
```

## Examples

### Example 1: Quick Security Check

```bash
python audit_pipeline.py --contract contracts/Token.sol --level quick
```

### Example 2: Comprehensive Audit with Etherscan Data

```bash
export ETHERSCAN_API_KEY="ABC123..."
python audit_pipeline.py \
    --contract contracts/Token.sol \
    --level deep \
    --address 0x1234567890123456789012345678901234567890 \
    --output audit_report.json
```

### Example 3: Forensic Analysis

```bash
python audit_pipeline.py \
    --contract contracts/Token.sol \
    --level forensic \
    --address 0xdac17f958d2ee523a2206206994597c13d831ec7
```

## Troubleshooting

### "Contract file not found"

Ensure the contract path is correct and the file exists:

```bash
ls -la contracts/MyToken.sol
```

### "ETHERSCAN_API_KEY not found"

The tool will work without an API key but return simulated data. To get real on-chain data:

1. Get a free API key from https://etherscan.io/apis
2. Export it: `export ETHERSCAN_API_KEY="your_key"`

### "requests library not installed"

Install the requests library:

```bash
pip install requests
```

### "Slither not installed"

Install Slither:

```bash
pip install slither-analyzer
```

## Contributing

Contributions are welcome! Please submit pull requests or open issues for bugs and feature requests.

## License

MIT License - See LICENSE file for details

## Author

John DaWalka

## Links

- Etherscan API Documentation: https://docs.etherscan.io/
- Slither Documentation: https://github.com/crytic/slither
- CoinGecko API: https://www.coingecko.com/en/api
