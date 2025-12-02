# Student Score Tracking Project

This repository stores score data for multiple subjects and automatically generates trend charts using GitHub Actions.

## Subjects
- Chinese
- Math
- English
- Science
- Social

## How it works
1. Add or update CSV files in the `data/` folder.
2. GitHub Actions automatically runs the Python script.
3. Trend charts will appear in the `charts/` folder.

## CSV Format
```
date,exam,score,full_score
2025-01-10,Midterm,92,100
```
