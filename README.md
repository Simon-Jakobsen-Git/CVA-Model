# CVA-Model

This project builds a simple Credit Valuation Adjustment (CVA) model from scratch
to understand exposure, collateral, and margin-period-of-risk effects for an
interest rate swap.

The focus is intuition and mechanics, not production calibration.

## What this project does

- Simulates interest rate paths using a Vasicek short-rate model
- Prices a vanilla interest rate swap path-by-path
- Constructs exposure profiles (EE and PFE)
- Computes CVA using:
  - flat hazard rates
  - term hazard curves implied from CDS spreads
- Shows the impact of collateral and Margin Period of Risk (MPOR)

## Key insights demonstrated

- Exposure spikes around payment dates
- CVA timing is driven by exposure, not just default probability
- Discounting reduces CVA but does not change its shape materially
- Collateral collapses exposure except during MPOR
- Residual CVA under a CSA is driven almost entirely by gap risk

## Structure

- `notebooks/`: step-by-step notebooks showing each concept
- `src/`: reusable model components (rates, discounting, curves)

