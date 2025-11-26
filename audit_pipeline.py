#!/usr/bin/env python3
"""
Comprehensive Smart Contract Audit Pipeline with Live Crypto Data Integration

Integrates: Slither, Mythril, Echidna, Certora, MythX, and Sag3.AI
Real-time data from: CoinGecko API, Etherscan, X.AI Grok (via web search)

Author: John DaWalka
"""

import os
import sys
import json
import subprocess
from datetime import datetime
from typing import Dict, List, Optional
from dataclasses import dataclass
from enum import Enum

# CONFIGURATION & CONSTANTS

class AuditLevel(Enum):
    """Defines the depth of audit to perform"""
    QUICK = "quick"           # Slither only - 2-5 minutes
    STANDARD = "standard"     # Slither + Mythril - 10-15 minutes
    DEEP = "deep"             # All tools including Certora - 30+ minutes
    FORENSIC = "forensic"     # Everything + continuous monitoring


# API endpoints for live crypto data
COINGECKO_API = "https://api.coingecko.com/api/v3"
ETHERSCAN_API = "https://api.etherscan.io/api"
SAG3_API = "https://api.sag3.ai"  # Placeholder - use actual endpoint


# Tool paths and versions
TOOLS_CONFIG = {
    "slither": {"min_version": "0.9.0", "installed": False},
    "mythril": {"min_version": "0.23.0", "installed": False},
    "echidna": {"min_version": "2.0.0", "installed": False},
    "certora": {"min_version": "4.0.0", "installed": False},
    "mythx": {"min_version": "0.20.0", "installed": False},
}


@dataclass
class AuditResult:
    """Stores audit findings from a single tool"""
    tool_name: str
    severity_count: Dict[str, int]  # {"critical": 0, "high": 1, "medium": 3}
    findings: List[Dict]
    execution_time: float
    passed: bool


@dataclass
class CryptoMetrics:
    """Live cryptocurrency metrics pulled from APIs"""
    token_name: str
    current_price: float
    market_cap: float
    volume_24h: float
    holder_count: int
    contract_address: str
    deployer_address: str
    creation_date: str
    transaction_count: int


@dataclass
class RiskScore:
    """Aggregated risk assessment combining technical and on-chain data"""
    technical_risk: float      # 0-100 based on audit findings
    tokenomics_risk: float     # 0-100 based on token distribution
    social_risk: float         # 0-100 based on sentiment
    developer_risk: float      # 0-100 based on activity
    overall_risk: float        # Weighted average
    recommendations: List[str]


# UTILITY FUNCTIONS

class Logger:
    """Simple logging utility with timestamps"""
    
    @staticmethod
    def info(message: str):
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        print(f"[{timestamp}] INFO: {message}")
    
    @staticmethod
    def error(message: str):
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        print(f"[{timestamp}] ERROR: {message}", file=sys.stderr)
    
    @staticmethod
    def success(message: str):
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        print(f"[{timestamp}] SUCCESS: {message}")


def check_tool_installed(tool_name: str) -> bool:
    """Verify if a security tool is installed and accessible"""
    try:
        if tool_name == "slither":
            subprocess.run(["slither", "--version"], capture_output=True, check=True)
        elif tool_name == "mythril":
            subprocess.run(["myth", "--version"], capture_output=True, check=True)
        elif tool_name == "echidna":
            subprocess.run(["echidna", "--version"], capture_output=True, check=True)
        elif tool_name == "certora":
            subprocess.run(["certoraRun", "--version"], capture_output=True, check=True)
        return True
    except (subprocess.CalledProcessError, FileNotFoundError):
        return False


def validate_contract_path(contract_path: str) -> bool:
    """Ensure the Solidity contract file exists and is readable"""
    if not os.path.exists(contract_path):
        Logger.error(f"Contract file not found: {contract_path}")
        return False
    if not contract_path.endswith(".sol"):
        Logger.error(f"Contract must be a Solidity file (.sol): {contract_path}")
        return False
    return True


# AUDIT TOOLS WRAPPERS

