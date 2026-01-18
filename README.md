# Crypto Portfolio Tracker

A comprehensive cryptocurrency portfolio tracking application built with React, designed to help you monitor your crypto holdings, staking rewards, and portfolio performance in real-time.

<!-- 
===========================================
SECTION 1: TABLE OF CONTENTS
===========================================
-->

## Table of Contents

- [Getting Started](#getting-started)
- [How to Use the Application](#how-to-use-the-application)
- [Understanding the Data Sources](#understanding-the-data-sources)
- [Project Organization](#project-organization)
- [Development Workflow](#development-workflow)
- [Deploying to Production](#deploying-to-production)
- [Troubleshooting](#troubleshooting)
- [Getting Help & Support](#getting-help--support)
- [Contributing to the Project](#contributing-to-the-project)
- [License & Legal Information](#license--legal-information)

<!-- 
===========================================
SECTION 2: GETTING STARTED
===========================================
-->

## Getting Started

### Prerequisites

Before you begin, ensure you have the following installed on your machine:

- **Node.js** (version 18 or higher) - Download from https://nodejs.org
- **npm** (comes with Node.js) - Package manager for JavaScript
- **Git** - Version control system, download from https://git-scm.com

### Step-by-Step Installation

The following instructions will get the project running on your local machine for development and testing purposes.

**Step 1: Clone the Repository**

Open your terminal or command prompt and navigate to where you want to store this project. Then run the following command to download the entire project to your computer.

```bash
git clone https://github.com/JohnDaWalka/crypto-portfolio-tracker.git
cd crypto-portfolio-tracker
```

This command first downloads the project from GitHub, then navigates into the project folder.

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

Edit the `.env` file with your preferred text editor and add any necessary API keys or configuration values.

**Step 4: Start the Development Server**

Once dependencies are installed, start the development server:

```bash
npm run dev
```

This command starts a local development server with hot module replacement. Open your browser and navigate to `http://localhost:5173` (or the URL shown in your terminal) to see the application.

<!-- 
===========================================
SECTION 3: HOW TO USE THE APPLICATION
===========================================
-->

## How to Use the Application

### Basic Usage

1. **Adding Cryptocurrencies**: Click the "Add Asset" button to add a new cryptocurrency to your portfolio
2. **Enter Holdings**: Input the amount of each cryptocurrency you own
3. **Configure Staking**: If you're staking assets, enter the percentage staked and the APY (Annual Percentage Yield)
4. **Monitor Performance**: Watch real-time price updates and portfolio value changes
5. **Track Rewards**: View estimated staking rewards based on your configurations

### Using the Portfolio Tracker for Coaching

If you're a crypto coach using this tracker to help clients:

- **Client Portfolios**: Create separate portfolio instances for different clients
- **Educational Tool**: Use the real-time data to teach about market volatility
- **Performance Analysis**: Export data to show historical performance
- **Risk Assessment**: Help clients understand their portfolio composition

### Exporting Portfolio Data

You can export your portfolio information for analysis, record-keeping, or sharing with clients. Different export formats serve different purposes.

```bash
# Exports data as a comma-separated values file that opens in Excel or Google Sheets
npm run export:csv

# Exports data as JSON, useful for programmatic processing
npm run export:json

# Creates a formatted PDF report of your portfolio (premium feature)
npm run export:pdf
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
const metrics = calculatePortfolioMetrics(holdings, prices);

console.log('Annual Staking Rewards:', rewards);
console.log('Portfolio Metrics:', metrics);
```

**Fetching Price Data**: You can use the price API service directly in your own components.

```javascript
import { fetchPrices } from './services/priceApi';

async function displayPrices() {
  const prices = await fetchPrices(['bitcoin', 'ethereum', 'avalanche-2']);
  
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
SECTION 4: UNDERSTANDING THE DATA SOURCES
===========================================
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

The tracker includes a feature to manually note trading signals from Sag3.ai. This is not an automated integration - you manually enter which assets have active signals.

**Purpose**: Keep track of which cryptocurrencies in your portfolio have buy/sell signals from Sag3.ai
**How to Use**: Click the signal indicator next to any asset to mark it as having an active signal
**Note**: This doesn't automatically fetch signals - it's a manual reminder system

<!-- 
===========================================
SECTION 5: PROJECT ORGANIZATION
===========================================
-->

## Project Organization

Here's how the project files are organized:

```
crypto-portfolio-tracker/
│
├── src/
│   ├── components/
│   │   ├── PortfolioTracker.jsx
│   │   │   <!-- Main component that orchestrates the entire portfolio view -->
│   │   │   <!-- Manages state for holdings, prices, and user interactions -->
│   │   │
│   │   ├── HoldingsList.jsx
│   │   │   <!-- Displays the list of cryptocurrency holdings -->
│   │   │   <!-- Shows current prices, values, and performance metrics -->
│   │   │
│   │   ├── AddHoldingForm.jsx
│   │   │   <!-- Form for adding new cryptocurrencies to portfolio -->
│   │   │   <!-- Validates inputs and handles submission -->
│   │   │
│   │   └── SignalIndicator.jsx
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
│   │   │   <!-- Handles automatic price refresh every 60 seconds -->
│   │   │
│   │   └── usePortfolio.js
│   │       <!-- Custom React hook for managing portfolio state -->
│   │       <!-- Encapsulates add/remove/update operations -->
│   │
│   ├── utils/
│   │   ├── formatters.js
│   │   │   <!-- Utility functions for formatting numbers and currencies -->
│   │   │   <!-- Handles decimal places, currency symbols, percentages -->
│   │   │
│   │   └── validators.js
│   │       <!-- Input validation functions -->
│   │       <!-- Ensures data integrity before saving -->
│   │
│   ├── App.jsx
│   │   <!-- Root component that sets up routing and global providers -->
│   │
│   └── main.jsx
│       <!-- Application entry point, renders App into the DOM -->
│
├── public/
│   <!-- Static assets like images and icons -->
│
├── package.json
│   <!-- Project dependencies and npm scripts -->
│
├── vite.config.js
│   <!-- Vite bundler configuration -->
│
├── tailwind.config.js
│   <!-- Tailwind CSS configuration and theme customization -->
│
└── README.md
    <!-- This file - project documentation -->
```

<!-- 
===========================================
SECTION 6: DEVELOPMENT WORKFLOW
===========================================
-->

## Development Workflow

### Available Development Commands

The `package.json` file defines several scripts that help with development. Run these commands in your terminal from the project directory.

```bash
# Starts the development server with hot reloading
# Changes you make are instantly visible in your browser
npm run dev

# Creates an optimized production build
# This creates a dist/ folder with minified files
npm run build

# Shows what the production build looks like
# Useful for testing before deploying
npm run preview

# Checks code for style issues and common mistakes
# Helps maintain consistent code quality
npm run lint

# Automatically fixes code formatting
# Makes all code follow the same style
npm run format

# Runs automated tests to catch bugs
# Tests verify that functions work as expected
npm test
```

### Adding a New Cryptocurrency to Track

To add support for a new cryptocurrency:

1. Find the coin's ID on CoinGecko (e.g., "bitcoin", "ethereum")
2. The application uses CoinGecko IDs to fetch prices
3. Users can add any coin by entering its CoinGecko ID in the form

### Performance Optimization Tips

- **Minimize API Calls**: The app automatically caches price data for 60 seconds
- **Batch Requests**: Multiple coin prices are fetched in a single API call
- **Lazy Loading**: Components load only when needed
- **Memoization**: Expensive calculations are cached using React.useMemo

<!-- 
===========================================
SECTION 7: DEPLOYING TO PRODUCTION
===========================================
-->

## Deploying to Production

### Vercel Deployment (Recommended)

Vercel offers the simplest deployment process for React applications:

1. Push your code to GitHub
2. Visit https://vercel.com and sign up
3. Click "Import Project" and select your repository
4. Vercel automatically detects it's a Vite project
5. Click "Deploy" - your app will be live in minutes

### Netlify Deployment

Another popular option with similar ease:

1. Build your project: `npm run build`
2. Visit https://netlify.com and sign up
3. Drag and drop the `dist` folder to deploy
4. Or connect your GitHub repo for automatic deployments

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
SECTION 8: TROUBLESHOOTING
===========================================
-->

## Troubleshooting

### Common Issues and Solutions

**Problem**: Prices not updating

**Solution**: Check your internet connection and verify the CoinGecko API is accessible. The app makes requests to `https://api.coingecko.com`. Check browser console for error messages.

**Problem**: "Module not found" errors

**Solution**: Delete `node_modules` folder and `package-lock.json`, then run `npm install` again.

**Problem**: Application won't start

**Solution**: Ensure you're using Node.js version 18 or higher. Check with `node --version`.

**Problem**: Staking calculations seem incorrect

**Solution**: Verify you entered the APY as a percentage (e.g., 5 for 5%, not 0.05) and the staked percentage is between 0 and 100.

<!-- 
===========================================
SECTION 9: GETTING HELP & SUPPORT
===========================================
-->

## Getting Help & Support

### Troubleshooting Resources

- Check the [Troubleshooting](#troubleshooting) section above
- Review the browser console for error messages
- Verify your Node.js version is compatible

### Getting Support

- **GitHub Issues**: Report bugs or request features at the repository's Issues page
- **Documentation**: This README covers most common use cases
- **Community**: Join discussions in the repository's Discussions section

### Additional Learning Resources

**React Documentation**: https://react.dev - Official React documentation and tutorials

**CoinGecko API Documentation**: https://www.coingecko.com/en/api/documentation - Reference for price data API

**Tailwind CSS Documentation**: https://tailwindcss.com/docs - Learn about the styling framework we use

**Node.js Documentation**: https://nodejs.org/en/docs - Official Node.js reference

**Git Documentation**: https://git-scm.com/doc - Learn how to use version control

<!-- 
===========================================
SECTION 10: CONTRIBUTION GUIDELINES
===========================================
-->

## Contributing to the Project

We welcome contributions from the community! Here's how you can help:

### How to Contribute

1. **Fork the Repository**: Click the "Fork" button on GitHub
2. **Create a Branch**: `git checkout -b feature/your-feature-name`
3. **Make Changes**: Implement your feature or bug fix
4. **Test**: Ensure all tests pass and add new tests if needed
5. **Commit**: `git commit -m "Add your descriptive commit message"`
6. **Push**: `git push origin feature/your-feature-name`
7. **Pull Request**: Open a PR on GitHub with a clear description

### Code Style Guidelines

- Follow the existing code style
- Use meaningful variable and function names
- Add comments for complex logic
- Run `npm run lint` before committing
- Format code with `npm run format`

### Reporting Bugs

When reporting bugs, please include:
- Steps to reproduce the issue
- Expected behavior
- Actual behavior
- Screenshots if applicable
- Your environment (OS, Node version, browser)

<!-- 
===========================================
SECTION 11: LICENSE & LEGAL
===========================================
-->

## License & Legal Information

This project is open source and available under the MIT License.

### Third-Party Services

This application uses the following third-party services:

- **CoinGecko API**: Free cryptocurrency price data (subject to their terms of service)
- **React**: MIT License
- **Tailwind CSS**: MIT License
- **Vite**: MIT License

### Disclaimer

This software is provided for educational and informational purposes only. It is not financial advice. Cryptocurrency investments carry risk, and you should do your own research before making investment decisions.

---

**Made with ❤️ for the crypto community**