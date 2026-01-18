# Crypto Portfolio Tracker

<!-- 
This is a professional-grade cryptocurrency portfolio tracking application built with React. 
The purpose of this tool is to help traders, coaches, and serious investors monitor their 
crypto holdings in real-time, track staking yields, and visualize their portfolio performance. 
This README provides comprehensive documentation for setup, usage, and contribution.
-->

<!-- 
===========================================
SECTION 1: PROJECT OVERVIEW & FEATURES
===========================================
This section introduces the project and explains what makes it valuable for users.
-->

A professional-grade React application for tracking cryptocurrency holdings with live price data, staking yield calculations, and Sag3.ai signal integration capabilities. Built for serious traders, crypto coaches, and portfolio managers who need accurate, real-time portfolio insights.

## Key Features

<!-- 
The following features represent the core functionality of the tracker. 
These are organized by category to help users understand what each feature does and why it matters.
-->

**Real-Time Market Data**: The application connects to the CoinGecko API to fetch live cryptocurrency prices. This means you always see current market values without any delay or manual updates.

**Comprehensive Portfolio Tracking**: Monitor multiple cryptocurrency holdings across different blockchains simultaneously. The tracker handles diverse assets from major cryptocurrencies like Bitcoin and Ethereum to smaller altcoins and layer-2 tokens.

**Staking Yield Calculations**: Automatically calculate Annual Percentage Yield (APY) and project your earning potential. The tool computes both annual and monthly reward estimates based on your staked amount and the current APY of each asset.

**24-Hour Price Change Visualization**: See which of your assets are gaining or losing value in the current day. Color-coded indicators (green for gains, red for losses) make it easy to spot trends at a glance.

**Mobile-Responsive Design**: The application works perfectly on desktop computers, tablets, and smartphones. This is particularly useful for crypto coaches who need to access their portfolio data while coaching clients.

**Sag3.ai Integration Ready**: While the tool doesn't directly connect to Sag3.ai's web interface, it's designed to work alongside Sag3.ai. You can manually input Sag3.ai trading signals and view them alongside your portfolio metrics for comprehensive analysis.

**Zero-Cost Data Sources**: The application uses only free APIs, meaning you never pay subscription fees for live data. This makes it sustainable for long-term use.

**Smart Contract Audit Pipeline**: Comprehensive security audit tool for Solidity smart contracts with real-time Etherscan integration. Supports multiple audit levels and fetches on-chain metrics like transaction count, verification status, and deployer information. See [AUDIT_PIPELINE.md](AUDIT_PIPELINE.md) for details.

<!-- 
===========================================
SECTION 2: INSTALLATION & SETUP
===========================================
This section guides new users through getting the project running on their machine.
-->

## Getting Started

### What You Need Before Installing

Before you can run this project, make sure your computer has the following software installed. These are the minimum requirements.

**Node.js**: Download and install Node.js version 16 or higher from nodejs.org. Node.js includes npm (Node Package Manager), which manages all the project dependencies. You can verify your installation by opening a terminal and typing `node --version` and `npm --version`.

**Git**: Install Git from git-scm.com so you can clone the repository to your computer. Git is also useful for version control and pushing changes back to GitHub.

**A Code Editor** (recommended but not required): Visual Studio Code is a popular choice and works well for React development, but any text editor will work.

### Step-by-Step Installation

The following instructions will get the project running on your local machine for development and testing purposes.

**Step 1: Clone the Repository**

Open your terminal or command prompt and navigate to where you want to store this project. Then run the following command to download the entire project to your computer.

```bash
git clone https://github.com/JohnDaWalka/Portfolio-Crypto-Tracker.git
cd Portfolio-Crypto-Tracker
git checkout master
```

This command first downloads the project from GitHub, navigates into the project folder, and checks out the master branch (the base branch for this repository).

**Step 2: Install Dependencies**

The project depends on several external libraries like React and Tailwind CSS. Run this command to download and install all required dependencies.

```bash
npm install
```

This reads the package.json file (which lists all dependencies) and installs them in a node_modules folder. This might take a few minutes on first install.

**Step 3: Set Up Environment Variables**

Copy the example environment file to create your own local configuration file.

```bash
cp .env.example .env
```

Open the new `.env` file in your code editor and configure any API keys or settings you need. For basic usage with CoinGecko, you don't need to add anything.