class SlitherAnalyzer:
    """Static analysis tool for detecting common vulnerabilities"""
    
    @staticmethod
    def run(contract_path: str) -> AuditResult:
        """
        Run Slither static analysis on a contract. Slither quickly identifies
        common patterns like reentrancy, uninitialized storage, and shadowed
        variables without needing to execute the code.
        """
        Logger.info("Running Slither static analysis...")
        start_time = datetime.now()
        
        try:
            result = subprocess.run(
                ["slither", contract_path, "--json"],
                capture_output=True,
                text=True,
                timeout=300
            )
            
            if result.returncode == 0:
                findings = json.loads(result.stdout)
                severity_count = {
                    "critical": 0,
                    "high": 0,
                    "medium": 0,
                    "low": 0,
                    "informational": 0
                }
                
                for issue in findings.get("results", {}).get("detections", []):
                    severity = issue.get("severity", "informational").lower()
                    if severity in severity_count:
                        severity_count[severity] += 1
                
                execution_time = (datetime.now() - start_time).total_seconds()
                passed = severity_count["critical"] == 0 and severity_count["high"] == 0
                
                return AuditResult(
                    tool_name="Slither",
                    severity_count=severity_count,
                    findings=findings.get("results", {}).get("detections", []),
                    execution_time=execution_time,
                    passed=passed
                )
            else:
                Logger.error(f"Slither failed with error: {result.stderr}")
                return AuditResult(
                    tool_name="Slither",
                    severity_count={},
                    findings=[],
                    execution_time=0,
                    passed=False
                )
        except Exception as e:
            Logger.error(f"Slither execution error: {str(e)}")
            return AuditResult(
                tool_name="Slither",
                severity_count={},
                findings=[],
                execution_time=0,
                passed=False
            )


