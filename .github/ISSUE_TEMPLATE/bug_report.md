---
name: Bug Report
about: Create a report to help us fix a bug or parsing issue
title: '[BUG] '
labels: bug
assignees: ''
---

### ⚠️ Privacy Reminder
**Never paste unredacted personal information!** If sharing a sample CSV line from your Strava export, redact your exact street addresses, real name, email, and GPS coordinates.

---

### Describe the Bug
A clear and concise description of what the bug is.

### Where did the issue occur?
- [ ] On the live web app (https://strava-my-dashboard.pages.dev/)
- [ ] Running locally off disk (`file:///.../index.html`)
- [ ] In the downloaded offline standalone HTML file

### Input File Type
- [ ] Strava Bulk Export `.zip` archive
- [ ] `activities.csv` directly
- [ ] Other (please specify)

### Steps to Reproduce
1. Open the application in your browser.
2. Select or drop your Strava export file.
3. Observe error / unexpected behavior.

### Expected Behavior
A clear and concise description of what you expected to happen.

### Actual Behavior / Error Message
If an error message appeared on the screen or in your browser's Developer Tools Console (`F12` or `Cmd+Option+I` -> Console tab), please paste it here:
```text
(Paste console error or status message here)
```

### CSV Header or Date Sample (If applicable)
If you suspect a date format or column naming issue, please share the header row or a redacted snippet:
```csv
Activity ID,Activity Date,Activity Name,Activity Type,...
```

### Environment Details
- **Browser**: [e.g. Chrome 129, Safari 18, Firefox 131]
- **Device**: [e.g. Mac, Windows PC, iPhone, Android]
- **Approximate Number of Rides**: [e.g. ~500, ~2,000, 5,000+]

### Additional Context
Add any other context about the problem here.