**Step 4: Start the Development Server**

Run the development server so you can see your changes in real-time as you code.

```bash
npm run dev
```

The application will typically start on `http://localhost:5173`. Open this URL in your web browser to see the tracker running.

<!-- 
===========================================
SECTION 3: PROJECT STRUCTURE
===========================================
This section explains how the project is organized and what each folder contains.
Understanding the structure helps developers navigate the codebase and know where to add new features.
-->

## Project Organization

The project is organized into several folders, each serving a specific purpose. Understanding this structure helps you find files quickly and know where to add new code.

```
Portfolio-Crypto-Tracker/
├── src/
│   ├── components/
│   │   ├── PortfolioTracker.jsx       
│   │   │   <!-- Main component that combines all other components -->
│   │   │   <!-- This is what gets displayed to users -->
│   │   │
│   │   ├── HoldingsTable.jsx          
│   │   │   <!-- Displays the detailed table of all cryptocurrency holdings -->
│   │   │   <!-- Shows price, change, value, and staking information -->
│   │   │
│   │   ├── SummaryCards.jsx           
│   │   │   <!-- Shows the big picture metrics at the top of the page -->
│   │   │   <!-- Displays total portfolio value and annual staking rewards -->
│   │   │
│   │   └── Sag3Integration.jsx        
│   │       <!-- Component for adding Sag3.ai trading signals manually -->
│   │       <!-- Allows users to note which assets have signals -->
│   │
│   ├── services/
│   │   ├── priceApi.js                
│   │   │   <!-- Handles all communication with the CoinGecko API -->
│   │   │   <!-- Fetches live prices and market data -->
│   │   │
│   │   ├── calculations.js            
│   │   │   <!-- Pure calculation functions for portfolio metrics -->
│   │   │   <!-- Computes staking rewards, portfolio value, etc -->
│   │   │
│   │   └── storage.js                 
│   │       <!-- Manages saving and retrieving data from browser storage -->
│   │       <!-- Keeps user preferences and portfolio data persistent -->
│   │
│   ├── hooks/
│   │   ├── usePriceData.js            
│   │   │   <!-- Custom React hook for fetching and updating prices -->
│   │   │   <!-- Handles automatic refresh every 60 seconds -->
│   │   │
│   │   └── usePortfolio.js            
│   │       <!-- Custom React hook for managing portfolio state -->
│   │       <!-- Handles adding, removing, and updating holdings -->
│   │
│   ├── styles/
│   │   └── tailwind.css               
│   │       <!-- Tailwind CSS configuration and global styles -->
│   │       <!-- Defines the color scheme and responsive breakpoints -->
│   │
│   ├── App.jsx                        
│   │   <!-- Root component that wraps everything -->
│   │   <!-- Sets up any global state or providers -->
│   │
│   └── index.jsx                      
│       <!-- Entry point for the React application -->
│       <!-- Mounts the App component to the DOM -->
│
├── public/
│   └── index.html
│       <!-- The main HTML file that gets served to browsers -->
│       <!-- React components get inserted into this file -->
│
├── .env.example
│   <!-- Template for environment variables -->
│   <!-- Copy this to .env and fill in your own values -->
│
├── .gitignore
│   <!-- Tells Git which files not to track -->
│   <!-- Typically includes node_modules and .env files -->
│
├── package.json
│   <!-- Lists all project dependencies and scripts -->
│   <!-- This is like a recipe that tells npm what to install -->
│
├── vite.config.js
│   <!-- Configuration for Vite, the build tool used by this project -->
│   <!-- Defines how the project is bundled and optimized -->
│
├── README.md
│   <!-- This file - comprehensive project documentation -->
│
├── CONTRIBUTING.md
│   <!-- Guidelines for developers who want to contribute -->
│
└── LICENSE
    <!-- Legal license for the project (typically MIT) -->
```

<!-- 
===========================================
SECTION 4: CONFIGURATION & CUSTOMIZATION
===========================================
This section explains how to customize the application for your specific needs.
-->

## Configuring Your Portfolio

The tracker needs to know what cryptocurrencies you own and how much you hold. There are two ways to configure this.

### Method 1: Edit the Configuration File