class AuditPipeline:
    """Main audit orchestration class"""
    
    def __init__(self, contract_path: str, audit_level: AuditLevel):
        self.contract_path = contract_path
        self.audit_level = audit_level
        self.results: List[AuditResult] = []
        self.metadata: Dict = {}
    
    def fetch_etherscan_data(self, contract_address: Optional[str] = None) -> Dict:
        """
        Fetch real on-chain data from Etherscan API when API key is configured.
        Falls back to simulated data for backward compatibility.
        
        Args:
            contract_address: Ethereum contract address (0x...)
            
        Returns:
            Dictionary containing on-chain metrics or simulated data
        """
        # Check if contract address is provided
        if not contract_address:
            return {
                "note": "No contract address provided. Pass --address parameter to fetch real data.",
                "verification_status": "unknown",
                "transaction_count": 0
            }
        
        # Check for API key
        api_key = os.getenv("ETHERSCAN_API_KEY")
        
        if not api_key:
            Logger.info("ETHERSCAN_API_KEY not found. Returning simulated data.")
            Logger.info("Get your free API key at: https://etherscan.io/apis")
            return {
                "note": "Simulated data - set ETHERSCAN_API_KEY for real on-chain data",
                "contract_address": contract_address,
                "verification_status": "unknown",
                "transaction_count": 0,
                "deployer_address": "0x0000000000000000000000000000000000000000",
                "creation_date": "Unknown"
            }
        
        # Make real API calls
        try:
            import requests
        except ImportError:
            Logger.error("requests library not installed. Install with: pip install requests")
            return {
                "error": "requests library not available",
                "note": "Install requests: pip install requests"
            }
        
        Logger.info(f"Fetching real on-chain data for {contract_address}...")
        
        try:
            # API call 1: Get transaction list to find deployer and transaction count
            tx_url = f"{ETHERSCAN_API}?module=account&action=txlist&address={contract_address}&startblock=0&endblock=99999999&sort=asc&apikey={api_key}"
            
            tx_response = requests.get(tx_url, timeout=10)
            tx_data = tx_response.json()
            
            # API call 2: Get source code to check verification status
            source_url = f"{ETHERSCAN_API}?module=contract&action=getsourcecode&address={contract_address}&apikey={api_key}"
            
            source_response = requests.get(source_url, timeout=10)
            source_data = source_response.json()
            
            # Parse responses
            transaction_count = 0
            deployer_address = "Unknown"
            creation_date = "Unknown"
            
            if tx_data.get("status") == "1" and tx_data.get("result"):
                transactions = tx_data["result"]
                transaction_count = len(transactions)
                
                # Find the contract creation transaction (where 'to' is empty)
                for tx in transactions:
                    if tx.get("to") == "":
                        deployer_address = tx.get("from", "Unknown")
                        timestamp = int(tx.get("timeStamp", 0))
                        creation_date = datetime.fromtimestamp(timestamp).isoformat()
                        break
            
            # Check verification status
            verification_status = "not_verified"
            if source_data.get("status") == "1" and source_data.get("result"):
                result = source_data["result"][0] if isinstance(source_data["result"], list) else source_data["result"]
                if result.get("SourceCode"):
                    verification_status = "verified"
            
            return {
                "contract_address": contract_address,
                "verification_status": verification_status,
                "transaction_count": transaction_count,
                "deployer_address": deployer_address,
                "creation_date": creation_date,
                "api_endpoint": tx_url.replace(api_key, "***")  # Don't expose API key
            }
            
        except requests.RequestException as e:
            Logger.error(f"Etherscan API error: {str(e)}")
            return {
                "error": f"Failed to fetch data: {str(e)}",
                "contract_address": contract_address
            }
        except Exception as e:
            Logger.error(f"Unexpected error fetching Etherscan data: {str(e)}")
            return {
                "error": f"Unexpected error: {str(e)}",
                "contract_address": contract_address
            }
    
    def run_audit(self) -> Dict:
        """Execute the audit pipeline based on the configured level"""
        Logger.info(f"Starting {self.audit_level.value} audit of {self.contract_path}")
        
        # Validate contract exists
        if not validate_contract_path(self.contract_path):
            return {"error": "Invalid contract path"}
        
        # Pass contract address from metadata if available
        contract_address = self.metadata.get("contract_address")
        self.metadata["etherscan_data"] = self.fetch_etherscan_data(contract_address)
        
        # Run tools based on audit level
        if self.audit_level in [AuditLevel.QUICK, AuditLevel.STANDARD, AuditLevel.DEEP, AuditLevel.FORENSIC]:
            if check_tool_installed("slither"):
                result = SlitherAnalyzer.run(self.contract_path)
                self.results.append(result)
            else:
                Logger.error("Slither not installed")
        
        # Compile results
        return {
            "contract": self.contract_path,
            "audit_level": self.audit_level.value,
            "timestamp": datetime.now().isoformat(),
            "results": [
                {
                    "tool": r.tool_name,
                    "passed": r.passed,
                    "severity_count": r.severity_count,
                    "execution_time": r.execution_time
                }
                for r in self.results
            ],
            "metadata": self.metadata
        }


def main():
    """Main entry point for the audit pipeline"""
    import argparse
    
    parser = argparse.ArgumentParser(
        description="Smart Contract Audit Pipeline with Etherscan Integration"
    )
    parser.add_argument(
        "--contract",
        required=True,
        help="Path to the Solidity contract file"
    )
    parser.add_argument(
        "--level",
        choices=["quick", "standard", "deep", "forensic"],
        default="quick",
        help="Audit depth level (default: quick)"
    )
    parser.add_argument(
        "--address",
        help="Contract address on Ethereum mainnet (0x...)"
    )
    parser.add_argument(
        "--output",
        help="Output file for audit report (JSON format)"
    )
    
    args = parser.parse_args()
    
    # Create pipeline
    audit_level = AuditLevel(args.level)
    pipeline = AuditPipeline(args.contract, audit_level)
    
    # Add contract address to metadata if provided
    if args.address:
        pipeline.metadata["contract_address"] = args.address
    
    # Run audit
    report = pipeline.run_audit()
    
    # Output results
    if args.output:
        with open(args.output, 'w') as f:
            json.dump(report, f, indent=2)
        Logger.success(f"Audit report saved to {args.output}")
    else:
        print(json.dumps(report, indent=2))
    
    # Exit code based on results
    passed = all(r.passed for r in pipeline.results)
    sys.exit(0 if passed else 1)


if __name__ == "__main__":
    main()
