#!/usr/bin/env python3
"""
TidyFactor Marketing Promotion & Margin Protection Calculator
Calculates break-even ROAS, gross margin impact, and discount thresholds.
"""

import sys
import json
import argparse

# Ensure UTF-8 output on Windows console
if sys.stdout and hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8", errors="replace")
if sys.stderr and hasattr(sys.stderr, "reconfigure"):
    sys.stderr.reconfigure(encoding="utf-8", errors="replace")

def calculate_promo_metrics(cogs: float, price: float, discount_percent: float, ad_spend_per_order: float = 0.0) -> dict:
    if price <= 0:
        raise ValueError("Price must be greater than 0")
        
    discount_amount = price * (discount_percent / 100.0)
    discounted_price = price - discount_amount
    gross_profit = discounted_price - cogs - ad_spend_per_order
    gross_margin_percent = (gross_profit / discounted_price) * 100.0 if discounted_price > 0 else 0.0
    
    # Break-even ROAS = 1 / Gross Margin before ads
    margin_before_ads = (discounted_price - cogs) / discounted_price if discounted_price > 0 else 0.0
    breakeven_roas = (1.0 / margin_before_ads) if margin_before_ads > 0 else 0.0

    is_margin_safe = gross_margin_percent >= 30.0 and gross_profit > 0

    return {
        "original_price": round(price, 2),
        "discount_percent": round(discount_percent, 2),
        "discount_amount": round(discount_amount, 2),
        "discounted_price": round(discounted_price, 2),
        "cogs": round(cogs, 2),
        "ad_spend_per_order": round(ad_spend_per_order, 2),
        "net_gross_profit": round(gross_profit, 2),
        "net_gross_margin_percent": round(gross_margin_percent, 2),
        "breakeven_roas": round(breakeven_roas, 2),
        "is_margin_safe": is_margin_safe,
        "recommendation": "SAFE_TO_RUN" if is_margin_safe else "HIGH_RISK_MARGIN_COMPRESSION"
    }

def main():
    parser = argparse.ArgumentParser(description="TidyFactor Margin & Promo Calculator")
    parser.add_argument("--price", type=float, default=100.0, help="Original product price")
    parser.add_argument("--cogs", type=float, default=30.0, help="Cost of Goods Sold (COGS)")
    parser.add_argument("--discount", type=float, default=20.0, help="Discount percentage (e.g. 20 for 20%)")
    parser.add_argument("--cac", type=float, default=15.0, help="Estimated ad spend / CAC per order")
    parser.add_argument("--json", action="store_true", help="Output pure JSON")

    args = parser.parse_args()

    result = calculate_promo_metrics(args.cogs, args.price, args.discount, args.cac)

    if args.json:
        print(json.dumps(result, indent=2))
    else:
        print("\n💰 TidyFactor Margin & Promotion Math Report")
        print(f"  Price: ${result['original_price']} -> Discounted: ${result['discounted_price']} (-{result['discount_percent']}%)")
        print(f"  COGS: ${result['cogs']} | Est. CAC: ${result['ad_spend_per_order']}")
        print(f"  Net Gross Profit: ${result['net_gross_profit']} ({result['net_gross_margin_percent']}%)")
        print(f"  Break-Even ROAS Target: {result['breakeven_roas']}x")
        print(f"  Status: {result['recommendation']}\n")

if __name__ == "__main__":
    main()