The simplest way to add your holdings is to edit the portfolio configuration file. Create a file at `src/data/portfolio.json` (you may need to create the data folder if it doesn't exist) with the following structure.

```json
{
  "holdings": [
    {
      "name": "Avalanche",
      "symbol": "AVAX",
      "holdings": 1.5,
      "stakedPercent": 100,
      "stakingAPY": 7.55,
      "blockchain": "avalanche-2"
    },
    {
      "name": "Polkadot",
      "symbol": "DOT",
      "holdings": 2.1,
      "stakedPercent": 100,
      "stakingAPY": 7.55,
      "blockchain": "polkadot"
    }
  ]
}
```

Each holding needs the following information. The `name` field is the full name of the cryptocurrency. The `symbol` is the ticker symbol (like AVAX or BTC). The `holdings` value is how much of that cryptocurrency you own. The `stakedPercent` is what percentage of your holdings are currently staked (100 means fully staked, 50 means half staked). The `stakingAPY` is the annual percentage yield you receive from staking that asset. The `blockchain` field helps identify which chain the token lives on.

### Method 2: Use the User Interface

Once the application is running, you can add holdings directly through the interface without editing code. This is more convenient for regular updates.

### Environment Variables

Create a `.env` file in the project root with the following optional settings. These variables control how the application behaves.

```
VITE_COINGECKO_API_KEY=your_api_key_here
<!-- If you have a CoinGecko API key, paste it here. Leave blank for free tier. -->

VITE_REFRESH_INTERVAL=60000
<!-- How often prices update in milliseconds. 60000 = every 60 seconds. Lower values = more API calls. -->

VITE_ENABLE_SAG3_INTEGRATION=true
<!-- Set to false if you don't want to see the Sag3.ai integration component. -->
```

<!-- 
===========================================
SECTION 5: API DOCUMENTATION & DATA SOURCES
===========================================
This section explains which external APIs the project uses and how to use them.
-->

## Understanding the Data Sources

The tracker pulls information from external APIs. Understanding how these work helps you troubleshoot issues and optimize performance.

### CoinGecko API - Live Price Data

The application uses CoinGecko's free API to fetch real-time cryptocurrency prices. CoinGecko is one of the most reliable cryptocurrency data providers and their free tier is generous.

**What Data We Get**: Current price in USD, 24-hour price changes, market capitalization, and trading volume.

**API Rate Limits**: The free tier allows 10 to 50 calls per minute depending on how many people are using it. This is usually plenty for a personal portfolio tracker.

**API Documentation**: You can read the full documentation at https://www.coingecko.com/en/api/documentation

**How It's Used in the Code**: The `src/services/priceApi.js` file handles all communication with CoinGecko. The `usePriceData` hook in `src/hooks/usePriceData.js` wraps this functionality and automatically refreshes prices every 60 seconds.

### Sag3.ai Integration - Manual Signal Entry

Unlike CoinGecko, Sag3.ai doesn't have a publicly available API for their web interface. Instead, the tracker is designed to work alongside Sag3.ai.

**How It Works**: You log into your Sag3.ai account on the web and review their AI-generated trading signals. For assets you're interested in, you manually note the signal (buy, hold, sell, strong buy, etc) and confidence level. Back in the portfolio tracker, you can add this information to your holdings using the Sag3Integration component.

**Why Manual Entry**: This approach actually has advantages. It forces you to actively review Sag3.ai's analysis rather than blindly following signals. It also ensures the tracker never has access to your Sag3.ai credentials.

**Storing Signals**: Signals are stored in your browser's local storage, so they persist even if you close and reopen the application.

<!-- 
===========================================
SECTION 6: USAGE & EXAMPLES
===========================================
This section provides practical examples of how to use the code.
-->

## How to Use the Application

### Basic Usage

Once the application is running, you'll see your portfolio dashboard. The page is divided into several sections.

**Summary Cards at the Top**: These three cards show your total portfolio value in USD, your projected annual staking rewards, and the current data status. The data status shows whether prices are currently updating and when they were last fetched.

**Holdings Table Below**: This detailed table lists every cryptocurrency you own. Each row shows the current price, 24-hour change, your holdings amount, total value, percentage staked, and annual staking rewards for that specific asset.

**Automatic Updates**: Prices automatically refresh every 60 seconds. You don't need to manually refresh or do anything.

### Using the Portfolio Tracker for Coaching

If you're a crypto coach, this tool becomes an educational asset. Here are some ways to use it with clients.

**Live Demonstration**: Pull up the tracker on your screen and show how staking yields compound over time. Pause at specific holdings to discuss why you chose certain APY rates or blockchains.

**Risk Education**: Use the diversification of your portfolio to teach clients about spreading risk across different chains and assets.

**Real-World Examples**: Show clients how much you actually earn in monthly staking rewards versus what they might see in marketing materials.

**Performance Analysis**: Export your portfolio data (explained below) to show clients how your portfolio performs over weeks and months.

### Exporting Portfolio Data

You can export your portfolio information for analysis, record-keeping, or sharing with clients. Different export formats serve different purposes.

```bash
npm run export:csv
<!-- Exports data as a comma-separated values file that opens in Excel or Google Sheets -->

npm run export:json
<!-- Exports data as JSON, useful for programmatic processing -->

npm run export:pdf
<!-- Creates a formatted PDF report of your portfolio (premium feature) -->
```

### Code Examples for Developers

If you want to extend the tracker or use its calculation functions in other projects, here are some examples.

**Importing the Tracker Component**: This example shows how to use the main tracker component in your own React application.

```javascript
import PortfolioTracker from './components/PortfolioTracker';

export default function App() {
  return (
    <div>
      <h1>My Dashboard</h1>
      <PortfolioTracker />
    </div>
  );
}
```

**Using Calculation Functions**: The calculations module exports utility functions for computing portfolio metrics. You can use these to build your own components.

```javascript
import { 
  calculateStakingRewards, 
  calculatePortfolioMetrics 
} from './services/calculations';

const holdings = [
  { name: 'Bitcoin', symbol: 'BTC', amount: 0.5, stakedPercent: 100, stakingAPY: 5 }
];

const prices = { bitcoin: { usd: 45000 } };

const rewards = calculateStakingRewards(holdings, prices);
// Returns: annual, monthly, daily staking reward estimates

const metrics = calculatePortfolioMetrics(holdings, prices);
// Returns: total value, diversification stats, risk metrics
```

**Accessing Price Data with the Custom Hook**: React hooks are special functions that manage state and side effects. This example shows how to use the price data hook.

```javascript
import { usePriceData } from './hooks/usePriceData';

function MyComponent() {
  // This hook returns current prices, loading status, and any errors
  const { prices, loading, error } = usePriceData([
    'bitcoin', 
    'ethereum', 
    'avalanche-2'
  ]);
  
  if (loading) return <p>Loading prices...</p>;
  if (error) return <p>Error: {error}</p>;
  
  return (
    <div>
      <p>Bitcoin: ${prices.bitcoin.usd}</p>
      <p>Ethereum: ${prices.ethereum.usd}</p>
      <p>Avalanche: ${prices['avalanche-2'].usd}</p>
    </div>
  );
}
```

<!-- 
===========================================
SECTION 7: DEVELOPMENT & CONTRIBUTION
===========================================
This section guides developers who want to contribute to the project.
-->

## Development Workflow

### Available Development Commands

The `package.json` file defines several scripts that help with development. Run these commands in your terminal from the project directory.

```bash
npm run dev
<!-- Starts the development server with hot reloading -->
<!-- Changes you make are instantly visible in your browser -->

npm run build
<!-- Creates an optimized production build -->
<!-- This creates a dist/ folder with minified files -->

npm run preview
<!-- Shows what the production build looks like -->
<!-- Useful for testing before deploying -->

npm run lint
<!-- Checks code for style issues and common mistakes -->
<!-- Helps maintain consistent code quality -->

npm run format
<!-- Automatically fixes code formatting -->
<!-- Makes all code follow the same style -->

npm test
<!-- Runs automated tests to catch bugs -->
<!-- Tests verify that functions work as expected -->
```

### Adding a New Cryptocurrency to Track

To add support for a new cryptocurrency, follow these steps.

**Step 1: Find the CoinGecko ID**: Visit coingecko.com and search for your cryptocurrency. Look at the URL - the part after `/en/coins/` is the ID you need.

**Step 2: Add to Portfolio Data**: Edit `src/data/portfolio.json` and add a new object to the holdings array with the correct symbol and blockchain ID.

**Step 3: Test the Integration**: Restart the development server with `npm run dev` and verify that prices are fetching correctly for your new asset.

**Step 4: Commit Your Changes**: If you're contributing back to the project, use Git to commit your changes with a descriptive message.

```bash
git add src/data/portfolio.json
git commit -m "Add support for [Cryptocurrency Name]"
```

### Performance Optimization Tips

If the application feels slow, consider these optimizations.

**Reduce the Number of Tracked Assets**: Each asset requires an API call. Tracking fewer assets means fewer requests and faster updates.

**Increase the Refresh Interval**: Changing `VITE_REFRESH_INTERVAL` to 120000 (2 minutes) instead of 60000 (1 minute) cuts API calls in half.

**Use Browser Caching**: The application stores prices locally, so opening it multiple times in quick succession uses cached data rather than hitting the API again.

**Close Unnecessary Browser Tabs**: Having many tabs open can slow down your entire browser, not just this application.

**Check System Resources**: If your computer is running slowly, close background applications to free up memory and CPU power.

<!-- 
===========================================
SECTION 8: SECURITY & PRIVACY
===========================================
This section explains important security considerations for users.
-->

## Security & Safety Considerations

Security is critically important when dealing with cryptocurrency and financial data. Please read this section carefully.

### What This Application DOES NOT Do

This is the most important part. The application deliberately avoids these actions to keep you safe.

**Never Stores Private Keys**: This application never asks for, stores, or transmits your private keys or seed phrases. If any application or website asks for these, it's a scam.

**Never Stores Wallet Passwords**: Your wallet passwords are secret. This application doesn't need them and won't store them.

**Never Makes Transactions**: The tracker only reads and displays data. It cannot send, receive, or move cryptocurrency. You must approve all transactions manually in your actual wallet.

**Never Connects to External Wallets**: While some applications connect to MetaMask or other wallets, this tracker doesn't. Your wallet remains completely separate and secure.

### Best Practices for Safe Usage

Follow these guidelines to keep your financial data safe.

**Keep Your Data Local**: Run this application on your personal computer rather than on shared networks or public computers. This ensures only you can access your portfolio data.

**Use Strong Passwords**: If you password-protect your computer, use a strong, unique password. This adds a layer of security to everything on your computer, including your portfolio data.

**Keep Your Credentials Secure**: Your Sag3.ai login should be kept private. Only you should access Sag3.ai on your personal devices.

**Review Your Code**: Since this is open-source and available on GitHub, you can review the code to see exactly what it does. If you're not a programmer, ask a trusted developer to review it for you.

**Enable Two-Factor Authentication**: For your Sag3.ai account and GitHub account, enable two-factor authentication if available. This prevents unauthorized access even if someone learns your password.

<!-- 
===========================================
SECTION 9: DEPLOYMENT & PRODUCTION USE
===========================================
This section explains how to deploy the application for public use.
-->

## Deploying to Production

Once you're confident in the tracker, you might want to deploy it so you can access it from anywhere (not just your local computer). Several platforms make this easy.

### Deploy to Vercel

Vercel is a platform optimized for deploying modern web applications. They offer free tier options perfect for personal projects.

**Prerequisites**: You need a GitHub account and a Vercel account (both free).

**Deployment Steps**: First, push your project to GitHub using Git. Then go to vercel.com and log in. Click "New Project" and select your Portfolio-Crypto-Tracker repository. Vercel automatically detects that it's a React project and configures everything. Click "Deploy" and your application goes live on the internet.

```bash
npm install -g vercel
vercel
```

### Deploy to GitHub Pages

GitHub Pages allows you to host static websites for free directly from your GitHub repository.

```bash
npm run build
npm run deploy
```

### Docker Deployment

Docker lets you package your application with all its dependencies, making it easy to run on any server.

**Create a Dockerfile** in your project root:

```dockerfile
FROM node:18-alpine
WORKDIR /app
COPY package*.json ./
RUN npm install
COPY . .
RUN npm run build
EXPOSE 3000
CMD ["npm", "run", "preview"]
```

**Build and Run**:

```bash
docker build -t crypto-tracker .
docker run -p 3000:3000 crypto-tracker
```

<!-- 
===========================================
SECTION 10: TROUBLESHOOTING
===========================================
This section helps solve common problems users might encounter.
-->

## Troubleshooting Common Issues

### Prices Are Not Updating

If you notice that cryptocurrency prices aren't changing or the "Last Updated" time isn't advancing, there are several things to check.

**Check Your Internet Connection**: This is the most common cause. Open another website in your browser to verify you're connected to the internet. If other websites work but the tracker doesn't update, continue to the next steps.

**Verify CoinGecko API is Accessible**: Sometimes CoinGecko's API experiences temporary outages. Go to https://status.coingecko.com to check if they're having issues. If they are, the tracker will automatically resume updating once CoinGecko is back online.

**Check Browser Console for Errors**: Open your browser's developer tools (F12 or right-click and select "Inspect"). Go to the "Console" tab and look for red error messages. These often provide clues about what's wrong.

**Check Your Rate Limiting**: If you've configured a CoinGecko API key and are making many requests, you might be hitting rate limits. Try increasing the `VITE_REFRESH_INTERVAL` value to make updates less frequent.

### Portfolio Data Not Saving

If you add holdings but they disappear when you close and reopen the application, your data isn't being saved properly.

**Clear Browser Cache and Local Storage**: Sometimes corrupt cached data prevents new data from saving. In your browser, press Ctrl+Shift+Delete (Windows) or Command+Shift+Delete (Mac). Select "All time" and check "Local storage". Click "Clear".

**Check Browser Console for Errors**: Similar to the previous issue, look for error messages in the console that might indicate what's wrong with saving.

**Enable Local Storage**: Verify that your browser hasn't disabled local storage. Some privacy-focused browser settings disable this feature.

**Try Exporting and Re-importing Data**: Export your portfolio to JSON. Then clear your browser data and re-import the JSON file. This often resolves corrupted data issues.

### Application Running Slowly

If the tracker feels sluggish or unresponsive, try these optimization steps.

**Reduce Number of Tracked Assets**: The more cryptocurrencies you track, the more data the application needs to fetch and process. Consider removing assets you're not actively monitoring.

**Increase Refresh Interval**: Edit your `.env` file and change `VITE_REFRESH_INTERVAL` to a higher number, like 180000 (3 minutes) instead of 60000 (1 minute).

**Close Background Applications**: Running many applications at once can slow your computer. Close applications you're not using to free up memory and processing power.

**Try a Different Browser**: If one browser is slow, try Chrome, Firefox, Safari, or Edge to see if the issue persists. Sometimes one browser handles web applications better than others.

### "Cannot Find Module" Errors

If you see an error about a missing module when you start the development server, dependencies weren't installed correctly.

**Reinstall Dependencies**: Run `npm install` again. Sometimes the first install is interrupted or incomplete.

**Delete node_modules Folder**: Delete the `node_modules` folder and the `package-lock.json` file. Then run `npm install` fresh.

**Update npm**: Make sure you have the latest version of npm by running `npm install -g npm@latest`.

<!-- 
===========================================
SECTION 11: ROADMAP & FUTURE FEATURES
===========================================
This section describes planned features and improvements.
-->

## Planned Features & Roadmap

The development roadmap shows features that are planned for future releases. These features are not yet available but are coming soon.

**Advanced Charting** (In Progress): Integration with TradingView Lite will allow you to see interactive price charts directly in the tracker without leaving the application.

**Direct Sag3.ai API Integration** (Planned): Currently you manually enter Sag3.ai signals. In the future, we hope to integrate directly with Sag3.ai's API so signals sync automatically.

**Portfolio Alerts & Notifications** (Planned): Set price targets or yield thresholds. The application will notify you when conditions are met, like when a token drops 10% or your rewards reach a milestone.

**Multi-Wallet Support** (Planned): Currently the tracker is manual. Eventually you'll be able to connect multiple wallets and see all holdings in one view.

**Tax Reporting** (Planned): Built-in tax report generation to simplify crypto tax preparation. This will calculate your cost basis and gains/losses automatically.

**Machine Learning Price Predictions** (Planned): AI-powered price forecasts based on historical data and market trends. These predictions will help inform your coaching recommendations.

**Mobile App** (Planned): A native mobile application built with React Native for iOS and Android. This will let you track your portfolio from your phone with full functionality.

<!-- 
===========================================
SECTION 12: SUPPORT & RESOURCES
===========================================
This section explains how to get help and find more information.
-->

## Getting Help & Support

### Troubleshooting Resources

Before reaching out for support, try these resources which often solve problems quickly.

**Search Existing GitHub Issues**: Other people may have experienced the same problem. Visit the GitHub Issues page and search for keywords related to your issue.

**Check the Documentation**: This README file covers most common questions. Use your browser's find function (Ctrl+F or Command+F) to search for keywords.

**Review Stack Overflow**: The programming community answers many React and JavaScript questions on stackoverflow.com. Search for your error message there.

### Getting Support

If you've tried the above and still need help, contact us through these channels.

**Create a GitHub Issue**: Go to the Issues tab on the GitHub repository and describe your problem in detail. Include any error messages, what you were doing when the error occurred, and what you've already tried to fix it. This is the primary support channel for this project.

### Additional Learning Resources

**React Documentation**: https://react.dev - Official React documentation and tutorials

**CoinGecko API Documentation**: https://www.coingecko.com/en/api/documentation - Reference for price data API

**Tailwind CSS Documentation**: https://tailwindcss.com/docs - Learn about the styling framework we use

**Node.js Documentation**: https://nodejs.org/en/docs - Official Node.js reference

**Git Documentation**: https://git-scm.com/doc - Learn how to use version control

**Smart Contract Audit Pipeline**: See [AUDIT_PIPELINE.md](AUDIT_PIPELINE.md) - Comprehensive guide for the audit pipeline

**Etherscan API Documentation**: https://docs.etherscan.io/ - Reference for on-chain data API

<!-- 
===========================================
SECTION 13: AI-ASSISTED DEVELOPMENT
===========================================
This section explains the AI tools configured for this repository.
-->

## AI-Assisted Development

This repository is configured to work seamlessly with GitHub Copilot and Sourcery-AI to enhance developer productivity and code quality.

### GitHub Copilot Setup

**What is GitHub Copilot?** GitHub Copilot is an AI-powered code assistant that helps you write code faster and with fewer errors. It can complete entire lines or blocks of code, suggest solutions to problems, and even help write tests.

**Repository Configuration**: This repository includes custom instructions in `.github/copilot-instructions.md` that guide GitHub Copilot on:
- Project structure and technology stack
- Coding standards and conventions
- Security requirements and best practices
- Build, test, and deployment commands
- Common patterns used in this codebase

**Getting Started with Copilot**:
1. Install the GitHub Copilot extension in your IDE (VS Code, JetBrains, etc.)
2. Sign up for GitHub Copilot (free for students, open source maintainers)
3. Open any file and start coding - Copilot will suggest completions automatically
4. The custom instructions ensure Copilot understands this project's specific needs

**Copilot Agent for GitHub Issues**: You can also use GitHub Copilot as an autonomous coding agent:
- Assign issues with the label `copilot` to have Copilot work on them
- Copilot will create a branch, make changes, and submit a pull request
- All changes are reviewed by humans before merging
- The agent follows the guidelines in `.github/copilot-instructions.md`

### Sourcery-AI Setup

**What is Sourcery-AI?** Sourcery is an AI-powered code review and refactoring tool specifically for Python. It automatically suggests improvements to make your code cleaner, more efficient, and more Pythonic.

**Repository Configuration**: This repository includes a `.sourcery.yaml` configuration file that:
- Defines code quality standards and thresholds
- Specifies which files and directories to analyze
- Configures refactoring preferences
- Sets up code duplication detection
- Enables security scanning for common vulnerabilities

**Getting Started with Sourcery**:
1. Install Sourcery: `pip install sourcery`
2. Install the Sourcery extension in VS Code or PyCharm (optional)
3. Sourcery will automatically analyze Python files as you work
4. Review and apply Sourcery's suggestions to improve code quality

**Using Sourcery from the Command Line**:
```bash
# Analyze a file
sourcery review audit_pipeline.py

# Automatically apply safe refactorings
sourcery refactor audit_pipeline.py --in-place

# Check code quality score
sourcery login  # One-time setup
sourcery review .
```

**Sourcery with Pre-commit Hooks**: You can integrate Sourcery into your git workflow:
```yaml
# Add to .pre-commit-config.yaml
repos:
  - repo: https://github.com/sourcery-ai/sourcery
    rev: v1.0.0
    hooks:
      - id: sourcery
        args: [--check]
```

### AI Tool Benefits

**For Individual Developers**:
- Faster code writing with intelligent completions
- Automatic code quality improvements
- Real-time security vulnerability detection
- Learning best practices through AI suggestions
- Consistent code style across the project

**For Teams**:
- Standardized coding patterns
- Reduced code review time
- Fewer bugs in production
- Better documentation through AI-assisted comments
- Knowledge sharing through consistent practices

### Best Practices

**When Using AI Tools**:
- Review all AI suggestions before accepting them
- Ensure changes align with project goals
- Test thoroughly after applying AI refactorings
- Use AI as an assistant, not a replacement for thinking
- Report issues or incorrect suggestions to improve the tools

**Configuration Updates**: As the project evolves, update:
- `.github/copilot-instructions.md` for new patterns or requirements
- `.sourcery.yaml` for new Python code quality standards
- Issue templates to help AI understand task requirements better

### Learn More

- **GitHub Copilot Documentation**: https://docs.github.com/en/copilot
- **Copilot Best Practices**: https://docs.github.com/en/copilot/tutorials/coding-agent/get-the-best-results
- **Sourcery Documentation**: https://docs.sourcery.ai/
- **Sourcery Rules**: https://docs.sourcery.ai/refactorings/

<!-- 
===========================================
SECTION 14: CONTRIBUTION GUIDELINES
===========================================
This section explains how developers can contribute to the project.
-->

## Contributing to the Project

We welcome contributions from developers of all skill levels. Whether you're fixing bugs, adding features, or improving documentation, your help makes this project better.

**Note**: This repository uses `master` as its base branch. All pull requests should target the `master` branch, and feature branches should be created from `master`.

### Contribution Process

If you want to contribute, follow this step-by-step process.

**Step 1: Fork the Repository**: Click the "Fork" button on GitHub to create your own copy of the project.

**Step 2: Create a Feature Branch**: In your local repository, create a new branch from the `master` branch for your changes. Use a descriptive name like `feature/add-email-alerts` or `bugfix/fix-price-calculation`.

```bash
git checkout master
git pull --ff-only origin master
git checkout -b feature/your-feature-name
```

**Step 3: Make Your Changes**: Write your code, add tests, and update documentation as needed.

**Step 4: Commit Your Changes**: Use clear, descriptive commit messages that explain what your changes do.

```bash
git commit -m "Add feature description: what this change accomplishes"
```

**Step 5: Push to Your Fork**: Upload your changes to your GitHub fork.

```bash
git push origin feature/your-feature-name
```

**Step 6: Create a Pull Request**: Go to the original repository on GitHub and create a Pull Request from your branch to the `master` branch. Describe your changes and why they're valuable.

### Code Style Guidelines

To keep the codebase consistent and readable, follow these guidelines when writing code.

**Use Meaningful Variable Names**: Write `totalPortfolioValue` instead of `tpv`. Future developers (including yourself) should understand what each variable represents.

**Add Comments for Complex Logic**: Not every line needs a comment, but complex calculations or non-obvious decisions should be explained.

**Follow React Best Practices**: Use functional components, hooks, and proper state management. Avoid class components unless necessary.

**Test Your Changes**: Write tests for new functions. Existing tests should still pass after your changes.

**Format Your Code**: Run `npm run format` before submitting to ensure consistent formatting.

### Types of Contributions We Need

We're always looking for these kinds of contributions.

**Bug Reports**: Found a problem? Report it with steps to reproduce and what you expected to happen.

**Feature Requests**: Have an idea for improvement? Suggest it! Be specific about the problem it solves.

**Code Improvements**: Refactor existing code to be faster, cleaner, or more readable. Performance optimizations are especially welcome.

**Documentation**: Fix typos, clarify confusing sections, or add examples to this README.

**Translations**: Help make the application accessible to non-English speakers by adding translations.

**Tooling and CI/CD**: Help set up automated testing, code quality checks, or deployment pipelines.

<!-- 
===========================================
SECTION 15: LICENSE & LEGAL
===========================================
This section covers the legal aspects of the project.
-->

## License & Legal Information

### MIT License

This project is released under the MIT License, which is one of the most permissive open-source licenses. You can use, modify, and distribute this software with very few restrictions.

**Permission Grants**: The MIT License grants you the right to use this software for any purpose, copy it, modify it, merge it with other software, and distribute it (whether for free or commercially).

**Conditions**: If you distribute this software, you must include the original license and copyright notice. That's it.

**Limitations**: The software is provided "as is" without any warranty. The authors are not responsible for any problems that arise from using this software.

For the complete license text, see the `LICENSE` file
