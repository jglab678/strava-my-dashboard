# Contributing to Strava Cycling Analytics Dashboard

First off, thank you for considering contributing! This utility was created out of a desire for deeper year-on-year cycling telemetry, lifetime consistency metrics, and uncompromising personal privacy. 

Community contributions are warmly welcomed—whether you are fixing a parsing bug, improving mobile UX, suggesting a new endurance metric, or refining documentation.

---

## 🔒 The Non-Negotiable Core Principle: 100% Client-Side Privacy

This project has one foundational rule that every contribution must adhere to:

> **Zero bytes of user data may ever leave the user's browser.**

* **No server uploads, external backends, or cloud storage.**
* **No third-party trackers, analytics pixels, or telemetry beacons.**
* **All parsing, unzipping, metric calculations, and chart rendering must execute 100% locally in browser memory.**

If a proposed feature requires sending user rides or profile data to an external server or API, it cannot be accepted.

---

## 🛠️ Local Development (Zero Build Setup)

One of the great things about this project is its simplicity—there is **no complex build pipeline, no bundler, and no `node_modules` required** to develop:

1. **Fork and clone the repository**:
   ```bash
   git clone https://github.com/<your-username>/strava-my-dashboard.git
   cd strava-my-dashboard
   ```

2. **Open the application**:
   Simply open `index.html` in your browser:
   ```bash
   open index.html # On macOS (or double-click index.html)
   ```

3. **Developing with Demo Data**:
   * Click **"✨ Try Demo Preview"** on the landing page to instantly test with the fictional dataset (**Alex Rivera**, Boulder, CO).
   * You do **not** need to use your own personal Strava export while developing.
   * If you need to test file imports, you can drop any test CSV or zip archive directly onto the dropzone.

---

## 💡 Ways to Contribute

### 1. New Cycling Metrics & Analytics
Have an idea for an insightful endurance metric? Examples include:
* New consistency badges or Eddington extensions (e.g. weekly or monthly Eddington).
* Power, heart rate, or cadence distribution profiles.
* Commute vs. recreational riding splits.
* Enhanced climb categorization or gradient distribution.

*Tip: When proposing new calculations, please include the mathematical formula and column dependencies in your issue or PR.*

### 2. Strava CSV & Locale Compatibility
Strava exports can vary across countries and account configurations:
* Date formats (e.g., `"Sep 24, 2026, 8:58 AM"`, `"24/09/2026 08:58"`, ISO format).
* Missing optional columns (e.g., power meters, heart rate monitors).
* Multiline activity descriptions.

If you encounter an export format that fails to parse cleanly, reporting it or submitting a regex/parser fix is immensely valuable.

### 3. UI, Styling & Accessibility
* Responsive layout refinements for mobile screens and tablets.
* Dark mode contrast and theme consistency.
* Interactive Chart.js tooltip improvements and touch interactions.

---

## 📋 Pull Request Guidelines

1. **Keep it simple**: Prefer clean, readable, dependency-free vanilla JavaScript and modern CSS.
2. **Never commit personal data**: Ensure `.gitignore` remains respected. Never commit real Strava archives, `.fit` files, or CSVs containing private GPS routes or personal names.
3. **Test in multiple browsers**: Verify your changes in at least two modern browsers (e.g. Chrome, Firefox, Safari, Edge).
4. **Create focused PRs**: One feature or bug fix per pull request makes review fast and smooth.

---

## 🐛 Reporting Issues

* **Found a bug?** Please use the [Bug Report Template](.github/ISSUE_TEMPLATE/bug_report.md).
* **Have a feature idea?** Please use the [Feature Request Template](.github/ISSUE_TEMPLATE/feature_request.md).

Thank you for helping make endurance cycling analytics more accessible, insightful, and private for everyone! 🚴💨
